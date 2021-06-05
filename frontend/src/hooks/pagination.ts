import * as React from 'react';
import { useHistory } from 'react-router-dom';

import { usePersistentState } from './persistentState';
import { useQuery } from './query';

export type IPagination = {
  page: number;
  setPage: React.Dispatch<React.SetStateAction<number>>;
  perPage: number;
  setPerPage: React.Dispatch<React.SetStateAction<number>>;
  numPages: number;
  setTotal: React.Dispatch<React.SetStateAction<number>>;
};

/**
 * A mega-state hook that handles pagination for arbitrary data.
 *
 * WARNING: Do not use this in a React dependency array.
 *
 * @param root0 - A configuration object.
 * @param root0.useUrl - If true, then this hook will read the initial page from the URL
 *        query string's ``page`` key and update that key whenever ``curpage``changes.
 * @returns An object with the following keys:
 *
 * - ``curPage`` - The current page.
 * - ``setCurPage`` - A function to set ``curPage``.
 * - ``perPage`` - The number of elements per page.
 * - ``setPerPage`` - A function to set ``perPage``.
 * - ``numPages`` The total number of pages. Dynamically calculated from the total
 *                number of elements.
 * - ``setTotal`` - A function to set the total number of elements.
 */
export const usePagination = ({
  useUrl = false,
}: { useUrl?: boolean } = {}): IPagination => {
  const history = useHistory();
  const query = useQuery();

  const startPage = getStartPage(useUrl, query);
  const [page, rawSetPage] = React.useState<number>(startPage);
  const [perPage, setPerPage] = usePersistentState<number>('pagination--perPage', 40);
  const [total, setTotal] = React.useState<number>(0);

  // We wrap the setCurPage function to sync the URL with the state. If ``useUrl`` is
  // true, then sync!
  const setPage = React.useCallback(
    (value: React.SetStateAction<number>) => {
      const calculatedValue = value instanceof Function ? value(page) : value;

      if (useUrl) {
        query.set('page', `${calculatedValue}`);
        history.push({
          pathname: '/releases',
          search: `?${query.toString()}`,
        });
      }

      rawSetPage(calculatedValue);
    },
    [page, history, query, useUrl, rawSetPage],
  );

  const numPages = perPage === 0 ? 0 : Math.ceil(total / perPage);

  return {
    numPages,
    page,
    perPage,
    setPage,
    setPerPage,
    setTotal,
  };
};

/**
 * Get the initial page. If ``useUrl`` is true, then source it from the URL. Otherwise,
 * return 1.
 */
const getStartPage = (useUrl: boolean, query: URLSearchParams): number => {
  const page = query.get('page');
  return useUrl && page !== null && /^\d+$/.test(page) ? parseInt(page, 10) : 1;
};

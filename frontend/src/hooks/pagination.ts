import * as React from 'react';
import { useHistory } from 'react-router-dom';

import { ISetValue, IStateValue } from '~/types';

import { usePersistentState } from './persistentState';
import { useQuery } from './query';

export type IPagination = {
  curPage: number;
  setCurPage: ISetValue<number>;
  perPage: number;
  setPerPage: ISetValue<number>;
  numPages: number;
  setTotal: ISetValue<number>;
};

/**
 * A mega-state hook that handles pagination for arbitrary data.
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
 * - ``numPages`` The total number of pages. Dynamically alculated from the total number of elements.
 * - ``setTotal`` - A function to set the total number of elements.
 */
export const usePagination = ({ useUrl = false }: { useUrl?: boolean } = {}): IPagination => {
  const history = useHistory();
  const query = useQuery();

  const startPage = getStartPage(useUrl, query);
  const [curPage, rawSetCurPage] = React.useState<number>(startPage);
  const [perPage, setPerPage] = usePersistentState<number>('pagination--perPage', 40);
  const [total, setTotal] = React.useState<number>(0);

  // We wrap the setCurPage function to sync the URL with the state. If ``useUrl`` is true, then
  // sync!
  const setCurPage = React.useCallback(
    (value: IStateValue<number>) => {
      const calculatedValue = value instanceof Function ? value(curPage) : value;

      if (useUrl) {
        query.set('page', `${calculatedValue}`);
        history.push({
          pathname: '/releases',
          search: `?${query.toString()}`,
        });
      }

      rawSetCurPage(calculatedValue);
    },
    [curPage, history, query, useUrl, rawSetCurPage],
  );

  const numPages = perPage === 0 ? 0 : Math.ceil(total / perPage);

  return { curPage, numPages, perPage, setCurPage, setPerPage, setTotal };
};

/**
 * Get the initial page. If ``useUrl`` is true, then source it from the URL. Otherwise, return 1.
 */
const getStartPage = (useUrl: boolean, query: URLSearchParams): number => {
  const page = query.get('page');
  return useUrl && page && /^\d+$/.test(page) ? parseInt(page, 10) : 1;
};

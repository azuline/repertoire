import * as React from 'react';
import { useHistory } from 'react-router-dom';
import { SetNumber } from 'src/types';

import { usePersistentState } from './persistentState';
import { useQuery } from './query';

export type PaginationT = {
  curPage: number;
  setCurPage: SetNumber;
  perPage: number;
  setPerPage: SetNumber;
  numPages: number;
  setTotal: SetNumber;
};

/**
 * A hook that handles pagination for arbitrary data.
 *
 * @param root0 A configuration object.
 * @param root0.useUrl If true, then this hook will read the initial page from the URL
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
export const usePagination = ({ useUrl = false }: { useUrl?: boolean } = {}): PaginationT => {
  const history = useHistory();
  const query = useQuery();

  // Get the initial page. If ``useUrl`` is true, then source it from the URL.
  // Otherwise, return 1.
  const startPage = React.useMemo(() => {
    if (!useUrl || !query.get('page') || !/^\d+$/.test(query.get('page') as string)) {
      return 1;
    }

    return parseInt(query.get('page') as string, 10);
  }, [useUrl, query]);

  const [curPage, setCurPage] = React.useState<number>(startPage);
  const [perPage, setPerPage] = usePersistentState<number>('pagination--perPage', 40);
  const [total, setTotal] = React.useState<number>(0);

  // If ``useUrl`` is true, then sync the URL's page parameter whenever ``curPage``
  // changes.
  React.useEffect(() => {
    if (!useUrl) return;

    query.set('page', `${curPage}`);

    history.push({
      pathname: '/releases',
      search: `?${query.toString()}`,
    });
  }, [curPage]);

  // Calculate the number of pages.
  const numPages = React.useMemo(() => {
    if (perPage === 0) return 0;

    return Math.ceil(total / perPage);
  }, [total, perPage]);

  return { curPage, setCurPage, perPage, setPerPage, numPages, setTotal };
};

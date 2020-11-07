import * as React from 'react';

import { usePersistentState } from './persistentState';
import { useQuery } from './query';
import { useHistory } from 'react-router-dom';

export type PaginationType = {
  curPage: number;
  setCurPage: (arg0: number) => void;
  perPage: number;
  setPerPage: (arg0: number) => void;
  total: number;
  setTotal: (arg0: number) => void;
  numPages: number;
};

type Params = {
  useUrl?: boolean;
};

export const usePagination = ({ useUrl = false }: Params = {}): PaginationType => {
  const history = useHistory();
  const query = useQuery();

  const startPage = React.useMemo(() => {
    if (!useUrl || !query.get('page') || !/^\d+$/.test(query.get('page') as string)) {
      return 1;
    }

    return parseInt(query.get('page') as string);
  }, [useUrl, query]);

  const [curPage, setCurPage] = React.useState<number>(startPage);
  const [perPage, setPerPage] = usePersistentState<number>('pagination--perPage', 50);
  const [total, setTotal] = React.useState<number>(0);

  React.useEffect(() => {
    if (!useUrl) return;

    query.set('page', `${curPage}`);

    history.push({
      pathname: '/releases',
      search: '?' + query.toString(),
    });
  }, [curPage]);

  const numPages = React.useMemo(() => {
    if (perPage === 0) return 0;

    return Math.ceil(total / perPage);
  }, [total, perPage]);

  return { curPage, setCurPage, perPage, setPerPage, total, setTotal, numPages };
};

import * as React from 'react';

import { usePersistentState } from './persistentState';

export type PCType = {
  curPage: number;
  setCurPage: (arg0: number) => void;
  perPage: number;
  setPerPage: (arg0: number) => void;
  total: number;
  setTotal: (arg0: number) => void;
  numPages: number;
};

export const usePagination = (): PCType => {
  const [curPage, setCurPage] = React.useState<number>(1);
  const [perPage, setPerPage] = usePersistentState<number>('pagination--perPage', 50);
  const [total, setTotal] = React.useState<number>(0);

  const numPages = React.useMemo(() => {
    if (perPage === 0) return 0;

    return Math.ceil(total / perPage);
  }, [total, perPage]);

  return { curPage, setCurPage, perPage, setPerPage, total, setTotal, numPages };
};

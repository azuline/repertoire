import * as React from 'react';

export type PCType = {
  curPage: number;
  setCurPage: (arg0: number) => void;
  perPage: number;
  setPerPage: (arg0: number) => void;
  total: number;
  setTotal: (arg0: number) => void;
  numPages: number;
};

export const PaginationContext = React.createContext<PCType>({
  curPage: 1,
  setCurPage: () => {},
  perPage: 50,
  setPerPage: () => {},
  total: 0,
  setTotal: () => {},
  numPages: 0,
});

export const PaginationProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [curPage, setCurPage] = React.useState<number>(1);
  const [perPage, setPerPage] = React.useState<number>(50);
  const [total, setTotal] = React.useState<number>(0);

  const numPages = React.useMemo(() => {
    if (perPage === 0) return 0;

    return Math.ceil(total / perPage);
  }, [total, perPage]);

  const value = {
    curPage,
    setCurPage,
    perPage,
    setPerPage,
    total,
    setTotal,
    numPages,
  };

  return <PaginationContext.Provider value={value}>{children}</PaginationContext.Provider>;
};

import * as React from 'react';

type PCType = {
  curPage: number;
  setCurPage: (arg0: number) => void;
  perPage: number;
  setPerPage: (arg0: number) => void;
  total: number;
  setTotal: (arg0: number) => void;
};

export const PaginationContext = React.createContext<PCType>({
  curPage: 1,
  setCurPage: () => {},
  perPage: 50,
  setPerPage: () => {},
  total: 0,
  setTotal: () => {},
});

export const PaginationProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [curPage, setCurPage] = React.useState(1);
  const [perPage, setPerPage] = React.useState(50);
  const [total, setTotal] = React.useState(0);

  const numPages = React.useMemo(() => (perPage !== 0 ? total / perPage : 0), [
    total,
    perPage,
  ]);

  const value = {
    curPage,
    setCurPage,
    perPage,
    setPerPage,
    total,
    setTotal,
    numPages,
  };

  return (
    <PaginationContext.Provider value={value}>{children}</PaginationContext.Provider>
  );
};

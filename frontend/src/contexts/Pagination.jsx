import React, { useState } from 'react';

export const PaginationContext = React.createContext({
  page: 1,
  setPage: () => {},
  numPages: 1,
  setNumPages: () => {},
  perPage: 50,
  setPerPage: () => {},
});

export const ReleasePaginationContextProvider = ({ children }) => {
  const [page, setPage] = useState(1);
  const [numPages, setNumPages] = useState(1);
  const [perPage, setPerPage] = useState(50);

  const value = { page, setPage, numPages, setNumPages, perPage, setPerPage };

  return (
    <PaginationContext.Provider value={value}>{children}</PaginationContext.Provider>
  );
};

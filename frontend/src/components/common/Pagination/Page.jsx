import React, { useContext, useCallback } from 'react';
import { PaginationContext } from 'contexts';
import { Button } from '@blueprintjs/core';

export const Page = ({ page }) => {
  const { page: activePage, setPage } = useContext(PaginationContext);

  const goToPage = useCallback(() => setPage(page), [page, setPage]);

  return (
    <Button
      className="Page"
      intent={page === activePage ? 'primary' : undefined}
      onClick={goToPage}
    >
      {page}
    </Button>
  );
};

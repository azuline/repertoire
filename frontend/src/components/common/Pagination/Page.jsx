import React, { useCallback, useContext } from 'react';

import { Button } from '@blueprintjs/core';
import { PaginationContext } from 'contexts';

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

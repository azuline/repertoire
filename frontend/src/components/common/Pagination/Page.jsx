import React, { useContext, useCallback } from 'react';
import { PaginationContext } from 'contexts';

export const Page = ({ page }) => {
  const { page: activePage, setPage } = useContext(PaginationContext);

  const goToPage = useCallback(() => setPage(page), [page, setPage]);

  return (
    <div className={'Page' + (page === activePage ? ' active' : '')} onClick={goToPage}>
      {page}
    </div>
  );
};

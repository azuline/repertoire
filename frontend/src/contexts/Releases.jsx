import React, { useContext, useEffect, useState } from 'react';

import { PaginationContext } from './Pagination';
import { SearchContext } from './Search';
import { AuthenticationContext } from './Authentication';
import { SortContext } from './Sort';
import { parseQuery } from 'common/queries';
import { queryReleases } from 'requests';

export const ReleasesContext = React.createContext({
  releases: [],
  setReleases: () => {},
});

export const ReleasesContextProvider = ({ children }) => {
  const [releases, setReleases] = useState([]);

  const { activeQuery } = useContext(SearchContext);
  const { asc, sortField } = useContext(SortContext);
  const { page, perPage, setNumPages } = useContext(PaginationContext);
  const { token } = useContext(AuthenticationContext);

  // On changes to the search query and release view options, update the
  // releases list.
  useEffect(() => {
    (async () => {
      if (token) {
        const [search, collections, artists] = parseQuery(activeQuery);
        const { releases, total } = await queryReleases(
          token,
          search,
          collections,
          artists,
          page,
          perPage,
          sortField,
          asc
        );
        setReleases(releases);
        setNumPages(Math.ceil(total / perPage));
      }
    })();
  }, [token, activeQuery, setReleases, page, perPage, setNumPages, sortField, asc]);

  const value = { releases, setReleases };

  return <ReleasesContext.Provider value={value}>{children}</ReleasesContext.Provider>;
};

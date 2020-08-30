import React, { useContext, useEffect, useState } from 'react';

import { PaginationContext } from './Pagination';
import { SearchContext } from './Search';
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

  // On changes to the search query and release view options, update the
  // releases list.
  useEffect(() => {
    (async () => {
      const [search, collections, artists] = parseQuery(activeQuery);
      const { releases, total } = await queryReleases(
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
    })();
  }, [activeQuery, setReleases, page, perPage, setNumPages, sortField, asc]);

  const value = { releases, setReleases };

  return <ReleasesContext.Provider value={value}>{children}</ReleasesContext.Provider>;
};

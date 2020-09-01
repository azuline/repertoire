import React, { useContext, useEffect, useState } from 'react';

import { AuthenticationContext } from './Authentication';
import { PaginationContext } from './Pagination';
import { SearchContext } from './Search';
import { SortContext } from './Sort';
import { parseQuery } from 'common/queries';
import { useRequest } from 'hooks';
import { TopToaster } from 'components/Toaster';

export const ReleasesContext = React.createContext({
  releases: [],
  setReleases: () => {},
});

export const ReleasesContextProvider = ({ children }) => {
  const request = useRequest();
  const [releases, setReleases] = useState([]);
  const { activeQuery } = useContext(SearchContext);
  const { asc, sortField } = useContext(SortContext);
  const { page, perPage, setNumPages } = useContext(PaginationContext);
  const { token } = useContext(AuthenticationContext);

  // On changes to the search query and release view options, update the
  // releases list.
  useEffect(() => {
    if (!token) return;
    TopToaster.show({ icon: 'music', message: 'Loading releases...', timeout: 1000 });

    (async () => {
      const [search, collections, artists] = parseQuery(activeQuery);

      const response = await request(
        '/api/releases?' +
          new URLSearchParams({
            search: search ?? '',
            collections: JSON.stringify(collections ?? []),
            artists: JSON.stringify(artists ?? []),
            page: page ?? '',
            perPage: perPage ?? '',
            sort: sortField ?? '',
            asc: asc ?? '',
          })
      );
      const { releases, total } = await response.json();

      setReleases(releases);
      setNumPages(Math.ceil(total / perPage));
    })();
  }, [
    token,
    request,
    activeQuery,
    setReleases,
    page,
    perPage,
    setNumPages,
    sortField,
    asc,
  ]);

  const value = { releases, setReleases };

  return <ReleasesContext.Provider value={value}>{children}</ReleasesContext.Provider>;
};

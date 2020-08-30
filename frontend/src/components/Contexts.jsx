import {
  ArtistsContextProvider,
  ReleasesContextProvider,
  ReleasePaginationContextProvider,
  CollectionsContextProvider,
  QueriesContextProvider,
  SearchContextProvider,
  ThemeContextProvider,
  ReleaseSortContextProvider,
  ReleaseViewContextProvider,
} from 'contexts';

import React from 'react';

export const Contexts = ({ children }) => {
  return (
    <ReleasesContextProvider>
      <ReleaseSortContextProvider>
        <ReleaseViewContextProvider>
          <ReleasePaginationContextProvider>
            <SearchContextProvider>
              <ThemeContextProvider>
                <CollectionsContextProvider>
                  <ArtistsContextProvider>
                    <QueriesContextProvider>{children}</QueriesContextProvider>
                  </ArtistsContextProvider>
                </CollectionsContextProvider>
              </ThemeContextProvider>
            </SearchContextProvider>
          </ReleasePaginationContextProvider>
        </ReleaseViewContextProvider>
      </ReleaseSortContextProvider>
    </ReleasesContextProvider>
  );
};

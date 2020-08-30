import {
  ArtistsContextProvider,
  CollectionsContextProvider,
  QueriesContextProvider,
  ReleasePaginationContextProvider,
  ReleaseSortContextProvider,
  ReleaseViewContextProvider,
  ReleasesContextProvider,
  SearchContextProvider,
  ThemeContextProvider,
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

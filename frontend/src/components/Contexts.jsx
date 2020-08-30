import {
  AuthenticationContextProvider,
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
    <AuthenticationContextProvider>
      <SearchContextProvider>
        <ReleaseSortContextProvider>
          <ReleaseViewContextProvider>
            <ReleasePaginationContextProvider>
              <ReleasesContextProvider>
                <ThemeContextProvider>
                  <CollectionsContextProvider>
                    <ArtistsContextProvider>
                      <QueriesContextProvider>{children}</QueriesContextProvider>
                    </ArtistsContextProvider>
                  </CollectionsContextProvider>
                </ThemeContextProvider>
              </ReleasesContextProvider>
            </ReleasePaginationContextProvider>
          </ReleaseViewContextProvider>
        </ReleaseSortContextProvider>
      </SearchContextProvider>
    </AuthenticationContextProvider>
  );
};

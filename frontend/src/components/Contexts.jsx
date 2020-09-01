import {
  ArtistsContextProvider,
  AuthenticationContextProvider,
  CollectionsContextProvider,
  QueriesContextProvider,
  ReleasePaginationContextProvider,
  ReleaseSortContextProvider,
  ReleaseViewContextProvider,
  ReleasesContextProvider,
  SearchContextProvider,
  ThemeContextProvider,
  NowPlayingContextProvider,
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
                      <QueriesContextProvider>
                        <NowPlayingContextProvider>
                          {children}
                        </NowPlayingContextProvider>
                      </QueriesContextProvider>
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

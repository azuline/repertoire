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
      <CollectionsContextProvider>
        <ArtistsContextProvider>
          <SearchContextProvider>
            <ReleaseSortContextProvider>
              <ReleaseViewContextProvider>
                <ReleasePaginationContextProvider>
                  <ReleasesContextProvider>
                    <ThemeContextProvider>
                      <QueriesContextProvider>
                        <NowPlayingContextProvider>
                          {children}
                        </NowPlayingContextProvider>
                      </QueriesContextProvider>
                    </ThemeContextProvider>
                  </ReleasesContextProvider>
                </ReleasePaginationContextProvider>
              </ReleaseViewContextProvider>
            </ReleaseSortContextProvider>
          </SearchContextProvider>
        </ArtistsContextProvider>
      </CollectionsContextProvider>
    </AuthenticationContextProvider>
  );
};

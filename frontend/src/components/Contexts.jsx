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
              <CollectionsContextProvider>
                <ArtistsContextProvider>
                  <ReleasesContextProvider>
                    <ThemeContextProvider>
                      <QueriesContextProvider>
                        <NowPlayingContextProvider>
                          {children}
                        </NowPlayingContextProvider>
                      </QueriesContextProvider>
                    </ThemeContextProvider>
                  </ReleasesContextProvider>
                </ArtistsContextProvider>
              </CollectionsContextProvider>
            </ReleasePaginationContextProvider>
          </ReleaseViewContextProvider>
        </ReleaseSortContextProvider>
      </SearchContextProvider>
    </AuthenticationContextProvider>
  );
};

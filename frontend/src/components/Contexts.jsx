import {
  ArtistsContextProvider,
  CollectionsContextProvider,
  RecentQueriesContextProvider,
  SearchContextProvider,
  ThemeContextProvider,
} from 'contexts';

import React from 'react';

export const Contexts = ({ children }) => {
  return (
    <RecentQueriesContextProvider>
      <SearchContextProvider>
        <ThemeContextProvider>
          <CollectionsContextProvider>
            <ArtistsContextProvider>{children}</ArtistsContextProvider>
          </CollectionsContextProvider>
        </ThemeContextProvider>
      </SearchContextProvider>
    </RecentQueriesContextProvider>
  );
};

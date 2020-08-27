import React from 'react';
import {
  SearchContextProvider,
  ThemeContextProvider,
  RecentQueriesContextProvider,
  CollectionsContextProvider,
  ArtistsContextProvider,
} from 'contexts';

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

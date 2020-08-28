import {
  ArtistsContextProvider,
  CollectionsContextProvider,
  QueriesContextProvider,
  SearchContextProvider,
  ThemeContextProvider,
} from 'contexts';

import React from 'react';

export const Contexts = ({ children }) => {
  return (
    <SearchContextProvider>
      <ThemeContextProvider>
        <CollectionsContextProvider>
          <ArtistsContextProvider>
            <QueriesContextProvider>{children}</QueriesContextProvider>
          </ArtistsContextProvider>
        </CollectionsContextProvider>
      </ThemeContextProvider>
    </SearchContextProvider>
  );
};

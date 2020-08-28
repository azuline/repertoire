import {
  ArtistsContextProvider,
  CollectionsContextProvider,
  SearchContextProvider,
  ThemeContextProvider,
} from 'contexts';

import React from 'react';

export const Contexts = ({ children }) => {
  return (
    <SearchContextProvider>
      <ThemeContextProvider>
        <CollectionsContextProvider>
          <ArtistsContextProvider>{children}</ArtistsContextProvider>
        </CollectionsContextProvider>
      </ThemeContextProvider>
    </SearchContextProvider>
  );
};

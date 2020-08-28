import React, { useState } from 'react';

import { usePersistentState } from 'hooks';

export const FilterContext = React.createContext({
  filter: '',
  setFilter: () => {},
  selection: '',
  setSelection: () => {},
});

const providerGenerator = ({ selectionKey }) => {
  return ({ children }) => {
    const [filter, setFilter] = useState('');
    const [selection, setSelection] = usePersistentState(selectionKey, 'All');

    const value = { filter, setFilter, selection, setSelection };

    return <FilterContext.Provider value={value}>{children}</FilterContext.Provider>;
  };
};

const artistSpec = { selectionKey: 'artists--artistType' };

export const ArtistFilterContextProvider = providerGenerator(artistSpec);

const collectionSpec = { selectionKey: 'collections--collectionType' };

export const CollectionFilterContextProvider = providerGenerator(collectionSpec);

const querySpec = { selectionKey: 'queries--queryType' };

export const QueryFilterContextProvider = providerGenerator(querySpec);

import React, { useEffect, useState } from 'react';

export const FilterContext = React.createContext({
  filter: '',
  setFilter: () => {},
  selection: '',
  setSelection: () => {},
});

const providerGenerator = ({ selectionKey }) => {
  const localSelection = localStorage.getItem(selectionKey) ?? 'All';

  return ({ children }) => {
    const [filter, setFilter] = useState('');
    const [selection, setSelection] = useState(localSelection);

    useEffect(() => localStorage.setItem(selectionKey, selection), [selection]);

    const value = { filter, setFilter, selection, setSelection };

    return <FilterContext.Provider value={value}>{children}</FilterContext.Provider>;
  };
};

const artistSpec = { selectionKey: 'artists--artistType' };

export const ArtistFilterContextProvider = providerGenerator(artistSpec);

const collectionSpec = { selectionKey: 'collections--collectionType' };

export const CollectionFilterContextProvider = providerGenerator(collectionSpec);

import React, { useEffect, useState } from 'react';
import Fuse from 'fuse.js';
import { mockArtists } from 'mockData';
import { fuseOptions } from 'common/fuse';

export const ArtistsContext = React.createContext({
  artists: [],
  fuse: null,
  setArtists: () => {},
});

export const ArtistsContextProvider = ({ children }) => {
  const [artists, setArtists] = useState(mockArtists);
  const fuse = new Fuse(artists, { ...fuseOptions, keys: ['name'] });

  useEffect(() => fuse.setCollection(artists), [fuse, artists]);

  const value = { artists, fuse, setArtists };

  return <ArtistsContext.Provider value={value}>{children}</ArtistsContext.Provider>;
};

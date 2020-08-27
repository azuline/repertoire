import React, { useEffect, useState } from 'react';

import Fuse from 'fuse.js';
import { fuseOptions } from 'common/fuse';
import { mockArtists } from 'mockData';

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

import React, { useEffect, useState } from 'react';

import Fuse from 'fuse.js';
import { fuseOptions } from 'common/fuse';
import { fetchArtists } from 'requests';

export const ArtistsContext = React.createContext({
  artists: [],
  setArtists: () => {},
  fuse: null,
  fetched: false,
});

export const ArtistsContextProvider = ({ children }) => {
  const [artists, setArtists] = useState([]);
  const [fetched, setFetched] = useState(false);
  const fuse = new Fuse(artists, { ...fuseOptions, keys: ['name'] });

  useEffect(() => fuse.setCollection(artists), [fuse, artists]);

  useEffect(() => {
    (async () => {
      setArtists(await fetchArtists());
      setFetched(true);
    })();
  }, []);

  const value = { artists, setArtists, fuse, fetched };

  return <ArtistsContext.Provider value={value}>{children}</ArtistsContext.Provider>;
};

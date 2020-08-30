import React, { useContext, useEffect, useState } from 'react';

import Fuse from 'fuse.js';
import { fetchArtists } from 'requests';
import { fuseOptions } from 'common/fuse';
import { AuthenticationContext } from './Authentication';

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

  const { token } = useContext(AuthenticationContext);

  useEffect(() => fuse.setCollection(artists), [fuse, artists]);

  useEffect(() => {
    (async () => {
      if (token) {
        setArtists(await fetchArtists(token));
        setFetched(true);
      }
    })();
  }, [token]);

  const value = { artists, setArtists, fuse, fetched };

  return <ArtistsContext.Provider value={value}>{children}</ArtistsContext.Provider>;
};

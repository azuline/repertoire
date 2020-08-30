import React, { useContext, useEffect, useState } from 'react';

import { AuthenticationContext } from './Authentication';
import Fuse from 'fuse.js';
import { fuseOptions } from 'common/fuse';
import { useRequest } from 'hooks';

export const ArtistsContext = React.createContext({
  artists: [],
  setArtists: () => {},
  fuse: null,
});

export const ArtistsContextProvider = ({ children }) => {
  const request = useRequest();
  const [artists, setArtists] = useState([]);
  const { token } = useContext(AuthenticationContext);

  const fuse = new Fuse(artists, { ...fuseOptions, keys: ['name'] });

  useEffect(() => fuse.setCollection(artists), [fuse, artists]);

  useEffect(() => {
    if (!token) return;

    (async () => {
      const response = await request('/api/artists');
      setArtists(await response.json());
    })();
  }, [token, request, setArtists]);

  const value = { artists, setArtists, fuse };

  return <ArtistsContext.Provider value={value}>{children}</ArtistsContext.Provider>;
};

import './index.scss';

import { ArtistFilterContextProvider, ArtistSortContextProvider } from 'contexts';

import { Artists } from './Artists';
import { ListOptions } from './ListOptions';
import React from 'react';

export const ArtistList = () => {
  return (
    <div className="ArtistList">
      <ArtistSortContextProvider>
        <ArtistFilterContextProvider>
          <ListOptions />
          <Artists />
        </ArtistFilterContextProvider>
      </ArtistSortContextProvider>
    </div>
  );
};

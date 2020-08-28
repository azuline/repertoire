import './index.scss';

import { ArtistFilterContextProvider, ArtistSortContextProvider } from 'contexts';

import { Artists } from './Artists';
import { ListOptions } from 'components/common/ListOptions';
import React from 'react';

const selections = ['All', 'Favorite'];

const sortCriteria = {
  name: { label: 'Name', icon: 'highlight' },
  releaseCount: { label: 'Release Count', icon: 'numerical' },
  random: { label: 'Random', icon: 'random' },
  fuzzyScore: { label: 'Fuzzy Score', icon: 'sort-numerical' },
};

export const ArtistList = () => {
  return (
    <div className="ArtistList">
      <ArtistSortContextProvider>
        <ArtistFilterContextProvider>
          <ListOptions selections={selections} sortCriteria={sortCriteria} />
          <Artists />
        </ArtistFilterContextProvider>
      </ArtistSortContextProvider>
    </div>
  );
};

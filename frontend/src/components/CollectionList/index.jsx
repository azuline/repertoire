import './index.scss';

import {
  CollectionFilterContextProvider,
  CollectionSortContextProvider,
} from 'contexts';

import { Collections } from './Collections';
import { ListOptions } from 'components/common/ListOptions';
import React from 'react';
import { collectionTypeNamesToIds } from 'common/collections';

const selections = ['All', 'Favorite', ...Object.keys(collectionTypeNamesToIds)];

const sortCriteria = {
  recentlyUpdated: { label: 'Recently Updated', icon: 'time' },
  name: { label: 'Name', icon: 'highlight' },
  releaseCount: { label: 'Release Count', icon: 'numerical' },
  random: { label: 'Random', icon: 'random' },
  fuzzyScore: { label: 'Fuzzy Score', icon: 'sort-numerical' },
};

export const CollectionList = () => {
  return (
    <div className="CollectionList">
      <CollectionSortContextProvider>
        <CollectionFilterContextProvider>
          <ListOptions selections={selections} sortCriteria={sortCriteria} />
          <Collections />
        </CollectionFilterContextProvider>
      </CollectionSortContextProvider>
    </div>
  );
};

import './index.scss';

import { QueryFilterContextProvider, QuerySortContextProvider } from 'contexts';

import React from 'react';
import { ListOptions } from 'components/common/ListOptions';
import { Queries } from './Queries';

const selections = ['All', 'Favorite'];

const sortCriteria = {
  recentlyAdded: { label: 'Recently Added', icon: 'time' },
  name: { label: 'Name', icon: 'highlight' },
  releaseCount: { label: 'Release Count', icon: 'numerical' },
  random: { label: 'Random', icon: 'random' },
  fuzzyScore: { label: 'Fuzzy Score', icon: 'sort-numerical' },
};

export const QueryList = () => {
  return (
    <div className="QueryList">
      <QuerySortContextProvider>
        <QueryFilterContextProvider>
          <ListOptions selections={selections} sortCriteria={sortCriteria} />
          <Queries />
        </QueryFilterContextProvider>
      </QuerySortContextProvider>
    </div>
  );
};

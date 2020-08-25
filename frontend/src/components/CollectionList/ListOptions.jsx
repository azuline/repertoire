import { Filter } from 'components/common/Filter';
import React from 'react';
import { SortBy } from 'components/common/SortBy';
import { collectionTypeNamesToIds } from 'common/collections';

// HTML Select has no icon support, blueprint select is confusing as fuck...
const sortCriteria = {
  1: { icon: 'time', id: 1, name: 'Recently Updated' },
  2: { icon: 'highlight', id: 2, name: 'Name' },
  3: { icon: 'numerical', id: 3, name: 'Release Count' },
  4: { icon: 'random', id: 4, name: 'Random' },
};

const selections = ['All', 'Favorite', ...Object.keys(collectionTypeNamesToIds)];

export const ListOptions = () => {
  return (
    <div className="ListOptions">
      <Filter selections={selections} />
      <SortBy criteria={sortCriteria} />
    </div>
  );
};

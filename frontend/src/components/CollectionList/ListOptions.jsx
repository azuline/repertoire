import { Filter } from 'components/common/Filter';
import React from 'react';
import { SortBy } from 'components/common/SortBy';
import { collectionTypeNamesToIds } from 'common/collections';

/* eslint-disable */
const sortCriteria = {
  'Recently Updated': { icon: 'time' },
  Name: { icon: 'highlight' },
  'Release Count': { icon: 'numerical' },
  Random: { icon: 'random' },
};
/* eslint-enable */

const selections = ['All', 'Favorite', ...Object.keys(collectionTypeNamesToIds)];

export const ListOptions = () => {
  return (
    <div className="ListOptions">
      <Filter selections={selections} />
      <SortBy criteria={sortCriteria} />
    </div>
  );
};

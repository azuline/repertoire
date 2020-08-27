import { Filter } from 'components/common/Filter';
import React from 'react';
import { SortBy } from 'components/common/SortBy';

/* eslint-disable */
const sortCriteria = {
  Name: { icon: 'highlight' },
  'Release Count': { icon: 'numerical' },
  Random: { icon: 'random' },
  'Fuzzy Score': { icon: 'sort-numerical' },
};
/* eslint-enable */

const selections = ['All', 'Favorite'];

export const ListOptions = () => {
  return (
    <div className="ListOptions">
      <Filter selections={selections} />
      <SortBy criteria={sortCriteria} />
    </div>
  );
};

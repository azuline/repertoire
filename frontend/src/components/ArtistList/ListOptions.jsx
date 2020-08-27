import { Filter } from 'components/common/Filter';
import React from 'react';
import { SortBy } from 'components/common/SortBy';

const sortCriteria = {
  name: { label: 'Name', icon: 'highlight' },
  releaseCount: { label: 'Release Count', icon: 'numerical' },
  random: { label: 'Random', icon: 'random' },
  fuzzyScore: { label: 'Fuzzy Score', icon: 'sort-numerical' },
};

const selections = ['All', 'Favorite'];

export const ListOptions = () => {
  return (
    <div className="ListOptions">
      <Filter selections={selections} />
      <SortBy criteria={sortCriteria} />
    </div>
  );
};

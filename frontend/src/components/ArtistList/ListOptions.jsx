import { Filter } from 'components/common/Filter';
import React from 'react';
import { SortBy } from 'components/common/SortBy';

// HTML Select has no icon support, blueprint select is confusing as fuck...
const sortCriteria = {
  1: { icon: 'highlight', id: 1, name: 'Name' },
  2: { icon: 'numerical', id: 2, name: 'Release Count' },
  3: { icon: 'random', id: 3, name: 'Random' },
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

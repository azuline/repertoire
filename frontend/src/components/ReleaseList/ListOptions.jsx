import React from 'react';
import { SearchBar } from './SearchBar';
import { SortBy } from 'components/common/SortBy';
import { ViewAs } from 'components/common/ViewAs';

const sortCriteria = {
  1: { icon: 'time', id: 1, name: 'Time Added' },
  2: { icon: 'highlight', id: 2, name: 'Title' },
  3: { icon: 'calendar', id: 3, name: 'Year' },
  4: { icon: 'random', id: 4, name: 'Random' },
};

const viewCriteria = ['Detailed', 'Compact', 'Artwork'];

export const ListOptions = () => {
  return (
    <div className="ListOptions">
      <SearchBar />
      <div className="ViewOptions">
        <SortBy criteria={sortCriteria} />
        <ViewAs criteria={viewCriteria} />
      </div>
    </div>
  );
};

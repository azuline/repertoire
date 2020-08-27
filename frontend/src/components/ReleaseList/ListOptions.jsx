import React from 'react';
import { SearchBar } from './SearchBar';
import { SortBy } from 'components/common/SortBy';
import { ViewAs } from './ViewAs';

const sortCriteria = {
  recentlyAdded: { label: 'Recently Added', icon: 'time' },
  title: { label: 'Title', icon: 'highlight' },
  year: { label: 'Year', icon: 'calendar' },
  random: { label: 'Random', icon: 'random' },
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

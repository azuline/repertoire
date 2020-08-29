import React from 'react';
import { SearchBar } from './SearchBar';
import { SortBy } from 'components/common/SortBy';
import { ViewAs } from './ViewAs';
import { PerPage } from './PerPage';

const sortCriteria = {
  recentlyAdded: { label: 'Recently Added', icon: 'time' },
  title: { label: 'Title', icon: 'highlight' },
  year: { label: 'Year', icon: 'calendar' },
  random: { label: 'Random', icon: 'random' },
};

const viewCriteria = ['Detailed', 'Compact', 'Artwork'];

export const ReleaseListOptions = () => {
  return (
    <div className="ReleaseListOptions">
      <SearchBar />
      <div className="ViewOptions">
        <SortBy criteria={sortCriteria} />
        <div className="ViewOptionsBottomRow">
          <PerPage />
          <ViewAs criteria={viewCriteria} />
        </div>
      </div>
    </div>
  );
};

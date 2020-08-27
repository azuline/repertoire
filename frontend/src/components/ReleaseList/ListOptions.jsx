import React from 'react';
import { SearchBar } from './SearchBar';
import { SortBy } from 'components/common/SortBy';
import { ViewAs } from './ViewAs';

/* eslint-disable */
const sortCriteria = {
  'Recently Added': { icon: 'time' },
  Title: { icon: 'highlight' },
  Year: { icon: 'calendar' },
  Random: { icon: 'random' },
};
/* eslint-enable */

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

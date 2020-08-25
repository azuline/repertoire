import './index.scss';

import { FilterContext, SortContext } from 'components/Contexts';
import React, { useEffect } from 'react';
import { useFilterContext, useSortContext } from 'components/Hooks';

import { Artists } from './Artists';
import { ListOptions } from './ListOptions';

// Fetch the initial context variables from localStorage.
const initialAsc = localStorage.getItem('artists--asc');
const initialSortField = localStorage.getItem('artists--sortField');
const initialArtistType = localStorage.getItem('artists--artistType');
const initialFilter = localStorage.getItem('artists--filter');

export const ArtistList = () => {
  const [asc, sortField, sortValue] = useSortContext(initialAsc, initialSortField);

  useEffect(() => localStorage.setItem('artists--asc', asc), [asc]);
  useEffect(() => localStorage.setItem('artists--sortField', sortField), [sortField]);

  const [filter, artistType, filterValue] = useFilterContext(
    initialFilter,
    initialArtistType
  );
  useEffect(() => localStorage.setItem('artists--filter', filter), [filter]);
  useEffect(() => localStorage.setItem('artists--artistType', artistType), [
    artistType,
  ]);

  return (
    <div className="ArtistList">
      <SortContext.Provider value={sortValue}>
        <FilterContext.Provider value={filterValue}>
          <ListOptions />
          <Artists />
        </FilterContext.Provider>
      </SortContext.Provider>
    </div>
  );
};

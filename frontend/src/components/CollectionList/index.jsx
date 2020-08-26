import './index.scss';

import { FilterContext, SortContext } from 'contexts';
import React, { useEffect } from 'react';
import { useFilterContext, useSortContext } from 'hooks';

import { Collections } from './Collections';
import { ListOptions } from './ListOptions';

// Fetch the stored context variables from localStorage.
const initialAsc = localStorage.getItem('collections--asc');
const initialSortField = localStorage.getItem('collections--sortField');
const initialFilter = localStorage.getItem('collections--filter');
const initialCollectionType = localStorage.getItem('collections--collectionType');

export const CollectionList = () => {
  // Set up the sort context variables.
  const [asc, sortField, sortValue] = useSortContext(initialAsc, initialSortField);

  useEffect(() => localStorage.setItem('collections--asc', asc), [asc]);
  useEffect(() => localStorage.setItem('collections--sortField', sortField), [
    sortField,
  ]);

  // Set up the filter context variables
  const [filter, collectionType, filterValue] = useFilterContext(
    initialFilter,
    initialCollectionType
  );

  useEffect(() => localStorage.setItem('collections--filter', filter), [filter]);
  useEffect(() => localStorage.setItem('collections--collectionType', collectionType), [
    collectionType,
  ]);

  return (
    <div className="CollectionList">
      <SortContext.Provider value={sortValue}>
        <FilterContext.Provider value={filterValue}>
          <ListOptions />
          <Collections />
        </FilterContext.Provider>
      </SortContext.Provider>
    </div>
  );
};

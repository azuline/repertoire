import './index.scss';

import React, { useEffect } from 'react';
import { SortContext, ViewContext } from 'contexts';
import { useReleaseViewContext, useSortContext } from 'hooks';

import { ListOptions } from './ListOptions';
import { Releases } from './Releases';

// Fetch the stored context variables from localStorage.
const initialAsc = localStorage.getItem('releases--asc');
const initialSortField = localStorage.getItem('releases--sortField');
const initialView = localStorage.getItem('releases--view');
const initialExpandTrackLists = localStorage.getItem('releases--expandTrackLists');

export const ReleaseList = () => {
  const [asc, sortField, sortValue] = useSortContext(initialAsc, initialSortField);

  useEffect(() => localStorage.setItem('releases--asc', asc), [asc]);
  useEffect(() => localStorage.setItem('releases--sortField', sortField), [sortField]);

  const [view, expandTrackLists, releaseViewValue] = useReleaseViewContext(
    initialView,
    initialExpandTrackLists
  );

  useEffect(() => localStorage.setItem('releases--view', view), [view]);
  useEffect(
    () => localStorage.setItem('releases--expandTrackLists', expandTrackLists),
    [expandTrackLists]
  );

  return (
    <div className="ReleaseList">
      <SortContext.Provider value={sortValue}>
        <ViewContext.Provider value={releaseViewValue}>
          <ListOptions />
          <Releases />
        </ViewContext.Provider>
      </SortContext.Provider>
    </div>
  );
};

import React, { useContext, useMemo } from 'react';
import { SortContext, ViewContext } from 'contexts';

import { Release } from 'components/Release';
import { mockReleases } from 'mockData';
import { random, recentlyAdded, title, year } from 'common/sorts';

// Functions to sort the releases by.
const sortFunctions = { recentlyAdded, title, year, random };

export const Releases = () => {
  const { asc, sortField } = useContext(SortContext);
  const { view } = useContext(ViewContext);

  const releases = useMemo(() => {
    const results = [...mockReleases];

    // Sort releases based on the sort context.
    results.sort(sortFunctions[sortField]);
    if (!asc) results.reverse();

    return results;
  }, [asc, sortField]);

  return (
    <div className={`${view}Releases`}>
      {releases.map((rls) => {
        return <Release key={rls.id} {...rls} />;
      })}
    </div>
  );
};

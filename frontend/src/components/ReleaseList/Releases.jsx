import React, { useContext, useMemo } from 'react';
import { SortContext, ViewContext } from 'contexts';

import { Release } from 'components/Release';
import { mockReleases } from 'mockData';

// Functions to sort the release by, keyed on the sort type ID.
const sortFunctions = {
  random: () => Math.random() - 0.5,
  recentlyAdded: (one, two) => two.addedOn - one.addedOn,
  ritle: (one, two) => (one.title.toLowerCase() < two.title.toLowerCase() ? -1 : 1),
  year: (one, two) => one.year - two.year,
};

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

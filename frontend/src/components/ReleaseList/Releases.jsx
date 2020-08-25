import React, { useContext, useMemo } from 'react';
import { SortContext, ViewContext } from 'components/Contexts';

import { Release } from './Release';
import { mockReleases } from 'mockData';

// Functions to sort the release by, keyed on the sort type ID.
const sortFunctions = {
  1: (one, two) => two.addedOn - one.addedOn,
  2: (one, two) => (one.title.toLowerCase() < two.title.toLowerCase() ? -1 : 1),
  3: (one, two) => one.year - two.year,
  4: () => Math.random() - 0.5,
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

import React, { useContext } from 'react';
import { ReleasesContext, ViewContext } from 'contexts';

import { NoResults } from 'components/common/NoResults';
import { Release } from 'components/Release';

export const Releases = () => {
  const { view } = useContext(ViewContext);
  const { releases } = useContext(ReleasesContext);

  if (releases.length === 0) {
    return <NoResults />;
  }

  return (
    <div className={`${view}Releases`}>
      {releases.map((rls) => {
        return <Release key={rls.id} {...rls} />;
      })}
    </div>
  );
};

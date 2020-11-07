import * as React from 'react';

import { ScrolledReleases } from 'src/components/Releases';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { useHistory } from 'react-router-dom';
import { fetchRecentlyAdded } from 'src/lib';

export const RecentlyAdded: React.FC = () => {
  const { status, data } = fetchRecentlyAdded();
  const history = useHistory();

  const releases = data && status === 'success' ? data.releases.results : [];

  const toRecentlyAdded = React.useCallback(() => {
    // TODO: change these string keys to an enum.
    localStorage.setItem('release-view-options--sort', JSON.stringify('RECENTLY_ADDED'));
    localStorage.setItem('release-view-options--asc', JSON.stringify(false));
    history.push('/releases');
  }, [history]);

  return (
    <div className="mt-8">
      <SectionHeader className="mx-8 my-8 cursor-pointer" onClick={toRecentlyAdded}>
        Recently Added
      </SectionHeader>
      <ScrolledReleases
        className="rpr--home-recently-added px-8 py-4 overflow-x-auto"
        releases={releases}
      />
    </div>
  );
};

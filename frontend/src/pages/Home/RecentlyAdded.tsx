import * as React from 'react';

import { Link } from 'src/components/common/Link';
import { ScrolledReleases } from 'src/components/Releases';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { fetchRecentlyAdded } from 'src/lib';
import { useHistory } from 'react-router-dom';

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
    <div>
      <Link onClick={toRecentlyAdded} href="/releases">
        <SectionHeader className="mx-8 mt-4 mb-8 cursor-pointer">
          Recently Added <span className="text-primary text-2xl">(View All)</span>
        </SectionHeader>
      </Link>
      <ScrolledReleases
        className="rpr--home-recently-added px-8 py-4 overflow-x-auto"
        releases={releases}
      />
    </div>
  );
};

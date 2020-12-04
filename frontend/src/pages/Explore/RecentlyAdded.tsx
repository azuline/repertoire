import * as React from 'react';
import { useHistory } from 'react-router-dom';
import { Link, ScrolledReleases, SectionHeader } from 'src/components';
import { useFetchRecentlyAdded } from 'src/lib';

export const RecentlyAdded: React.FC = () => {
  const { data } = useFetchRecentlyAdded();
  const history = useHistory();

  const releases = data?.releases?.results || [];

  const toRecentlyAdded = React.useCallback(() => {
    // TODO: change these string keys to an enum.
    localStorage.setItem('release-view-options--sort', JSON.stringify('RECENTLY_ADDED'));
    localStorage.setItem('release-view-options--asc', JSON.stringify(false));
    history.push('/releases');
  }, [history]);

  return (
    <div>
      <Link href="/releases" onClick={toRecentlyAdded}>
        <SectionHeader className="mt-4 mb-8 cursor-pointer">
          Recently Added
          <span className="text-xl hover:text-primary-400 text-primary-500"> (View All)</span>
        </SectionHeader>
      </Link>
      <ScrolledReleases className="overflow-x-auto recently-added" releases={releases} />
    </div>
  );
};

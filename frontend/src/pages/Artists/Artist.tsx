import * as React from 'react';
import { Icon } from 'src/components/common/Icon';
import { SectionHeader } from 'src/components/common/SectionHeader';

import { useToasts } from 'react-toast-notifications';
import { fetchArtist } from 'src/lib';
import { ArtistReleases } from './Releases';
import { useHistory } from 'react-router-dom';

export const Artist: React.FC<{ active: number }> = ({ active }) => {
  const { addToast } = useToasts();
  const history = useHistory();

  const { status, data } = fetchArtist(active);

  React.useEffect(() => {
    if (status === 'loading') addToast('Loading artist...', { appearance: 'info' });
  }, [active, status]);

  // prettier-ignore
  const artist = React.useMemo(
    () => (data && status === 'success' ? data.artist : null),
    [status, data],
  );

  const setInactive = React.useCallback(
    (e) => {
      e.preventDefault();
      history.push('/artists');
    },
    [history],
  );

  if (!artist) return null;

  return (
    <div className="pl-8 py-4 flex-1 overflow-x-hidden">
      <button className="flex items-center text-btn" onClick={setInactive}>
        <Icon className="w-5 -ml-3 mr-1" icon="chevron-left-small" />
        <div className="flex-shrink">Back</div>
      </button>
      <SectionHeader className="my-8">{artist.name}</SectionHeader>
      <ArtistReleases active={active} />
    </div>
  );
};

import * as React from 'react';

import { ArtistReleases } from './Releases';
import { Icon } from 'src/components/common/Icon';
import { Link } from 'src/components/common/Link';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { fetchArtist } from 'src/lib';

export const Artist: React.FC<{ active: number }> = ({ active }) => {
  const { status, data } = fetchArtist(active);

  // prettier-ignore
  const artist = React.useMemo(
    () => (data && status === 'success' ? data.artist : null),
    [status, data],
  );

  if (!artist) return null;

  return (
    <div className="px-8 py-4 flex-1 overflow-x-hidden">
      <Link href="/artists">
        <button className="-ml-2 flex items-center text-btn">
          <Icon className="w-5 -ml-1 mr-1" icon="chevron-left-small" />
          <div className="flex-shrink">Back</div>
        </button>
      </Link>
      <SectionHeader className="my-8">{artist.name}</SectionHeader>
      <ArtistReleases active={active} />
    </div>
  );
};

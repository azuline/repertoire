import * as React from 'react';
import { BackButton, Header, Link, SectionHeader } from 'src/components';
import { fetchArtist } from 'src/lib';

import { ArtistReleases } from './Releases';

export const Artist: React.FC<{ active: number }> = ({ active }) => {
  const { status, data } = fetchArtist(active);

  // prettier-ignore
  const artist = React.useMemo(
    () => (data && status === 'success' ? data.artist : null),
    [status, data],
  );

  if (!artist) return null;

  return (
    <div className="relative flex flex-col flex-1">
      <Header />
      <div className="overflow-y-auto">
        <div className="px-8 pb-8 mt-1">
          <div className="flex justify-start">
            <Link href="/artists">
              <BackButton />
            </Link>
          </div>
          <SectionHeader className="my-4">{artist.name}</SectionHeader>
          <ArtistReleases active={active} />
        </div>
      </div>
    </div>
  );
};

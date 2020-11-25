import * as React from 'react';

import { BackButton, Header, Link, SectionHeader } from 'src/components';
import { ArtistReleases } from './Releases';
import { fetchArtist } from 'src/lib';

export const Artist: React.FC<{ active: number }> = ({ active }) => {
  const fetchVariables = React.useMemo(() => ({ id: active }), [active]);
  const { status, data } = fetchArtist(fetchVariables);

  // prettier-ignore
  const artist = React.useMemo(
    () => (data && status === 'success' ? data.artist : null),
    [status, data],
  );

  if (!artist) return null;

  return (
    <div className="relative flex-1 flex flex-col">
      <Header />
      <div className="overflow-y-auto">
        <div className="px-8 pb-8 mt-1">
          <Link href="/artists">
            <BackButton />
          </Link>
          <SectionHeader className="my-4">{artist.name}</SectionHeader>
          <ArtistReleases active={active} />
        </div>
      </div>
    </div>
  );
};

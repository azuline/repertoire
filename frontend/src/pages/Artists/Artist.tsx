import * as React from 'react';
import { BackButton, Header, Link, SectionHeader } from 'src/components';
import { BackgroundContext } from 'src/contexts';
import { fetchArtist } from 'src/lib';

import { ArtistReleases } from './Releases';

export const Artist: React.FC<{ active: number }> = ({ active }) => {
  const { data } = fetchArtist(active);
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const artist = React.useMemo(() => data?.artist || null, [data]);

  React.useEffect(() => {
    if (!artist) return;

    setBackgroundImageId(artist.imageId);
    return (): void => setBackgroundImageId(null);
  }, [artist]);

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
          <SectionHeader className="mt-4 mb-8">{artist.name}</SectionHeader>
          <ArtistReleases active={active} />
        </div>
      </div>
    </div>
  );
};

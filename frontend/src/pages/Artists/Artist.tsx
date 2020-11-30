import * as React from 'react';
import { Header, SectionHeader } from 'src/components';
import { BackgroundContext } from 'src/contexts';
import { useFetchArtist } from 'src/lib';

import { ArtistReleases } from './Releases';

export const Artist: React.FC<{ active: number }> = ({ active }) => {
  const { data } = useFetchArtist(active);
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const artist = React.useMemo(() => data?.artist || null, [data]);

  React.useEffect(() => {
    if (!artist) return;

    setBackgroundImageId(artist.imageId);
    return (): void => setBackgroundImageId(null);
  }, [artist, setBackgroundImageId]);

  if (!artist) return null;

  return (
    <div className="flex flex-col w-full">
      <Header />
      <div className="px-8">
        <SectionHeader className="mt-4 mb-8">{artist.name}</SectionHeader>
        <ArtistReleases active={active} />
      </div>
    </div>
  );
};

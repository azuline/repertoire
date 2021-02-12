import * as React from 'react';

import { Header, SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useFetchArtist } from '~/lib';

import { ArtistReleases } from './Releases';

export const Artist: React.FC<{ active: number }> = ({ active }) => {
  const { data } = useFetchArtist(active);
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const artist = data?.artist || null;

  React.useEffect(() => {
    if (!artist) return;

    setBackgroundImageId(artist.imageId);
    return (): void => setBackgroundImageId(null);
  }, [artist, setBackgroundImageId]);

  if (!artist) return null;

  return (
    <div className="flex flex-col w-full">
      <Header />
      <SectionHeader className="mt-4 mb-8">{artist.name}</SectionHeader>
      <ArtistReleases active={active} />
    </div>
  );
};

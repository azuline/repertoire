import * as React from 'react';

import { Header, SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useFetchArtistQuery } from '~/graphql';
import { ErrorP } from '~/pages';

import { ArtistReleases } from './Releases';

type IComponent = React.FC<{ active: number }>;

export const Artist: IComponent = ({ active }) => {
  const { data, error } = useFetchArtistQuery({ variables: { id: active } });
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const artist = data?.artist || null;

  React.useEffect(() => {
    if (!artist) return;

    setBackgroundImageId(artist.imageId);
    return (): void => setBackgroundImageId(null);
  }, [artist, setBackgroundImageId]);

  if (error) {
    const errors = error.graphQLErrors.map(({ message }) => message);
    return <ErrorP errors={errors} title="Could not fetch label." />;
  }

  if (!artist) return null;

  return (
    <div className="flex flex-col w-full">
      <Header />
      <SectionHeader className="mt-4 mb-8">{artist.name}</SectionHeader>
      <ArtistReleases active={active} />
    </div>
  );
};

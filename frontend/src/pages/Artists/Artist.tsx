import 'twin.macro';

import * as React from 'react';

import { Header, SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useFetchArtistQuery } from '~/graphql';
import { ErrorPage } from '~/pages';

import { ArtistReleases } from './Releases';

type IArtist = React.FC<{ active: number }>;

export const Artist: IArtist = ({ active }) => {
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
    return <ErrorPage errors={errors} title="Could not fetch label." />;
  }

  if (!artist) return null;

  return (
    <div tw="flex flex-col w-full">
      <Header />
      <SectionHeader tw="mt-4 mb-8">{artist.name}</SectionHeader>
      <ArtistReleases active={active} />
    </div>
  );
};

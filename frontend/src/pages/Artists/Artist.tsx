import { gql } from '@apollo/client';
import * as React from 'react';

import { SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useArtistsFetchArtistQuery } from '~/graphql';
import { ErrorPage } from '~/pages';

import { ArtistReleases } from './Releases';

type IArtist = React.FC<{ active: number }>;

export const Artist: IArtist = ({ active }) => {
  const { data, error } = useArtistsFetchArtistQuery({ variables: { id: active } });
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const artist = data?.artist;

  React.useEffect(() => {
    if (!artist) {
      return;
    }

    setBackgroundImageId(artist.imageId);
    return (): void => setBackgroundImageId(null);
  }, [artist]);

  if (error) {
    const errors = error.graphQLErrors.map(({ message }) => message);
    return <ErrorPage errors={errors} title="Could not fetch playlist." />;
  }

  if (!artist) {
    return null;
  }

  return (
    <>
      <SectionHeader tw="mt-4 mb-8">{artist.name}</SectionHeader>
      <ArtistReleases active={active} />
    </>
  );
};

gql`
  query ArtistsFetchArtist($id: Int!) {
    artist(id: $id) {
      ...ArtistFields
    }
  }
`;

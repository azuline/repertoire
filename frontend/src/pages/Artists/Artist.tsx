import { gql } from '@apollo/client';
import * as React from 'react';

import { Header, SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useArtistsFetchArtistQuery } from '~/graphql';
import { AuthenticatedError } from '~/pages';

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
    return <AuthenticatedError errors={errors} title="Could not fetch playlist." />;
  }

  if (!artist) {
    return null;
  }

  return (
    <div tw="flex flex-col w-full">
      <Header />
      <SectionHeader tw="mt-4 mb-8">{artist.name}</SectionHeader>
      <ArtistReleases active={active} />
    </div>
  );
};

/* eslint-disable */
gql`
  query ArtistsFetchArtist($id: Int!) {
    artist(id: $id) {
      ...ArtistFields
    }
  }
`;

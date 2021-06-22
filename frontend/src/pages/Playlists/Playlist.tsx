import { gql } from '@apollo/client';
import * as React from 'react';

import { SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { usePlaylistsFetchPlaylistQuery } from '~/graphql';
import { ErrorPage } from '~/pages';

import { PlaylistTracks } from './Tracks';

type IPlaylist = React.FC<{ active: number }>;

export const Playlist: IPlaylist = ({ active }) => {
  const { data, error } = usePlaylistsFetchPlaylistQuery({ variables: { id: active } });
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const playlist = data?.playlist;

  React.useEffect(() => {
    if (!playlist) {
      return;
    }

    setBackgroundImageId(playlist.imageId);
    return (): void => setBackgroundImageId(null);
  }, [playlist]);

  if (error) {
    const errors = error.graphQLErrors.map(({ message }) => message);
    return <ErrorPage errors={errors} title="Could not fetch playlist." />;
  }

  if (!playlist) {
    return null;
  }

  return (
    <div tw="flex flex-col w-full">
      <SectionHeader tw="mt-4 mb-16">{playlist.name}</SectionHeader>
      <PlaylistTracks active={active} />
    </div>
  );
};

gql`
  query PlaylistsFetchPlaylist($id: Int!) {
    playlist(id: $id) {
      ...PlaylistFields
    }
  }
`;

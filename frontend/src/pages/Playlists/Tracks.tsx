import { gql } from '@apollo/client';
import * as React from 'react';

import { Tracklist } from '~/components';
import { usePlaylistsFetchTracksQuery } from '~/graphql';
import { ErrorPage } from '~/pages/Error';
import { filterNulls } from '~/util';

type IPlaylistTracks = React.FC<{ active: number }>;

export const PlaylistTracks: IPlaylistTracks = ({ active }) => {
  const { data, error } = usePlaylistsFetchTracksQuery({ variables: { id: active } });

  if (error) {
    const errors = error.graphQLErrors.map(({ message }) => message);
    return <ErrorPage errors={errors} title="Could not fetch release." />;
  }

  const tracks = filterNulls(data?.playlist.entries.map((e) => e.track) ?? []);

  return <Tracklist showCovers tracks={tracks} />;
};

/* eslint-disable */
gql`
  query PlaylistsFetchTracks($id: Int!) {
    playlist(id: $id) {
      id
      entries {
        id
        track {
          ...TrackFields
        }
      }
    }
  }
`;

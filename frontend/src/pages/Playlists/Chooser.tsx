import { gql } from '@apollo/client';
import * as React from 'react';

import { Chooser, IToggleStarFactory } from '~/components';
import {
  IPlaylist,
  usePlaylistChooserFetchPlaylistsQuery,
  usePlaylistChooserUpdatePlaylistStarredMutation,
} from '~/graphql';

type IPlaylistChooser = React.FC<{
  active: number | null;
  className?: string;
}>;

export const PlaylistChooser: IPlaylistChooser = ({ active, className }) => {
  const { data, error, loading } = usePlaylistChooserFetchPlaylistsQuery();
  const [mutatePlaylist] = usePlaylistChooserUpdatePlaylistStarredMutation();

  const toggleStarFactory: IToggleStarFactory = ({ id, starred, type }) => {
    if (type === 'SYSTEM') return;

    return async (): Promise<void> => {
      await mutatePlaylist({ variables: { id, starred: !starred } });
    };
  };

  if (!data || !data.playlists || error || loading) return null;

  return (
    <Chooser
      active={active}
      className={className}
      results={data.playlists.results as IPlaylist[]}
      toggleStarFactory={toggleStarFactory}
      urlFactory={urlFactory}
    />
  );
};

const urlFactory = (id: number): string => `/playlists/${id}`;

/* eslint-disable */
gql`
  query PlaylistChooserFetchPlaylists($types: [PlaylistType]) {
    playlists(types: $types) {
      results {
        ...PlaylistFields
      }
    }
  }

  mutation PlaylistChooserUpdatePlaylistStarred($id: Int!, $starred: Boolean) {
    updatePlaylist(id: $id, starred: $starred) {
      id
      starred
    }
  }
`;

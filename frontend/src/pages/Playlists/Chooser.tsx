import { gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Chooser, StarrableChooserRow } from '~/components';
import {
  IPlaylistFieldsFragment,
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
  const { addToast } = useToasts();

  const toggleStar = async (playlist: IPlaylistFieldsFragment): Promise<void> => {
    if (playlist.type === 'SYSTEM') {
      addToast('Cannot unstar system playlists.', { appearance: 'error' });
      return;
    }

    await mutatePlaylist({
      variables: { id: playlist.id, starred: playlist.starred !== true },
    });
  };

  if (!data || error || loading) {
    return null;
  }

  // If the playlist has a user, prefix the playlist name with the user's nickname.
  const playlists = data.playlists.results.map((p) =>
    p.user === null ? p : { ...p, name: `${p.user.nickname}'s ${p.name}` },
  );

  const renderElement = (index: number): React.ReactNode => {
    const element = playlists[index];

    return (
      <StarrableChooserRow
        element={element}
        isActive={element.id === active}
        url={`/playlists/${element.id}`}
        onToggle={(): Promise<void> => toggleStar(element)}
      />
    );
  };

  return (
    <Chooser
      active={active}
      className={className}
      renderElement={renderElement}
      results={playlists}
    />
  );
};

/* eslint-disable */
gql`
  query PlaylistChooserFetchPlaylists($types: [PlaylistType!]) {
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

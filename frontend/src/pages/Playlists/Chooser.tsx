import { gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Chooser, StarrableChooserRow } from '~/components';
import {
  IPlaylistFieldsFragment,
  useFetchPlaylistsChooserQuery,
  useStarPlaylistChooserMutation,
  useUnstarPlaylistChooserMutation,
} from '~/graphql';

type IPlaylistChooser = React.FC<{
  active: number | null;
  className?: string;
}>;

export const PlaylistChooser: IPlaylistChooser = ({ active, className }) => {
  const { data, error, loading } = useFetchPlaylistsChooserQuery();
  const [starPlaylist] = useStarPlaylistChooserMutation();
  const [unstarPlaylist] = useUnstarPlaylistChooserMutation();
  const { addToast } = useToasts();

  const toggleStar = async (playlist: IPlaylistFieldsFragment): Promise<void> => {
    if (playlist.type === 'SYSTEM') {
      addToast('Cannot unstar system playlists.', { appearance: 'error' });
      return;
    }

    if (playlist.starred) {
      await unstarPlaylist({ variables: { id: playlist.id } });
    } else {
      await starPlaylist({ variables: { id: playlist.id } });
    }
  };

  if (!data || error || loading) {
    return null;
  }

  // If the playlist has a user, prefix the playlist name with the user's nickname.
  // TODO(now): Sort properly.
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
  query FetchPlaylistsChooser($types: [PlaylistType!]) {
    playlists(types: $types) {
      results {
        ...PlaylistFields
      }
    }
  }

  mutation StarPlaylistChooser($id: Int!) {
    starPlaylist(id: $id) {
      id
      starred
    }
  }

  mutation UnstarPlaylistChooser($id: Int!) {
    unstarPlaylist(id: $id) {
      id
      starred
    }
  }
`;

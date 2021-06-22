import { gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import tw from 'twin.macro';

import { ArtistListWithRoles, Icon, Image } from '~/components';
import { ListItem } from '~/components/common';
import {
  ITrackFieldsFragment,
  useFavoritePlaylistsIdQuery,
  usePlaylistsFavoriteTrackMutation,
  usePlaylistsUnfavoriteTrackMutation,
} from '~/graphql';
import { filterNulls, secondsToLength } from '~/util';

type ITrackComponent = React.FC<{
  track: ITrackFieldsFragment;
  trackNumber: number;
  index: number;
  onClick?: (arg0: number) => void;
  active?: boolean;
  showCover?: boolean;
}>;

export const Track: ITrackComponent = ({
  track,
  trackNumber,
  index,
  onClick,
  active = false,
  showCover = false,
}) => {
  const { addToast } = useToasts();

  const { data } = useFavoritePlaylistsIdQuery();
  const [favoriteTrack] = usePlaylistsFavoriteTrackMutation();
  const [unfavoriteTrack] = usePlaylistsUnfavoriteTrackMutation();

  const toggleFavorite = async (): Promise<void> => {
    if (data === undefined) {
      addToast('Failed to fetch favorites.', { appearance: 'error' });
      return;
    }

    const toggleFunc = track.inFavorites ? unfavoriteTrack : favoriteTrack;
    await toggleFunc({
      variables: {
        playlistId: data.user.favoritesPlaylistId,
        trackId: track.id,
      },
    });
  };

  return (
    <ListItem
      css={[
        tw`flex relative items-center`,
        tw`py-2 pr-3 -mx-3 width[calc(100% + 1.5rem)]`,
        active && tw`font-bold`,
      ]}
      onClick={(): void => onClick && onClick(index)}
    >
      <div
        css={[
          tw`flex-none flex items-center absolute top-0 left-0`,
          tw`px-3 cursor-pointer h-full`,
          track.inFavorites
            ? tw`text-primary-500 fill-current hover:(text-gray-500 stroke-current)`
            : tw`text-gray-500 stroke-current hover:(text-primary-400 fill-current)`,
        ]}
        title={`${track.inFavorites ? 'Unfavorite' : 'Favorite'} this track!`}
        onClick={toggleFavorite}
      >
        <Icon icon="star-small" tw="w-6 md:w-5" />
      </div>
      <div tw="ml-12 md:ml-11 w-full flex items-center min-w-0">
        {showCover && (
          <Image imageId={track.release.imageId} tw="rounded w-8 h-8 mr-3" />
        )}
        <div tw="flex-1">
          <div tw="flex items-center w-full min-w-0">
            <div tw="flex items-center flex-1 min-w-0">
              <div title={track.title} tw="flex-none mr-2 truncate w-full md:w-1/3">
                <span>{trackNumber}. </span>
                {track.title}
              </div>
              <ArtistListWithRoles
                artists={filterNulls(track.artists)}
                tw="flex-1 hidden w-2/3 truncate text-foreground-500 md:block"
              />
            </div>
            <div tw="flex-none w-14 text-right text-foreground-500">
              {secondsToLength(track.duration)}
            </div>
          </div>
          <ArtistListWithRoles
            artists={filterNulls(track.artists)}
            tw="mt-1 truncate text-foreground-500 md:hidden"
          />
        </div>
      </div>
    </ListItem>
  );
};

gql`
  query FavoritePlaylistsId {
    user {
      id
      favoritesPlaylistId
    }
  }

  mutation PlaylistsFavoriteTrack($playlistId: Int!, $trackId: Int!) {
    createPlaylistEntry(playlistId: $playlistId, trackId: $trackId) {
      id
      playlist {
        id
        numTracks
        entries {
          id
        }
      }
      track {
        id
        inFavorites
      }
    }
  }

  mutation PlaylistsUnfavoriteTrack($trackId: Int!) {
    delPlaylistEntries(playlistId: 1, trackId: $trackId) {
      playlist {
        id
        numTracks
        entries {
          id
        }
      }
      track {
        id
        inFavorites
      }
    }
  }
`;

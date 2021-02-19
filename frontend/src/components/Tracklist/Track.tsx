import { gql } from '@apollo/client';
import * as React from 'react';
import tw from 'twin.macro';

import { Icon } from '~/components/common';
import { TrackArtistList } from '~/components/Lists';
import {
  ITrack,
  usePlaylistsFavoriteTrackMutation,
  usePlaylistsUnfavoriteTrackMutation,
} from '~/graphql';
import { filterNulls, secondsToLength } from '~/util';

type ITrackComponent = React.FC<{
  track: ITrack;
  trackNumber: number;
  index: number;
  onClick?: (arg0: number) => void;
  active?: boolean;
}>;

export const Track: ITrackComponent = ({ track, trackNumber, index, onClick, active = false }) => {
  const [favoriteTrack] = usePlaylistsFavoriteTrackMutation();
  const [unfavoriteTrack] = usePlaylistsUnfavoriteTrackMutation();

  const toggleFavorite = async (): Promise<void> => {
    const toggleFunc = track.favorited ? unfavoriteTrack : favoriteTrack;
    await toggleFunc({ variables: { trackId: track.id } });
  };

  return (
    <div
      css={[
        tw`flex relative items-center py-1.5 pr-3 -mx-3 rounded width[calc(100% + 1.5rem)]`,
        active && tw`font-bold`,
        onClick && tw`cursor-pointer hover-bg`,
      ]}
    >
      <div
        css={[
          tw`flex-none flex items-center absolute top-0 left-0 px-3 cursor-pointer h-full`,
          track.favorited
            ? tw`text-primary-500 fill-current hover:(text-gray-500 stroke-current)`
            : tw`text-gray-500 stroke-current hover:(text-primary-400 fill-current)`,
        ]}
        title={`${track.favorited ? 'Unfavorite' : 'Favorite'} this track!`}
        onClick={toggleFavorite}
      >
        <Icon icon="star-small" tw="w-6 md:w-5" />
      </div>
      <div tw="ml-12 md:ml-11 w-full" onClick={(): void => onClick && onClick(index)}>
        <div tw="flex items-center">
          <div title={track.title} tw="flex-1 mr-2 truncate md:flex-none w-1/3">
            <span>{trackNumber}. </span>
            {track.title}
          </div>
          <TrackArtistList
            artists={filterNulls(track.artists)}
            tw="flex-1 hidden truncate text-foreground-400 md:block"
          />
          <div tw="flex-none ml-2 text-foreground-400">{secondsToLength(track.duration)}</div>
        </div>
        <TrackArtistList
          artists={filterNulls(track.artists)}
          tw="mt-1 truncate text-foreground-400 md:hidden"
        />
      </div>
    </div>
  );
};

/* eslint-disable */
gql`
  mutation PlaylistsFavoriteTrack($trackId: Int!) {
    createPlaylistEntry(playlistId: 1, trackId: $trackId) {
      id
      playlist {
        numTracks
        entries {
          id
        }
      }
      track {
        id
        favorited
      }
    }
  }

  mutation PlaylistsUnfavoriteTrack($trackId: Int!) {
    delPlaylistEntries(playlistId: 1, trackId: $trackId) {
      playlist {
        numTracks
        entries {
          id
        }
      }
      track {
        id
        favorited
      }
    }
  }
`;

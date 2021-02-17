import * as React from 'react';
import tw from 'twin.macro';

import { Icon } from '~/components/common';
import { TrackArtistList } from '~/components/Lists';
import { ITrack } from '~/graphql';
import { filterNulls, secondsToLength } from '~/util';

type ITrackComponent = React.FC<{
  track: ITrack;
  trackNumber: number;
  index: number;
  onClick?: (arg0: number) => void;
  active?: boolean;
}>;

export const Track: ITrackComponent = ({ track, trackNumber, index, onClick, active = false }) => {
  const trackOnClick = (): void => onClick && onClick(index);

  return (
    <div
      css={[
        tw`py-1.5 px-3 -mx-3 rounded`,
        active && tw`font-bold`,
        onClick && tw`cursor-pointer hover-bg`,
      ]}
      style={{ width: 'calc(100% + 1.5rem)' }}
      onClick={trackOnClick}
    >
      <div tw="flex items-center">
        <Icon icon="play-medium" tw="flex-none w-5 mr-3 cursor-pointer text-primary-500" />
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
        tw="mt-1 ml-8 truncate text-foreground-400 md:hidden"
      />
    </div>
  );
};

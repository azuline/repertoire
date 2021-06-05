import * as React from 'react';

import { ArtistListWithRoles, Image, Link } from '~/components';
import { ITrackFieldsFragment } from '~/graphql';
import { filterNulls } from '~/util';

import { RedirectToNowPlaying } from './RedirectToNowPlaying';

type ITrackInfo = React.FC<{
  curTrack: Pick<ITrackFieldsFragment, 'title' | 'artists' | 'release'>;
}>;

export const TrackInfo: ITrackInfo = ({ curTrack }) => {
  return (
    <div tw="flex flex-1 ml-2 lg:ml-6 mr-2 truncate">
      <Link
        href={`/releases/${curTrack.release.id}`}
        tw="flex-none hidden w-11 sm:block"
      >
        <div tw="relative w-full h-0 pb-full">
          <Image
            thumbnail
            imageId={curTrack.release.imageId}
            tw="absolute object-cover rounded full"
          />
        </div>
      </Link>
      <RedirectToNowPlaying tw="flex flex-col flex-1 mx-1 text-center truncate sm:mx-4">
        <div tw="font-bold truncate">{curTrack.title}</div>
        <ArtistListWithRoles artists={filterNulls(curTrack.artists)} tw="truncate" />
      </RedirectToNowPlaying>
    </div>
  );
};

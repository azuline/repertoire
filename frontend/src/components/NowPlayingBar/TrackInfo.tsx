import * as React from 'react';
import { Image, Link, TrackArtistList } from '~/components';
import { TrackT } from '~/types';

import { RedirectToNowPlaying } from './RedirectToNowPlaying';

export const TrackInfo: React.FC<{ curTrack: TrackT }> = ({ curTrack }) => (
  <div className="flex flex-1 mr-2 truncate sm:mr-0">
    <Link className="flex-none hidden w-11 sm:block" href={`/releases/${curTrack.release.id}`}>
      <div className="relative w-full h-0 pb-full">
        <Image
          thumbnail
          className="absolute object-cover rounded full"
          imageId={curTrack.release.imageId}
        />
      </div>
    </Link>
    <RedirectToNowPlaying className="flex flex-col flex-1 mx-1 text-center truncate sm:mx-4">
      <div className="font-bold truncate">{curTrack.title}</div>
      <TrackArtistList artists={curTrack.artists} className="truncate" />
    </RedirectToNowPlaying>
  </div>
);

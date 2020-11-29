import * as React from 'react';
import { Image, Link, TrackArtistList } from 'src/components';
import { TrackT } from 'src/types';

import { RedirectToNowPlaying } from './RedirectToNowPlaying';

export const TrackInfo: React.FC<{ curTrack: TrackT }> = ({ curTrack }) => (
  <div className="flex flex-1 truncate">
    <Link href={`/releases/${curTrack.release.id}`} className="flex-none hidden sm:block w-11">
      <div className="relative w-full h-0 pb-full">
        <Image
          className="absolute object-cover rounded full"
          imageId={curTrack.release.imageId}
          thumbnail
        />
      </div>
    </Link>
    <RedirectToNowPlaying className="flex flex-col flex-1 mx-1 text-center truncate sm:mx-4">
      <div className="font-bold truncate">{curTrack.title}</div>
      <TrackArtistList className="truncate" artists={curTrack.artists} />
    </RedirectToNowPlaying>
  </div>
);

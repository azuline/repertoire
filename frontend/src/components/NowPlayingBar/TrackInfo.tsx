import * as React from 'react';
import { ArtistList, CoverArt } from 'src/components';
import { ReleaseT, TrackArtistT, TrackT } from 'src/types';
import { arrangeArtists } from 'src/util';

export const TrackInfo: React.FC<{ curTrack: TrackT | null }> = ({ curTrack }) => (
  <>
    <div className="flex-none w-11">
      <div className="relative w-full h-0 pb-full">
        {curTrack && (
          <CoverArt
            className="absolute object-cover rounded full"
            release={curTrack.release as ReleaseT}
            thumbnail
          />
        )}
      </div>
    </div>
    <div className="flex flex-col flex-1 mx-4 text-center truncate">
      <div className="font-bold truncate">{curTrack && curTrack.title}</div>
      {curTrack && (
        <ArtistList
          className="truncate"
          elements={arrangeArtists(curTrack.artists as TrackArtistT[])}
        />
      )}
    </div>
  </>
);

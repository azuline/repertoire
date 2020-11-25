import * as React from 'react';
import { ArtistList, CoverArt } from 'src/components';
import { ReleaseT, TrackArtistT, TrackT } from 'src/types';
import { arrangeArtists } from 'src/util';

export const TrackInfo: React.FC<{ curTrack: TrackT | null }> = ({ curTrack }) => (
  <>
    <div className="flex-none w-11">
      <div className="w-full h-0 pb-full relative">
        {curTrack && (
          <CoverArt
            className="full absolute object-cover rounded"
            release={curTrack.release as ReleaseT}
            thumbnail
          />
        )}
      </div>
    </div>
    <div className="truncate mx-4 flex-1 flex flex-col text-center">
      <div className="truncate font-bold">{curTrack && curTrack.title}</div>
      {curTrack && (
        <ArtistList
          className="truncate"
          elements={arrangeArtists(curTrack.artists as TrackArtistT[])}
        />
      )}
    </div>
  </>
);

import * as React from 'react';
import { CoverArt, Icon, ArtistList } from 'src/components';
import { TrackArtistT, ReleaseT } from 'src/types';
import { PlayQueueContext } from 'src/contexts';
import { useAudio } from 'src/hooks';
import { arrangeArtists, secondsToLength } from 'src/util';

export const Footer: React.FC = () => {
  const { playQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);
  const { isPlaying, setIsPlaying, curTime, seek } = useAudio();

  // prettier-ignore
  const curTrack = React.useMemo(
    () => (curIndex !== null ? playQueue[curIndex] : null),
    [playQueue, curIndex],
  );

  console.log(curTrack);

  const togglePlay = React.useCallback(() => setIsPlaying((p: boolean) => !p), [setIsPlaying]);
  const fastForward = React.useCallback(
    () => setCurIndex((idx) => (idx !== null && idx !== playQueue.length - 1 ? idx + 1 : null)),
    [setIsPlaying],
  );
  const rewind = React.useCallback(() => {
    if (isPlaying && curTime > 10) {
      seek(0);
    } else {
      setCurIndex((idx) => (idx !== null && idx !== 0 ? idx - 1 : null));
    }
  }, [curTime, setIsPlaying]);

  return (
    <div className="relative z-30 flex-none w-full h-16 bg-background-alt2 border-t-2 border-gray-300 dark:border-gray-700">
      <div className="full flex items-center">
        <div className="flex-none ml-8 md:ml-0 md:w-56 flex justify-center items-center text-primary">
          <Icon
            className="w-9 mr-1 cursor-pointer hover:text-primary-alt3"
            icon="rewind-small"
            onClick={rewind}
          />
          <Icon
            className="w-9 mr-1 cursor-pointer hover:text-primary-alt3"
            icon={isPlaying ? 'pause-small' : 'play-small'}
            onClick={togglePlay}
          />
          <Icon
            className="w-9 cursor-pointer hover:text-primary-alt3"
            icon="fast-forward-small"
            onClick={fastForward}
          />
        </div>
        <div className="flex-none w-12 ml-8">
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
        <div className="mr-8 flex-none hidden sm:block">
          {curTrack ? (
            <>
              {secondsToLength(curTime)}
              <span> / </span>
              {secondsToLength(curTrack.duration)}
            </>
          ) : (
            <span>-:-- / -:--</span>
          )}
        </div>
      </div>
    </div>
  );
};

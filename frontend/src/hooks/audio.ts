import * as React from 'react';
import { PlayQueueContext } from 'src/contexts';
import { SetBoolean, SetNumber } from 'src/types';

// TODO: Preload next track?
// TODO: Make sure that we aren't leaking memory from all these audio
// objects... they better be garbage collected properly.

export type AudioPlayT = {
  isPlaying: boolean;
  setIsPlaying: SetBoolean;
  curTime: number;
  seek: SetNumber;
};

export const useAudio = (): AudioPlayT => {
  const { playQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);
  const [audio, setAudio] = React.useState<HTMLAudioElement | null>(null);
  const [isPlaying, setIsPlaying] = React.useState<boolean>(false);
  const [curTime, setCurTime] = React.useState<number>(0);

  const onTrackEnd = React.useCallback(
    () => setCurIndex((idx) => (idx !== null && idx !== playQueue.length - 1 ? idx + 1 : null)),
    [playQueue, setCurIndex],
  );

  // prettier-ignore
  const curTrack = React.useMemo(
    () => (curIndex !== null ? playQueue[curIndex] : null),
    [playQueue, curIndex],
  );

  // Whenever we load a new track, load the audio file and begin playing it.
  React.useEffect(() => {
    if (audio) audio.pause();

    if (!curTrack) return;

    const newAudio = new Audio(`/files/tracks/${curTrack.id}`);
    setAudio(newAudio);
    setIsPlaying(true);

    newAudio.addEventListener('ended', onTrackEnd);
    return (): void => newAudio.removeEventListener('ended', onTrackEnd);
  }, [curTrack]);

  // Sync the isPlaying variable with the audio.
  // Return a timer to sync curTime with the track progress.
  React.useEffect(() => {
    if (!audio) {
      setIsPlaying(false);
      return;
    }

    if (isPlaying) {
      if (audio.ended) audio.fastSeek(0);
      if (audio.paused) audio.play();

      const timer = setInterval(() => setCurTime(Math.floor(audio.currentTime)), 1);
      return (): void => clearInterval(timer);
    }
    if (!audio.ended) {
      audio.pause();
    }
  }, [isPlaying, audio]);

  const seek = React.useCallback((seconds) => audio && audio.fastSeek(seconds), [audio]);

  return { isPlaying, setIsPlaying, curTime, seek };
};

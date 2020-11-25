import * as React from 'react';
import { PlayQueueContext } from 'src/contexts';

// TODO: Preload next track?
// TODO: Make sure that we aren't leaking memory from all these audio
// objects... they better be garbage collected properly.

type AudioPlayType = {
  isPlaying: boolean;
  setIsPlaying: (arg0: boolean | ((arg0: boolean) => boolean)) => void;
  curTime: number;
  seek: (arg0: number) => void;
};

export const useAudio = (): AudioPlayType => {
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
    return () => newAudio.removeEventListener('ended', onTrackEnd);
  }, [curTrack]);

  // Sync the isPlaying variable with the audio.
  // Return a timer to sync curTime with the track progress.
  React.useEffect(() => {
    if (!audio) return;

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

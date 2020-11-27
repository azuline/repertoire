import * as React from 'react';
import { PlayQueueContext, VolumeContext } from 'src/contexts';
import { SetValue } from 'src/types';

// TODO: Preload next track?
// TODO: Make sure that we aren't leaking memory from all these audio
// objects... they better be garbage collected properly.

export type AudioT = {
  isPlaying: boolean;
  setIsPlaying: SetValue<boolean>;
  curTime: number;
  seek: SetValue<number>;
};

/**
 * A hook to manage audio playback. This hook will play the current track in the queue if
 * one exists. Upon track completion, the hook will auto-play the next track in the queue.
 *
 * This hook must exist below a ``PlayQueueProvider``.
 *
 * @returns An object with four keys:
 *
 * - ``isPlaying`` - Whether audio is playing.
 * - ``setIsPlaying`` - Start/stop the audio. Does nothing if the play queue is empty.
 * - ``curTime`` - The current time in the track.
 * - ``seek`` - A function to jump to a certain track time in the audio.
 */
export const useAudio = (): AudioT => {
  const { playQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);
  const { volume, isMuted } = React.useContext(VolumeContext);
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
    newAudio.volume = isMuted ? 0 : volume / 100;
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

  // Sync the currently playing track with the volume.
  React.useEffect(() => {
    if (audio) audio.volume = isMuted ? 0 : volume / 100;
  }, [isMuted, volume]);

  const seek = React.useCallback((seconds) => audio && audio.fastSeek(seconds), [audio]);

  return { isPlaying, setIsPlaying, curTime, seek };
};

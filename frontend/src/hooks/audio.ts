import * as React from 'react';
import { PlayQueueContext, VolumeContext } from 'src/contexts';
import { SetValue } from 'src/types';
import { sleep } from 'src/util';

// TODO: Make sure that we aren't leaking memory from all these audio
// objects... they better be garbage collected properly.

type NextAudio = {
  trackId: number;
  audio: HTMLAudioElement;
};

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
  const [nextAudio, setNextAudio] = React.useState<NextAudio | null>(null);

  const [isPlaying, setIsPlaying] = React.useState<boolean>(false);
  const [curTime, setCurTime] = React.useState<number>(0);

  // prettier-ignore
  const curTrack = React.useMemo(
    () => (curIndex !== null ? playQueue[curIndex] : null),
    [playQueue, curIndex],
  );

  // Whenever we switch to a new track, load the corresponding audio file and begin playing it.
  // For gapless playback, we preload the next track shortly after playing this track.
  React.useEffect(() => {
    if (audio) audio.pause();

    if (!curTrack) {
      setIsPlaying(false);
      return;
    }

    const newAudio =
      nextAudio && nextAudio.trackId === curTrack.id
        ? nextAudio.audio
        : new Audio(`/files/tracks/${curTrack.id}`);

    newAudio.volume = isMuted ? 0 : volume / 100;
    setAudio(newAudio);
    setIsPlaying(true);

    // Set the next audio track for preloading.
    if (curIndex && curIndex !== playQueue.length - 1) {
      const nextTrack = playQueue[curIndex + 1];
      const nextTrackAudio = new Audio(`/files/tracks/${nextTrack.id}`);
      setNextAudio({ trackId: nextTrack.id, audio: nextTrackAudio });
    }

    const onTrackEnd = (): void => {
      if (curIndex === playQueue.length - 1) {
        setCurIndex(null);
        setAudio(null);
      } else {
        setCurIndex((idx) => (idx as number) + 1);
      }

      setIsPlaying(false);
    };

    newAudio.addEventListener('ended', onTrackEnd);
    return (): void => newAudio.removeEventListener('ended', onTrackEnd);
  }, [curTrack]);

  React.useEffect(() => {
    if (!nextAudio) return;

    (async (): Promise<void> => {
      // Sleep for 8 seconds to not interfere with current track loading.
      // Do we even need to do this? Will browsers prioritize the playing track? Who knows!
      await sleep(8000);
      if (nextAudio.audio.paused) {
        nextAudio.audio.load();
      }
    })();
  }, [nextAudio]);

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

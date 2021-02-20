import * as React from 'react';

import { PlayQueueContext, VolumeContext } from '~/contexts';
import { ISetValue } from '~/types';

export type IAudio = {
  isPlaying: boolean;
  setIsPlaying: ISetValue<boolean>;
  curTime: number;
  seek: (arg0: number) => void;
};

type IAudioTracks = { curr?: IAudioTrack; next?: IAudioTrack };
type IAudioTrack = { trackId: number; audio: HTMLAudioElement };

/**
 * A hook to manage audio playback. This hook will play the current track in the queue
 * if one exists. Upon track completion, the hook will auto-play the next track in the
 * queue.
 *
 * This hook must be inside a ``PlayQueueProvider``.
 *
 * @returns An object with four keys:
 *
 * - ``isPlaying`` - Whether audio is playing.
 * - ``setIsPlaying`` - Start/stop the audio. Does nothing if the play queue is empty.
 * - ``curTime`` - The current time in the track.
 * - ``seek`` - A function to jump to a certain track time in the audio.
 */
export const useAudio = (): IAudio => {
  const { playQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);
  const { volume, isMuted } = React.useContext(VolumeContext);

  const [isPlaying, setIsPlaying] = React.useState<boolean>(false);
  const [curTime, setCurTime] = React.useState<number>(0);

  const atc = React.useRef<IAudioTracks>({}).current;

  // Whenever we switch to a new track, load the corresponding audio file and begin
  // playing it. For near-gapless playback, we preload the next track shortly after
  // playing this track.
  React.useEffect(() => {
    const track = curIndex !== null ? playQueue[curIndex] : undefined;
    const nextTrack = curIndex !== null ? playQueue[curIndex + 1] : undefined;

    if (atc.curr?.audio) {
      atc.curr.audio.pause();
    }

    if (!track) {
      atc.curr = undefined;
      atc.next = undefined;
      setIsPlaying(false);
      return;
    }

    // Set the current track. If we preloaded it before, just move it up. Otherwise
    // create a new audio track.
    if (atc.next !== undefined && atc.next.trackId === track.id) {
      atc.curr = atc.next;
      atc.curr.audio.play();
    } else {
      atc.curr = {
        audio: new Audio(`/api/files/tracks/${track.id}`),
        trackId: track.id,
      };
      atc.curr.audio.preload = 'auto';
    }

    // Set the next track and begin preloading it.
    if (nextTrack !== undefined) {
      atc.next = {
        audio: new Audio(`/api/files/tracks/${nextTrack.id}`),
        trackId: nextTrack.id,
      };
      atc.next.audio.preload = 'auto';
    } else {
      atc.next = undefined;
    }

    setIsPlaying(true);

    // Set an event listener that will play this track as soon as possible.
    const onCanPlay = (): Promise<void> | undefined => atc.curr?.audio.play();
    atc.curr.audio.addEventListener('canplay', onCanPlay);
    return (): void => atc.curr?.audio.removeEventListener('canplay', onCanPlay);
  }, [playQueue, curIndex]);

  // Set up an event on the current playing audio that handles when a track finishes
  // playing.
  React.useEffect(() => {
    if (atc.curr === undefined) {
      return;
    }

    const onTrackEnd = (): void => {
      setIsPlaying(false);
      setCurIndex((idx) => {
        return idx !== null && idx !== playQueue.length - 1 ? idx + 1 : null;
      });
    };

    const { audio } = atc.curr;
    audio.addEventListener('ended', onTrackEnd);
    return (): void => audio.removeEventListener('ended', onTrackEnd);
  }, [playQueue, curIndex]);

  // Sync the isPlaying variable with the audio. Return a timer to sync curTime with the
  // track progress.
  React.useEffect(() => {
    if (atc.curr === undefined) {
      setIsPlaying(false);
      setCurTime(0);
      return;
    }

    if (isPlaying) {
      if (atc.curr.audio.ended) {
        atc.curr.audio.currentTime = 0;
      }
      if (atc.curr.audio.paused) {
        atc.curr.audio.play();
      }

      const timer = setInterval(() => {
        setCurTime((time) => {
          if (atc.curr === undefined || atc.curr.audio.paused) {
            return time;
          }

          return Math.floor(atc.curr.audio.currentTime);
        });
      }, 500);
      return (): void => clearInterval(timer);
    }

    if (!atc.curr.audio.ended) {
      atc.curr.audio.pause();
    }
  }, [isPlaying]);

  // Sync the currently playing track with the volume.
  React.useEffect(() => {
    if (atc.curr !== undefined) {
      atc.curr.audio.volume = isMuted ? 0 : volume / 100;
    }
  }, [isMuted, volume]);

  // A seek function to set the curTime on the track.
  const seek = (seconds: number): void => {
    if (atc.curr !== undefined) {
      atc.curr.audio.currentTime = seconds;
      setCurTime(seconds);
      setIsPlaying(true);
    }
  };

  return { curTime, isPlaying, seek, setIsPlaying };
};

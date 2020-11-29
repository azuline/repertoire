import * as React from 'react';
import { PlayQueueContext, VolumeContext } from 'src/contexts';
import { SetValue, TrackT } from 'src/types';
import { sleep } from 'src/util';

// TODO: Make sure that we aren't leaking memory from all these audio
// objects... they better be garbage collected properly.

export type AudioT = {
  isPlaying: boolean;
  setIsPlaying: SetValue<boolean>;
  curTime: number;
  seek: SetValue<number>;
};

type AudioReducerState = {
  audio: HTMLAudioElement | null;
  trackId: number | null;
  nextAudio: HTMLAudioElement | null;
  nextTrackId: number | null;
};

type AudioReducerPayload = { track: TrackT | null; nextTrack: TrackT | null };

const INITIAL_AUDIO_STATE = { audio: null, trackId: null, nextAudio: null, nextTrackId: null };

const audioReducer = (
  state: AudioReducerState,
  payload: AudioReducerPayload,
): AudioReducerState => {
  if (state.audio) state.audio.pause();
  if (!payload.track) return INITIAL_AUDIO_STATE;

  return {
    audio:
      state.nextAudio && state.nextTrackId === payload.track.id
        ? state.nextAudio
        : new Audio(`/files/tracks/${payload.track.id}`),
    trackId: payload.track.id,
    nextAudio: payload.nextTrack ? new Audio(`/files/tracks/${payload.nextTrack.id}`) : null,
    nextTrackId: payload.nextTrack?.id ?? null,
  };
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
  const [audioState, audioDispatch] = React.useReducer(audioReducer, INITIAL_AUDIO_STATE);
  const [isPlaying, setIsPlaying] = React.useState<boolean>(false);
  const [curTime, setCurTime] = React.useState<number>(0);

  // Whenever we switch to a new track, load the corresponding audio file and begin playing it.
  // For gapless playback, we preload the next track shortly after playing this track.
  React.useEffect(() => {
    const track = curIndex !== null ? playQueue[curIndex] : null;
    const nextTrack =
      curIndex !== null && curIndex !== playQueue.length - 1 ? playQueue[curIndex + 1] : null;

    audioDispatch({ track, nextTrack });
    setIsPlaying(!!track);
  }, [playQueue, curIndex]);

  // Preload the next audio track. To not compete for bandwidth with the
  // current track, sleep 8 seconds before invoking load.
  //
  // Do we even need to do this? Will browsers prioritize the playing track? Who knows!
  React.useEffect(() => {
    (async (): Promise<void> => {
      await sleep(8000);
      if (audioState?.nextAudio?.paused) {
        audioState.nextAudio.load();
      }
    })();
  }, [audioState]);

  // Set up an event on the current playing audio that handles when a track finishes playing.
  React.useEffect(() => {
    if (!audioState?.audio) return;

    const onTrackEnd = (): void => {
      if (curIndex === playQueue.length - 1) {
        setCurIndex(null);
      } else {
        setCurIndex((idx) => (idx as number) + 1);
      }

      setIsPlaying(false);
    };

    audioState.audio.addEventListener('ended', onTrackEnd);
    return (): void => {
      if (audioState?.audio) audioState.audio.removeEventListener('ended', onTrackEnd);
    };
  }, [audioState, playQueue, curIndex, setCurIndex]);

  // Sync the isPlaying variable with the audio. Return a timer to sync curTime with the track
  // progress.
  React.useEffect(() => {
    if (!audioState.audio) {
      setIsPlaying(false);
      return;
    }

    if (isPlaying) {
      if (audioState.audio.ended) audioState.audio.fastSeek(0);
      if (audioState.audio.paused) audioState.audio.play();

      const timer = setInterval(() => {
        if (audioState.audio) {
          setCurTime(Math.floor(audioState.audio.currentTime));
        } else {
          setCurTime(0);
        }
      }, 1);
      return (): void => clearInterval(timer);
    }

    if (!audioState.audio.ended) {
      audioState.audio.pause();
    }
  }, [isPlaying, audioState]);

  // Sync the currently playing track with the volume.
  React.useEffect(() => {
    if (audioState.audio) audioState.audio.volume = isMuted ? 0 : volume / 100;
  }, [audioState, isMuted, volume]);

  // A seek function to set the curTime on the track.
  const seek = React.useCallback(
    (seconds) => audioState.audio && audioState.audio.fastSeek(seconds),
    [audioState],
  );

  return { isPlaying, setIsPlaying, curTime, seek };
};

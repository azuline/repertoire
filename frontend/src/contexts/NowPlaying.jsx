import React, { useState, useMemo, useEffect } from 'react';
import { useAudio } from 'hooks';

export const NowPlayingContext = React.createContext({
  playQueue: [],
  setPlayQueue: () => {},
  currentQueueIndex: 0,
  setCurrentQueueIndex: () => {},
  playHistory: [],
  setPlayHistory: () => {},
});

export const NowPlayingContextProvider = ({ children }) => {
  const [playQueue, setPlayQueue] = useState([]);
  const [currentQueueIndex, setCurrentQueueIndex] = useState(0);
  const [playHistory, setPlayHistory] = useState([]);
  const { audio, setTrackId, playing, setPlaying, time, setTime, seek } = useAudio(
    null
  );
  const [totalTime, setTotalTime] = useState(0);

  // Fetch current track object from playQueue.
  const currentTrack = useMemo(() => playQueue[currentQueueIndex], [
    playQueue,
    currentQueueIndex,
  ]);

  // If current track changes, set the audio file and total time accordingly.
  useEffect(() => {
    if (!currentTrack) {
      setTrackId(null);
      setTime(0);
      setTotalTime(0);
    } else {
      setTrackId(currentTrack.id);
      setTotalTime(currentTrack.duration);
      setPlayHistory((history) => [currentTrack.id, ...history]);
    }
  }, [setTrackId, setTime, setPlayHistory, currentTrack]);

  // If current track ends, and we still have tracks in queue, begin next track.
  useEffect(() => {
    if (!audio) return;

    const onEnded = () => {
      if (currentQueueIndex !== playQueue.length - 1) {
        setCurrentQueueIndex(currentQueueIndex + 1);
      } else {
        setPlaying(false);
      }
    };

    audio.addEventListener('ended', onEnded);
    return () => audio.removeEventListener('ended', onEnded);
  }, [audio, currentQueueIndex, playQueue, setCurrentQueueIndex, setPlaying]);

  const value = {
    playQueue,
    setPlayQueue,
    currentQueueIndex,
    setCurrentQueueIndex,
    playHistory,
    currentTrack,
    audio,
    playing,
    setPlaying,
    time,
    totalTime,
    seek,
  };

  return (
    <NowPlayingContext.Provider value={value}>{children}</NowPlayingContext.Provider>
  );
};

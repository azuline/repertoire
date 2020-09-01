import React, { useState } from 'react';

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

  const value = {
    playQueue,
    setPlayQueue,
    currentQueueIndex,
    setCurrentQueueIndex,
    playHistory,
    setPlayHistory,
  };

  return (
    <NowPlayingContext.Provider value={value}>{children}</NowPlayingContext.Provider>
  );
};

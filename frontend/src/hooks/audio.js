import { useCallback, useEffect, useState } from 'react';
import { useRequest } from 'hooks';

const useMedia = () => {
  const [media, setMediaRaw] = useState(null);

  const setMedia = useCallback(
    (newMedia) =>
      setMediaRaw((oldMedia) => {
        if (oldMedia && !(oldMedia.ended || oldMedia.paused)) {
          oldMedia.pause();
        }

        newMedia.play();
        return newMedia;
      }),
    [setMediaRaw]
  );

  return [media, setMedia];
};

export const useAudio = (initialTrackId) => {
  const request = useRequest();
  const [trackId, setTrackId] = useState(initialTrackId);
  const [playing, setPlaying] = useState(false);
  const [audio, setAudio] = useMedia();
  const [time, setTime] = useState(0);

  // Whenever a new trackId is set, update the audio object.
  useEffect(() => {
    if (!trackId) return;

    (async () => {
      const response = await request(`/files/tracks/${trackId}`);
      const blob = await response.blob();
      const audio = new Audio(URL.createObjectURL(blob));
      setAudio(audio);
      setPlaying(true);
    })();
  }, [request, trackId, setAudio, setPlaying]);

  // Add hooks to manage time setting on active audio.
  useEffect(() => {
    if (playing) {
      if (audio.ended) audio.fastSeek(0);
      if (audio.paused) audio.play();

      const timer = setInterval(() => setTime(Math.floor(audio.currentTime), 1));
      return () => clearInterval(timer);
    } else if (audio && !audio.ended) {
      audio.pause();
    }
  }, [playing, setPlaying, audio]);

  return { audio, setTrackId, playing, setPlaying, time };
};

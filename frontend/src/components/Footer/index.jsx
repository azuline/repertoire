import React, { useCallback, useEffect, useMemo, useState, useContext } from 'react';
import { CoverArt } from 'components/common/CoverArt';
import './index.scss';
import { NowPlayingContext } from 'contexts';
import { ProgressBar, ControlGroup, Button, Card } from '@blueprintjs/core';
import { TrackArtists } from 'components/Release/TrackList/Artists';
import { secondsToLength } from 'common/tracks';
import { useAudio } from 'hooks';
import { TopToaster } from 'components/Toaster';

export const Footer = () => {
  const { audio, setTrackId, playing, setPlaying, time } = useAudio(null);
  const [expanded, setExpanded] = useState(false);
  const [totalTime, setTotalTime] = useState(0);
  const { playQueue, currentQueueIndex, setCurrentQueueIndex } = useContext(
    NowPlayingContext
  );

  // Fetch current track object from playQueue.
  const currentTrack = useMemo(() => playQueue[currentQueueIndex], [
    playQueue,
    currentQueueIndex,
  ]);

  // If current track changes, set the audio file and total time accordingly.
  useEffect(() => {
    if (!currentTrack) return;

    setTrackId(currentTrack.id);
    setTotalTime(currentTrack.duration);
  }, [setTrackId, currentTrack]);

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

  // Function to handle clicking of play button.
  const togglePlay = useCallback(() => {
    if (!audio) {
      TopToaster.show({
        icon: 'music',
        intent: 'danger',
        message: 'Nothing to play!',
        timeout: 2000,
      });
      return;
    }

    if (playing) {
      setPlaying(false);
    } else if (audio.paused && !audio.ended) {
      setPlaying(true);
    } else if (playQueue.length === 1) {
      audio.fastSeek(0);
      setPlaying(true);
    } else {
      setCurrentQueueIndex(0);
    }
  }, [audio, playing, setPlaying, playQueue, setCurrentQueueIndex]);

  return (
    <Card className={'Footer' + (expanded ? ' Expanded' : '')}>
      <div className="LongMainInfo">
        <div className="ShortMainInfo">
          <ControlGroup className="PlayButtons">
            <Button icon="fast-backward" />
            <Button icon={playing ? 'pause' : 'play'} onClick={togglePlay} />
            <Button icon="fast-forward" />
          </ControlGroup>
          <CoverArt
            releaseId={currentTrack ? currentTrack.release.id : null}
            hasImage={currentTrack ? currentTrack.release.hasImage : null}
          />
          <div className="PlayTrackInfo">
            <div className="TrackTitle">
              {currentTrack ? currentTrack.title : 'N/A'}
            </div>
            <TrackArtists artists={currentTrack ? currentTrack.artists : []} minimal />
          </div>
        </div>
        <div className="PlayStatus">
          <div className="CurrentTime">{secondsToLength(time)}</div>
          <ProgressBar
            className="TimeProgress"
            animate={false}
            intent="primary"
            value={totalTime !== 0 ? time / totalTime : 0}
          />
          <div className="TotalTime">{secondsToLength(totalTime)}</div>
        </div>
      </div>
      <div className="PlayQueue">
        {playQueue.length === 0 ? (
          <div className="EmptyQueue">Play queue empty.</div>
        ) : (
          <div className="TrackListTracks">
            {[...playQueue.entries()].map(([index, track]) => (
              <Card
                key={index}
                className="Track"
                onClick={() => setCurrentQueueIndex(index)}
              >
                <div className="TrackSimpleInfo">
                  <div className="TrackNumber">{index + 1}</div>
                  <div className="TrackTitle">{track.title}</div>
                  <div className="TrackLength">{secondsToLength(track.duration)}</div>
                </div>
                <TrackArtists artists={track.artists} minimal />
              </Card>
            ))}
          </div>
        )}
      </div>
      <div className="ExpandFooter">
        <Button
          minimal
          icon={expanded ? 'chevron-down' : 'chevron-up'}
          onClick={() => setExpanded(!expanded)}
        />
      </div>
    </Card>
  );
};

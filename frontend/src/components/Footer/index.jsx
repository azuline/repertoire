import React, { useCallback, useState, useContext } from 'react';
import { CoverArt } from 'components/common/CoverArt';
import './index.scss';
import { NowPlayingContext } from 'contexts';
import { ProgressBar, ControlGroup, Button, Card } from '@blueprintjs/core';
import { TrackArtists } from 'components/Release/TrackList/Artists';
import { secondsToLength } from 'common/tracks';
import { TopToaster } from 'components/Toaster';

export const Footer = () => {
  const [expanded, setExpanded] = useState(false);
  const {
    currentTrack,
    audio,
    time,
    totalTime,
    playing,
    setPlaying,
    playQueue,
    currentQueueIndex,
    setCurrentQueueIndex,
  } = useContext(NowPlayingContext);

  // Function to handle clicking of play button.
  const togglePlay = useCallback(() => {
    if (currentQueueIndex === -1) {
      setCurrentQueueIndex(0);
    } else if (!audio) {
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
    } else if (audio && audio.paused && !audio.ended) {
      setPlaying(true);
    } else if (playQueue.length === 1) {
      audio.fastSeek(0);
      setPlaying(true);
    } else {
      setCurrentQueueIndex(0);
    }
  }, [audio, playing, setPlaying, playQueue, currentQueueIndex, setCurrentQueueIndex]);

  const nextTrack = useCallback(() => {
    if (currentQueueIndex === playQueue.length - 1) {
      setCurrentQueueIndex(-1);
    } else {
      setCurrentQueueIndex((index) => index + 1);
    }
  }, [currentQueueIndex, playQueue, setCurrentQueueIndex]);

  const prevTrack = useCallback(() => {
    if (currentQueueIndex === 0) {
      setCurrentQueueIndex(-1);
    } else {
      setCurrentQueueIndex((index) => index - 1);
    }
  }, [currentQueueIndex, setCurrentQueueIndex]);

  return (
    <Card className={'Footer' + (expanded ? ' Expanded' : '')}>
      <div className="LongMainInfo">
        <div className="ShortMainInfo">
          <ControlGroup className="PlayButtons">
            <Button icon="fast-backward" onClick={prevTrack} />
            <Button icon={playing ? 'pause' : 'play'} onClick={togglePlay} />
            <Button icon="fast-forward" onClick={nextTrack} />
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
        <div className="QueueTitle">Play Queue</div>
        {playQueue.length === 0 ? (
          <div className="EmptyQueue">Play queue empty.</div>
        ) : (
          <div className="TrackListTracks">
            {[...playQueue.entries()].map(([index, track]) => (
              <Card
                key={index}
                className={'Track' + (currentQueueIndex === index ? ' Active' : '')}
                onClick={() => {
                  setCurrentQueueIndex(index);
                  TopToaster.show({
                    icon: 'image',
                    message: 'Loading track...',
                    timeout: 1000,
                  });
                }}
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

import React from 'react';
import { TrackList } from './TrackList.jsx';

export const FlatTrackList = (props) => {
  return (
    <div className="FlatTrackList">
      <div className="TopArrowPointer"></div>
      <TrackList {...props} />
    </div>
  );
};

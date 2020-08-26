import { Popover } from '@blueprintjs/core';
import React from 'react';
import { TrackList } from './TrackList';

export const PopoverTrackList = (props) => {
  return (
    <Popover
      portalClassName="PopoverPortalTrackList"
      popoverClassName="PopoverTrackList"
      content={<TrackList {...props} />}
      position="bottom"
      modifiers={{
        flip: { enabled: false },
        preventOverflow: {
          boundariesElement: 'scrollParent',
          enabled: true,
          padding: 0,
          priority: ['left', 'top', 'right'],
        },
      }}
    >
      {props.children}
    </Popover>
  );
};

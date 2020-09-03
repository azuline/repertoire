import { Popover } from '@blueprintjs/core';
import React, { useContext } from 'react';
import { TrackList } from './TrackList';
import { SideBarContext } from 'contexts';

export const PopoverTrackList = (props) => {
  const { numVisible } = useContext(SideBarContext);

  return (
    <Popover
      portalClassName={`PopoverPortalTrackList SideBars${numVisible}`}
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

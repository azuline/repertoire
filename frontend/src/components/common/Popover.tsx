import * as React from 'react';

import RawPopover from 'react-awesome-popover';

export const Popover: React.FC<{
  children: React.ReactNode;
  placement: string;
  arrowColor?: string;
}> = ({ children, placement, arrowColor = '' }) => {
  return (
    <RawPopover
      placement={placement}
      arrowProps={{ className: arrowColor }}
      overlayColor="rgba(0,0,0,0)"
    >
      {children}
    </RawPopover>
  );
};

import * as React from 'react';
import { Icon, IconT } from 'src/components';

export const Arrow: React.FC<{ direction: 'left' | 'right'; onClick: () => void }> = ({
  direction,
  onClick,
}) => (
  <div className="flex-none h-full px-1 cursor-pointer" onClick={onClick}>
    <Icon
      className="flex items-center w-4 h-full text-primary"
      icon={`chevron-double-${direction}-small` as IconT}
    />
  </div>
);

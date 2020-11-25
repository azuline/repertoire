import * as React from 'react';
import { Icon, IconT } from 'src/components';

export const Arrow: React.FC<{ direction: 'left' | 'right'; onClick: () => void }> = ({
  direction,
  onClick,
}) => (
  <div className="flex-none px-1 cursor-pointer h-full" onClick={onClick}>
    <Icon
      className="w-4 h-full text-primary flex items-center"
      icon={`chevron-double-${direction}-small` as IconT}
    />
  </div>
);

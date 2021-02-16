import 'twin.macro';

import * as React from 'react';

import { Icon, IconT } from '~/components';

export const Arrow: React.FC<{ direction: 'left' | 'right'; onClick: () => void }> = ({
  direction,
  onClick,
}) => (
  <div tw="flex items-center flex-none h-full px-1 cursor-pointer" onClick={onClick}>
    <Icon icon={`chevron-double-${direction}-small` as IconT} tw="w-4 text-primary-500" />
  </div>
);

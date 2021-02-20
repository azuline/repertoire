import * as React from 'react';

import { Icon, IIcon } from '~/components';

type IArrow = React.FC<{ direction: 'left' | 'right'; onClick: () => void }>;

export const Arrow: IArrow = ({ direction, onClick }) => (
  <div tw="flex items-center flex-none h-full px-1 cursor-pointer" onClick={onClick}>
    <Icon icon={`chevron-double-${direction}-small` as IIcon} tw="w-4 text-primary-500" />
  </div>
);

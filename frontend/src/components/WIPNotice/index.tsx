import * as React from 'react';

import { Icon } from '~/components/common';

export const WIPNotice: React.FC = () => (
  <div tw="flex">
    <div tw="py-4 px-6 rounded bg-background-950 flex items-center gap-2">
      <Icon icon="warning-small" tw="w-7 text-yellow-200" />
      <div>This feature is a work in progress.</div>
    </div>
  </div>
);

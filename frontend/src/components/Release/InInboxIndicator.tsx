import 'twin.macro';

import clsx from 'clsx';
import * as React from 'react';

export const InInboxIndicator: React.FC<{ className?: string }> = ({ className }) => (
  <div className={clsx(className, 'flex items-center flex-none')} title="In Inbox">
    <div tw="w-2.5 h-2.5 bg-blue-500 rounded-full" />
  </div>
);

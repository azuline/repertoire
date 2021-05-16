import React from 'react';

type IInInboxIndicator = React.FC<{ className?: string }>;

export const InInboxIndicator: IInInboxIndicator = ({ className }) => (
  <div className={className} title="In Inbox" tw="flex items-center flex-none">
    <div tw="w-2.5 h-2.5 bg-blue-500 rounded-full" />
  </div>
);

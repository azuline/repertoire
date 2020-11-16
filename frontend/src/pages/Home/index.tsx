import * as React from 'react';

import { RecentlyAdded } from './RecentlyAdded';

export const Home: React.FC = (): React.ReactElement => {
  return (
    <div className="flex-1">
      <RecentlyAdded />
    </div>
  );
};

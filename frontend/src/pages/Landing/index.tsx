import * as React from 'react';
import { RecentlyAdded } from './RecentlyAdded';

export const Landing: React.FC = (): React.ReactElement => {
  return (
    <div className="flex flex-col flex-no-wrap">
      <RecentlyAdded />
    </div>
  );
};

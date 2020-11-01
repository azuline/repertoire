import * as React from 'react';
import { RecentlyAdded } from './RecentlyAdded';

export const Home: React.FC = (): React.ReactElement => {
  return (
    <div className="flex flex-col mt-4">
      <RecentlyAdded />
    </div>
  );
};

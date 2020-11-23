import * as React from 'react';

import { Header } from 'src/components/Header';
import { RecentlyAdded } from './RecentlyAdded';

export const Home: React.FC = (): React.ReactElement => {
  return (
    <>
      <Header />
      <RecentlyAdded />
    </>
  );
};

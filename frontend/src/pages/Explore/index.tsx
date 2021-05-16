import React from 'react';

import { Header } from '~/components';

import { RecentlyAdded } from './RecentlyAdded';

export const Explore: React.FC = () => (
  <>
    <Header />
    <RecentlyAdded />
    <span tw="py-8">More to come later~</span>
  </>
);

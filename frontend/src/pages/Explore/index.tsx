import 'twin.macro';

import * as React from 'react';

import { Header } from '~/components';

import { RecentlyAdded } from './RecentlyAdded';

export const Explore: React.FC = (): React.ReactElement => (
  <>
    <Header />
    <RecentlyAdded />
    <span tw="py-8">More to come later~</span>
  </>
);

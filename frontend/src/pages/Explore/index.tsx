import * as React from 'react';

import { Layout } from '~/layout';

import { RecentlyAdded } from './RecentlyAdded';

export const Explore: React.FC = () => (
  <Layout padY>
    <RecentlyAdded />
    <div>
      <span tw="flex pad-page my-12">More to come later~</span>
    </div>
  </Layout>
);

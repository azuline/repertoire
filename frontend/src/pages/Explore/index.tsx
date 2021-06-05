import * as React from 'react';

import { Layout } from '~/layout';

import { RecentlyAdded } from './RecentlyAdded';

export const Explore: React.FC = () => (
  <Layout pad>
    <RecentlyAdded />
    <div>
      <span tw="flex my-12">More to come later~</span>
    </div>
  </Layout>
);

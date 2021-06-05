import * as React from 'react';

import { RouteList } from '~/components';
import { Layout } from '~/layout';

export const Mobile: React.FC = () => (
  <Layout pad scroll tw="py-4 flex flex-col">
    <RouteList />
  </Layout>
);

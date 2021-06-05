import * as React from 'react';

import { SectionHeader } from '~/components';
import { Layout } from '~/layout';

import { ThemeSettings } from './Theme';
import { UserSettings } from './User';

export const Settings: React.FC = () => (
  <Layout pad scroll>
    <SectionHeader tw="mt-4 mb-8">Settings</SectionHeader>
    <UserSettings />
    <ThemeSettings />
  </Layout>
);

import * as React from 'react';

import { SectionHeader } from '~/components';
import { Layout } from '~/layout';

import { IndexCrontab } from './IndexCrontab';
import { MusicDirectories } from './MusicDirectories';
import { ThemeSettings } from './Theme';
import { UserSettings } from './User';

// TODO: Give this entire page a make over.

export const Settings: React.FC = () => (
  <Layout pad scroll tw="flex flex-col gap-8">
    <SectionHeader>Personal Settings</SectionHeader>
    <UserSettings />
    <ThemeSettings />
    <SectionHeader>Server Settings</SectionHeader>
    <MusicDirectories />
    <IndexCrontab />
  </Layout>
);

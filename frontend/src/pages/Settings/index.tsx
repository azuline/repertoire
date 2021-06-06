import * as React from 'react';

import { SectionHeader, WIPNotice } from '~/components';
import { Layout } from '~/layout';

import { IndexCrontab } from './IndexCrontab';
import { MusicDirectories } from './MusicDirectories';
import { ThemeSettings } from './Theme';
import { UserSettings } from './User';

// TODO: Give this entire page a make over. Make the options like actually usable and
// stylish, improve the navigation, and also add some information text for each setting.

export const Settings: React.FC = () => (
  <Layout pad scroll tw="flex flex-col gap-8">
    <WIPNotice />
    <SectionHeader>Personal Settings</SectionHeader>
    <UserSettings />
    <ThemeSettings />
    <SectionHeader>Server Settings</SectionHeader>
    <MusicDirectories />
    <IndexCrontab />
  </Layout>
);

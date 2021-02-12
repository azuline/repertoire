import * as React from 'react';

import { Header, SectionHeader } from '~/components';

import { ThemeSettings } from './Theme';
import { UserSettings } from './User';

export const Settings: React.FC = () => (
  <>
    <Header searchbar={false} />
    <SectionHeader className="mt-4 mb-8">Settings</SectionHeader>
    <UserSettings />
    <ThemeSettings />
  </>
);

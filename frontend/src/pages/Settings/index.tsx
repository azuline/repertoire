import * as React from 'react';

import { SectionHeader } from '~/components';

import { ThemeSettings } from './Theme';
import { UserSettings } from './User';

export const Settings: React.FC = () => (
  <>
    <SectionHeader tw="mt-4 mb-8">Settings</SectionHeader>
    <UserSettings />
    <ThemeSettings />
  </>
);

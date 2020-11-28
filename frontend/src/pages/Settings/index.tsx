import * as React from 'react';
import { Header, SectionHeader } from 'src/components';

import { ThemeSettings } from './Theme';
import { UserSettings } from './User';

export const Settings: React.FC = () => (
  <div>
    <Header searchbar={false} />
    <div className="px-8">
      <SectionHeader className="mt-4 mb-8">Settings</SectionHeader>
      <UserSettings />
      <ThemeSettings />
    </div>
  </div>
);

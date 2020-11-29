import * as React from 'react';
import { Icon } from 'src/components';

import { RedirectToNowPlaying } from './RedirectToNowPlaying';

export const ExpandPlaying: React.FC = () => (
  <RedirectToNowPlaying className="p-2 pr-4 hover:text-primary-400 text-primary-500 sm:pr-8">
    <Icon className="w-6" icon="chevron-up-medium" />
  </RedirectToNowPlaying>
);

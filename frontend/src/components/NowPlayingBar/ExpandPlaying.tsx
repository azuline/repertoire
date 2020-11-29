import * as React from 'react';
import { Icon } from 'src/components';

import { RedirectToNowPlaying } from './RedirectToNowPlaying';

export const ExpandPlaying: React.FC = () => (
  <RedirectToNowPlaying className="p-2 pr-4 sm:pr-8 text-primary-alt hover:text-primary">
    <Icon icon="chevron-up-medium" className="w-6" />
  </RedirectToNowPlaying>
);

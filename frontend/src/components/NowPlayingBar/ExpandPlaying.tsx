import * as React from 'react';
import { Icon } from '~/components';

import { RedirectToNowPlaying } from './RedirectToNowPlaying';

export const ExpandPlaying: React.FC = () => (
  <RedirectToNowPlaying className="hidden p-2 pr-8 sm:block hover:text-primary-400 text-primary-500">
    <Icon className="w-6" icon="chevron-up-medium" />
  </RedirectToNowPlaying>
);

import * as React from 'react';

import { Icon } from '~/components';

import { RedirectToNowPlaying } from './RedirectToNowPlaying';

export const ExpandPlaying: React.FC = () => (
  <RedirectToNowPlaying tw="hidden pl-2 sm:block">
    <div tw="hover:text-primary-400 text-primary-500">
      <Icon icon="chevron-up-medium" tw="w-6" />
    </div>
  </RedirectToNowPlaying>
);

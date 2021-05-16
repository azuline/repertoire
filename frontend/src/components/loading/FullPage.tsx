import React from 'react';
import ReactLoading from 'react-loading';

import { colors } from '~/colors';

export const FullPageLoading: React.FC = () => (
  <div tw="full flex items-center justify-center">
    <ReactLoading
      color={colors.primary[500]}
      height={120}
      type="spinningBubbles"
      width={120}
    />
  </div>
);

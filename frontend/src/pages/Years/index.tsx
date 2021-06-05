import * as React from 'react';

import { useId } from '~/hooks';
import { Layout } from '~/layout';

import { YearChooser } from './Chooser';
import { Year } from './Year';

export const Years: React.FC = () => {
  const active = useId();

  return (
    <Layout tw="flex flex-1">
      <YearChooser active={active} tw="flex-none" />
      {active !== null && (
        <Layout pad scroll>
          <Year active={active} />
        </Layout>
      )}
    </Layout>
  );
};

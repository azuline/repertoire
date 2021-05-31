import * as React from 'react';

import { useId } from '~/hooks';

import { YearChooser } from './Chooser';
import { Year } from './Year';

export const Years: React.FC = () => {
  const active = useId();

  return (
    <div tw="flex flex-1">
      <YearChooser active={active} tw="flex-none" />
      {active !== null && <Year active={active} />}
    </div>
  );
};

import * as React from 'react';
import { Header } from '~/components';
import { useId } from '~/hooks';

import { YearChooser } from './Chooser';
import { Year } from './Year';

export const Years: React.FC = () => {
  const active = useId();

  return (
    <>
      {!active && <Header />}
      <div className="flex flex-1">
        <YearChooser active={active} className="flex-none" />
        {active && <Year active={active} />}
      </div>
    </>
  );
};

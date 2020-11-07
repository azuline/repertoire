import * as React from 'react';

import { Element, ElementT } from './Element';

import clsx from 'clsx';

const style = { maxHeight: 'calc(100vh - 4rem)' };

export const Chooser: React.FC<{
  className?: string;
  setter: (arg0: number[]) => void;
  results: ElementT[];
}> = ({ className = '', setter, results }) => {
  const [active, setActive] = React.useState<number | null>(null);

  React.useEffect(() => setter(active ? [active] : []), [active]);

  return (
    <div
      className={clsx(className, 'rpr--chooser sticky mt-4 pt-4 top-0 w-48 overflow-y-auto')}
      style={style}
    >
      {results.map((elem: ElementT) => (
        <Element key={elem.id} element={elem} active={active} setActive={setActive} />
      ))}
    </div>
  );
};

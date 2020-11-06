import * as React from 'react';

import { Element, ElementT } from './Element';

import clsx from 'clsx';

const style = { height: 'calc(100vh - 4rem)' };

export const Chooser: React.FC<{
  className?: string;
  setter: (arg0: number[]) => void;
  results: ElementT[];
}> = ({ className = '', setter, results }) => {
  const [active, setActive] = React.useState<number>(0);

  React.useEffect(() => setter(active !== 0 ? [active] : []), [active]);

  return (
    <div
      className={clsx(className, 'rpr--chooser sticky mt-4 pt-4 top-0 w-48 overflow-y-auto')}
      style={style}
    >
      <Element element={null} active={active} setActive={setActive} />
      {results.map((elem: ElementT) => (
        <Element key={elem.id} element={elem} active={active} setActive={setActive} />
      ))}
    </div>
  );
};

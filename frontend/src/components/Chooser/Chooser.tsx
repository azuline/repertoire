import * as React from 'react';

import { Element, ElementT } from './Element';

import { Icon } from 'src/components/common/Icon';
import clsx from 'clsx';

const style = { maxHeight: 'calc(100vh - 4rem)' };

export const Chooser: React.FC<{
  className?: string | undefined;
  results: ElementT[];
  setter: (arg0: number[]) => void;
  filter: string;
  setFilter: (arg0: string) => void;
}> = ({ className, results, setter, filter, setFilter }) => {
  const [active, setActive] = React.useState<number | null>(null);

  React.useEffect(() => setter(active ? [active] : []), [active]);

  const updateFilter = React.useCallback((e) => setFilter(e.target.value), [setFilter]);

  return (
    <div
      className={clsx(className, 'rpr--chooser sticky mt-4 pt-4 top-0 w-64 overflow-y-auto')}
      style={style}
    >
      <div className="relative w-full pl-8 pr-4 mb-2">
        <input
          className="w-full pl-7"
          placeholder="Filter"
          value={filter}
          onChange={updateFilter}
        />
        <div className="h-full absolute top-0 left-0 ml-8 px-1 flex items-center pointer-events-none">
          <Icon className="w-5 text-bold" icon="filter-small" />
        </div>
      </div>
      {results.map((elem: ElementT) => (
        <Element key={elem.id} element={elem} active={active} setActive={setActive} />
      ))}
    </div>
  );
};

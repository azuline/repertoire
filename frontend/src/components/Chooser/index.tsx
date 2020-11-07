import * as React from 'react';
import { SidebarContext } from 'src/contexts';

import { Element, ElementT } from './Element';

import { Icon } from 'src/components/common/Icon';
import clsx from 'clsx';

const style = { maxHeight: 'calc(100vh - 4rem)', bottom: '4rem' };

export const Chooser: React.FC<{
  className?: string | undefined;
  results: ElementT[];
  active: number | null;
  setActive: (arg0: number | null) => void;
  filter: string;
  setFilter: (arg0: string) => void;
}> = ({ className, results, active, setActive, filter, setFilter }) => {
  const { openBar } = React.useContext(SidebarContext);

  const bp = React.useMemo(() => (openBar ? 'lg' : 'md'), [openBar]);
  const updateFilter = React.useCallback((e) => setFilter(e.target.value), [setFilter]);

  return (
    <div
      className={clsx(
        className,
        active
          ? `hidden ${bp}:block w-64 ${bp}:sticky ${bp}:self-end ${bp}:overflow-y-auto`
          : 'w-full',
        'rpr--chooser mt-4 pt-4',
      )}
      style={active ? style : {}}
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

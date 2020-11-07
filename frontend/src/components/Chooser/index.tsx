import * as React from 'react';

import { AutoSizer, List, WindowScroller } from 'react-virtualized';
import { SidebarContext } from 'src/contexts';

import { Element, ElementT } from './Element';

import { Icon } from 'src/components/common/Icon';
import clsx from 'clsx';

const style = { maxHeight: 'calc(100vh - 4rem)' };

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

  // Virtual render setup.
  const scrollRef = React.useRef<WindowScroller>();

  const renderRow = React.useCallback(
    ({ index, key, style }) => {
      return (
        <div key={key} style={style}>
          <Element element={results[index]} active={active} setActive={setActive} />
        </div>
      );
    },
    [results, active, setActive],
  );

  return (
    <div
      className={clsx(
        className,
        active ? `hidden ${bp}:flex ${bp}:flex-col w-64 ${bp}:sticky ${bp}:top-0` : 'w-full',
        'py-4',
      )}
      style={active ? style : {}}
    >
      <div className="relative w-full pl-8 pr-4 mb-2 flex-none">
        <input
          className="w-full pl-9"
          placeholder="Filter"
          value={filter}
          onChange={updateFilter}
        />
        <div className="h-full absolute top-0 left-0 ml-9 px-1 flex items-center pointer-events-none">
          <Icon className="w-5 text-bold" icon="filter-small" />
        </div>
      </div>
      <div className={clsx('flex-auto hidden', active && `${bp}:block`)}>
        <AutoSizer>
          {({ width, height }): React.ReactNode => (
            <List
              height={height}
              overscanRowCount={8}
              rowCount={results.length}
              rowHeight={28.5}
              rowRenderer={renderRow}
              width={width}
            />
          )}
        </AutoSizer>
      </div>
      <div className={clsx('', active ? `${bp}:hidden` : undefined)}>
        <AutoSizer disableHeight>
          {({ width }): React.ReactNode => (
            <WindowScroller ref={scrollRef as React.RefObject<WindowScroller>}>
              {({ height, isScrolling, onChildScroll, scrollTop }): React.ReactNode => (
                <List
                  autoHeight
                  height={height}
                  isScrolling={isScrolling}
                  onScroll={onChildScroll}
                  overscanRowCount={8}
                  rowCount={results.length}
                  rowHeight={28.5}
                  rowRenderer={renderRow}
                  scrollTop={scrollTop}
                  width={width}
                />
              )}
            </WindowScroller>
          )}
        </AutoSizer>
      </div>
    </div>
  );
};

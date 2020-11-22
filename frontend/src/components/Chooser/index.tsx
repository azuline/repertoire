import * as React from 'react';

import { AutoSizer, List, WindowScroller } from 'react-virtualized';
import { Element, ElementT } from './Element';

import { SidebarContext } from 'src/contexts';
import clsx from 'clsx';

const style = { maxHeight: 'calc(100vh - 4rem)' };

export const Chooser: React.FC<{
  className?: string | undefined;
  results: ElementT[];
  active: number | null;
  makeUrl: (arg0: number) => string;
}> = ({ className, results, active, makeUrl }) => {
  const { openBar } = React.useContext(SidebarContext);
  const bp = React.useMemo(() => (openBar ? 'xl' : 'lg'), [openBar]);

  // Virtual render setup.
  const scrollRef = React.useRef<WindowScroller>();
  const renderRow = React.useCallback(
    ({ index, key, style }) => {
      return (
        <div key={key} style={style}>
          <Element element={results[index]} active={active} makeUrl={makeUrl} />
        </div>
      );
    },
    [results, active, makeUrl],
  );
  const scrollToIndex = React.useMemo(
    () => (active ? results.findIndex((elem) => elem.id === active) : undefined),
    [active, results],
  );

  return (
    <div
      className={clsx(
        className,
        active ? `hidden ${bp}:flex ${bp}:flex-col ${bp}:sticky ${bp}:top-0` : 'w-full',
        openBar ? 'w-80' : 'w-84',
      )}
      style={active ? style : {}}
    >
      <div className={clsx('flex-auto hidden bg-background-alt', active && `${bp}:block`)}>
        <div className="w-full -mt-24 h-24 bg-background-alt border-b-2 border-background-alt2" />
        <AutoSizer>
          {({ width, height }): React.ReactNode => (
            <List
              className="py-4"
              height={height}
              overscanRowCount={8}
              rowCount={results.length}
              rowHeight={28.5}
              rowRenderer={renderRow}
              scrollToIndex={scrollToIndex}
              width={width}
            />
          )}
        </AutoSizer>
      </div>
      <div className={active ? `${bp}:hidden` : undefined}>
        <AutoSizer disableHeight>
          {({ width }): React.ReactNode => (
            <WindowScroller ref={scrollRef as React.RefObject<WindowScroller>}>
              {({ height, isScrolling, onChildScroll, scrollTop }): React.ReactNode => (
                <List
                  className="py-4"
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

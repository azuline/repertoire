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
        active
          ? openBar
            ? 'hidden xl:flex xl:flex-col xl:sticky xl:top-0'
            : 'hidden lg:flex lg:flex-col lg:sticky lg:top-0'
          : 'w-full',
        openBar ? 'w-80' : 'w-88',
      )}
      style={active ? style : {}}
    >
      <div
        className={clsx(
          'flex-auto hidden bg-background-alt',
          active && (openBar ? 'xl:block' : 'lg:block'),
        )}
      >
        <div className="w-full -mt-24 h-24 bg-background-alt" />
        <AutoSizer>
          {({ width, height }): React.ReactNode => (
            <List
              className="chooser pt-4"
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
      <div className={active ? (openBar ? 'xl:hidden' : 'lg:hidden') : undefined}>
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

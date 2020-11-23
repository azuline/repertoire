import * as React from 'react';

import { AutoSizer, List } from 'react-virtualized';
import { Element, ElementT } from './Element';
import { JumpToLetter } from './JumpToLetter';

import { SidebarContext } from 'src/contexts';
import clsx from 'clsx';

const style = { maxHeight: 'calc(100vh - 9rem)' };

export const Chooser: React.FC<{
  className?: string | undefined;
  results: ElementT[];
  active: number | null;
  makeUrl: (arg0: number) => string;
}> = ({ className, results, active, makeUrl }) => {
  const { openBar } = React.useContext(SidebarContext);
  const [jumpTo, setJumpTo] = React.useState<number | null>(null);

  // Virtual render setup.
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

  const [scrollToIndex, scrollToAlignment] = React.useMemo(() => {
    if (jumpTo) {
      return [jumpTo, 'start'];
    } else if (active) {
      return [results.findIndex((elem) => elem.id === active), 'auto'];
    } else {
      return [undefined, 'auto'];
    }
  }, [jumpTo, active, results]);

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
          'relative h-full flex-auto',
          active && (openBar ? 'xl:bg-background-alt' : 'lg:bg-background-alt'),
        )}
      >
        <div
          className={clsx(
            'hidden w-full -mt-24 h-24 bg-background-alt',
            active && (openBar ? 'xl:block' : 'lg:block'),
          )}
        />
        <JumpToLetter results={results} setJumpTo={setJumpTo} />
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
              scrollToAlignment={scrollToAlignment as 'start' | 'auto'}
              width={width}
            />
          )}
        </AutoSizer>
      </div>
    </div>
  );
};

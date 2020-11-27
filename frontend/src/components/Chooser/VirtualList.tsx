import clsx from 'clsx';
import * as React from 'react';
import { AutoSizer, List } from 'react-virtualized';

import { Element, ElementT, ToggleStarFactory } from './Element';

export const VirtualList: React.FC<{
  results: ElementT[];
  active: number | null;
  jumpTo: number | null;
  urlFactory: (arg0: number) => string;
  toggleStarFactory: ToggleStarFactory;
}> = ({ results, active, jumpTo, urlFactory, toggleStarFactory }) => {
  const renderRow = React.useCallback(
    ({ index, key, style }) => {
      // Because React-Virtualized has bungled scrollToIndex behavior when the
      // containing div has margin/padding, we replaced the margin/padding with
      // these blank elements on the bottom.
      if (index === results.length || index === results.length + 1) {
        return <div key={key} style={style} />;
      }

      return (
        <div key={key} style={style}>
          <Element
            element={results[index]}
            active={active}
            urlFactory={urlFactory}
            toggleStarFactory={toggleStarFactory}
          />
        </div>
      );
    },
    [results, active, urlFactory],
  );

  const [scrollToIndex, scrollToAlignment] = React.useMemo(() => {
    if (jumpTo) {
      return [jumpTo, 'start'];
    }
    if (active) {
      // TODO: Perhaps construct a map of IDs to index for this sort of thing.
      return [results.findIndex((elem) => elem.id === active), 'center'];
    }
    return [undefined, 'center'];
  }, [jumpTo, active, results]);

  return (
    <AutoSizer>
      {({ width, height }): React.ReactNode => (
        <List
          className={clsx('chooser', active && 'pt-8')}
          height={height}
          overscanRowCount={8}
          rowCount={results.length + 2}
          rowHeight={28.5}
          rowRenderer={renderRow}
          scrollToIndex={scrollToIndex}
          scrollToAlignment={scrollToAlignment as 'start' | 'auto'}
          width={width}
        />
      )}
    </AutoSizer>
  );
};

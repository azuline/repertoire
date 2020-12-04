import clsx from 'clsx';
import * as React from 'react';
import { AutoSizer, List, ListRowRenderer } from 'react-virtualized';
import { convertRemToPixels } from 'src/util';

import { Element, ElementT, ToggleStarFactory } from './Element';

export const VirtualList: React.FC<{
  active: number | null;
  jumpTo: number | null;
  results: ElementT[];
  starrable?: boolean;
  toggleStarFactory: ToggleStarFactory;
  urlFactory: (arg0: number) => string;
}> = ({ results, active, jumpTo, urlFactory, starrable, toggleStarFactory }) => {
  const renderRow: ListRowRenderer = ({ index, key, style }) => {
    // Because React-Virtualized has bungled scrollToIndex behavior when the
    // containing div has margin/padding, we replaced the margin/padding with
    // these blank elements on the bottom.
    if (index === results.length || index === results.length + 1) {
      return <div key={key} style={style} />;
    }

    return (
      <div key={key} style={style}>
        <Element
          active={active}
          element={results[index]}
          starrable={starrable}
          toggleStarFactory={toggleStarFactory}
          urlFactory={urlFactory}
        />
      </div>
    );
  };

  const rowHeight = convertRemToPixels(2);

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
          rowCount={results.length + (active ? 2 : 1)}
          rowHeight={rowHeight}
          rowRenderer={renderRow}
          scrollToAlignment={scrollToAlignment as 'start' | 'auto'}
          scrollToIndex={scrollToIndex}
          width={width}
        />
      )}
    </AutoSizer>
  );
};

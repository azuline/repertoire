import * as React from 'react';
import { AutoSizer, List, ListRowRenderer } from 'react-virtualized';

import { convertRemToPixels } from '~/util';

import { IElement } from './types';

type IVirtualList = React.FC<{
  active: number | null;
  jumpTo: number | null;
  results: IElement[];
  renderElement: (index: number) => React.ReactNode;
}>;

export const VirtualList: IVirtualList = ({
  results,
  active,
  jumpTo,
  renderElement,
}) => {
  const renderRow: ListRowRenderer = ({ index, key, style }) => {
    // Because React-Virtualized has bungled scrollToIndex behavior when the
    // containing div has margin/padding, we replaced the margin/padding with
    // these blank elements on the bottom.
    if (index === results.length || index === results.length + 1) {
      return <div key={key} style={style} />;
    }

    return (
      <div key={key} style={style}>
        {renderElement(index)}
      </div>
    );
  };

  const rowHeight = convertRemToPixels(2);

  const [scrollToIndex, scrollToAlignment] = React.useMemo(() => {
    if (jumpTo !== null) {
      return [jumpTo, 'start'];
    }
    if (active !== null) {
      // TODO(perf): Perhaps construct a map of IDs to index for this sort of thing.
      return [results.findIndex((elem) => elem.id === active), 'center'];
    }
    return [undefined, 'center'];
  }, [jumpTo, active, results]);

  return (
    <AutoSizer>
      {({ width, height }): React.ReactNode => (
        <List
          height={height}
          overscanRowCount={8}
          rowCount={results.length + 2}
          rowHeight={rowHeight}
          rowRenderer={renderRow}
          scrollToAlignment={scrollToAlignment as 'start' | 'auto'}
          scrollToIndex={scrollToIndex}
          tw="pt-8"
          width={width}
        />
      )}
    </AutoSizer>
  );
};

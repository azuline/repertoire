import * as React from 'react';
import { AutoSizer, List, ListRowRenderer } from 'react-virtualized';
import tw from 'twin.macro';

import { convertRemToPixels } from '~/util';

import { Element, IElement, IToggleStarFactory } from './Element';

type IVirtualList = React.FC<{
  active: number | null;
  jumpTo: number | null;
  results: IElement[];
  starrable?: boolean;
  toggleStarFactory: IToggleStarFactory;
  urlFactory: (arg0: number) => string;
}>;

export const VirtualList: IVirtualList = ({
  results,
  active,
  jumpTo,
  urlFactory,
  starrable,
  toggleStarFactory,
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
          css={active !== null && tw`pt-8`}
          height={height}
          overscanRowCount={8}
          rowCount={results.length + (active !== null ? 2 : 1)}
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

import { CollectionsContext, FilterContext, SortContext } from 'contexts';
import { List, WindowScroller } from 'react-virtualized';
import React, { useCallback, useContext, useMemo, useRef } from 'react';
import { name, random, recentlyUpdated, releaseCount } from 'common/sorts';

import { Collection } from './Collection';
import { collectionTypeNamesToIds } from 'common/collections';

const sortFunctions = { recentlyUpdated, name, releaseCount, random };

export const Collections = () => {
  const { asc, sortField } = useContext(SortContext);
  const { filter, selection: collectionType } = useContext(FilterContext);
  const { collections, fuse } = useContext(CollectionsContext);

  // Filter the collections based on the context.
  const filteredCollections = useMemo(() => {
    // Filter collections by fuzzy-search, if there is a filter....
    let results = filter ? fuse.search(filter).map(({ item }) => item) : collections;

    // Filter by the collection type.
    results = results.filter((collection) => {
      switch (collectionType) {
        case 'All':
          return true;
        case 'Favorite':
          return collection.favorite;
        default:
          return collection.type === collectionTypeNamesToIds[collectionType];
      }
    });

    // Sort collections based on the sort context.
    if (!filter || sortField !== 'fuzzyScore') {
      results.sort(sortFunctions[sortField]);
    }
    if (!asc) results.reverse();

    // And return!
    return results;
  }, [collections, fuse, asc, sortField, filter, collectionType]);

  // Virtual render setup.
  const scrollRef = useRef();

  const renderRow = useCallback(
    ({ index, key, style }) => {
      return (
        <div key={key} style={style}>
          <Collection collection={filteredCollections[index]} />
        </div>
      );
    },
    [filteredCollections]
  );

  return (
    <div className="Collections">
      <WindowScroller ref={scrollRef}>
        {({ height, width, isScrolling, onChildScroll, scrollTop }) => (
          <List
            autoHeight
            height={height}
            isScrolling={isScrolling}
            onScroll={onChildScroll}
            overscanRowCount={8}
            rowCount={filteredCollections.length}
            rowHeight={46}
            rowRenderer={renderRow}
            scrollTop={scrollTop}
            width={width}
          />
        )}
      </WindowScroller>
    </div>
  );
};

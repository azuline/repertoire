import { CollectionsContext, FilterContext, SortContext } from 'contexts';
import React, { useContext, useMemo } from 'react';

import { Collection } from './Collection';
import { collectionTypeNamesToIds } from 'common/collections';
import { name, random, recentlyUpdated, releaseCount } from 'common/sorts';
import { useVirtual } from 'react-virtual';

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
  const parentRef = React.useRef();
  const rowVirtualizer = useVirtual({
    size: filteredCollections.length,
    parentRef,
    estimateSize: React.useCallback(() => 46, []),
    overscan: 5,
  });

  return (
    <div className="Collections" ref={parentRef}>
      <div className="Virtual" style={{ height: `${rowVirtualizer.totalSize}px` }}>
        {rowVirtualizer.virtualItems.map((virtualRow) => (
          <div
            key={virtualRow.index}
            className="VirtualRow"
            style={{ height: '46px', transform: `translateY(${virtualRow.start}px)` }}
          >
            <Collection collection={filteredCollections[virtualRow.index]} />
          </div>
        ))}
      </div>
    </div>
  );
};

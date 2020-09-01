import { FilterContext, QueriesContext, SortContext } from 'contexts';
import { AutoSizer, List, WindowScroller } from 'react-virtualized';
import React, { useCallback, useContext, useMemo, useRef } from 'react';
import { name, random, recentlyAdded, releaseCount } from 'common/sorts';

import { Query } from './Query';

const sortFunctions = { recentlyAdded, name, releaseCount, random };

export const Queries = () => {
  const { asc, sortField } = useContext(SortContext);
  const { filter, selection: queryType } = useContext(FilterContext);
  const { queries, fuse } = useContext(QueriesContext);

  // Filter the queries based on the context.
  const filteredQueries = useMemo(() => {
    // Filter queries by fuzzy-search, if there is a filter....
    let results = filter ? fuse.search(filter).map(({ item }) => item) : queries;

    // Filter by the query type.
    results = results.filter((query) => {
      // Filter by type...
      switch (queryType) {
        case 'Favorite':
          return query.favorite;
        case 'All':
        default:
          return true;
      }
    });

    // Sort queries based on the sort context.
    if (!filter || sortField !== 'fuzzyScore') {
      results.sort(sortFunctions[sortField]);
    }
    if (!asc) results.reverse();

    // And return!
    return results;
  }, [queries, fuse, asc, sortField, filter, queryType]);

  // Virtual render setup.
  const scrollRef = useRef();

  const renderRow = useCallback(
    ({ index, key, style }) => {
      return (
        <div key={key} style={style}>
          <Query query={filteredQueries[index]} />
        </div>
      );
    },
    [filteredQueries]
  );

  return (
    <div className="Queries">
      <AutoSizer disableHeight>
        {({ width }) => (
          <WindowScroller ref={scrollRef}>
            {({ height, isScrolling, onChildScroll, scrollTop }) => (
              <List
                autoHeight
                height={height}
                isScrolling={isScrolling}
                onScroll={onChildScroll}
                overscanRowCount={8}
                rowCount={filteredQueries.length}
                rowHeight={46}
                rowRenderer={renderRow}
                scrollTop={scrollTop}
                width={width}
              />
            )}
          </WindowScroller>
        )}
      </AutoSizer>
    </div>
  );
};

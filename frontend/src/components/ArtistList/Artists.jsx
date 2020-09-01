import { ArtistsContext, FilterContext, SortContext } from 'contexts';
import { AutoSizer, List, WindowScroller } from 'react-virtualized';
import React, { useCallback, useContext, useMemo, useRef } from 'react';
import { name, random, releaseCount } from 'common/sorts';

import { Artist } from './Artist';

const sortFunctions = { name, releaseCount, random };

export const Artists = () => {
  const { asc, sortField } = useContext(SortContext);
  const { filter, selection: artistType } = useContext(FilterContext);
  const { artists, fuse } = useContext(ArtistsContext);

  // Filter artists based on the filter context.
  const filteredArtists = useMemo(() => {
    // Filter artists by fuzzy-search, if there is a filter....
    let results = filter ? fuse.search(filter).map(({ item }) => item) : artists;

    // Filter by the artist type.
    results = results.filter((artist) => {
      // Filter by type...
      switch (artistType) {
        case 'Favorite':
          return artist.favorite;
        case 'All':
        default:
          return true;
      }
    });

    // Sort artists based on the sort context.
    if (!filter || sortField !== 'fuzzyScore') {
      results.sort(sortFunctions[sortField]);
    }
    if (!asc) results.reverse();

    // And return!
    return results;
  }, [artists, fuse, asc, sortField, filter, artistType]);

  // Virtual render setup.
  const scrollRef = useRef();

  const renderRow = useCallback(
    ({ index, key, style }) => {
      return (
        <div key={key} style={style}>
          <Artist artist={filteredArtists[index]} />
        </div>
      );
    },
    [filteredArtists]
  );

  return (
    <div className="Artists">
      <AutoSizer disableHeight>
        {({ width }) => (
          <WindowScroller ref={scrollRef}>
            {({ height, width, isScrolling, onChildScroll, scrollTop }) => (
              <List
                autoHeight
                height={height}
                isScrolling={isScrolling}
                onScroll={onChildScroll}
                overscanRowCount={8}
                rowCount={filteredArtists.length}
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

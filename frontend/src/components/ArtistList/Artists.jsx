import { ArtistsContext, FilterContext, SortContext } from 'contexts';
import React, { useContext, useMemo } from 'react';
import { name, random, releaseCount } from 'common/sorts';

import { Artist } from './Artist';
import { useVirtual } from 'react-virtual';

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
  const parentRef = React.useRef();
  const rowVirtualizer = useVirtual({
    size: filteredArtists.length,
    parentRef,
    estimateSize: React.useCallback(() => 46, []),
    overscan: 5,
  });

  return (
    <div className="Artists" ref={parentRef}>
      <div className="Virtual" style={{ height: `${rowVirtualizer.totalSize}px` }}>
        {rowVirtualizer.virtualItems.map((virtualRow) => (
          <div
            key={virtualRow.index}
            className="VirtualRow"
            style={{ height: '46px', transform: `translateY(${virtualRow.start}px)` }}
          >
            <Artist artist={filteredArtists[virtualRow.index]} />
          </div>
        ))}
      </div>
    </div>
  );
};

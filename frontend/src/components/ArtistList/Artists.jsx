import { ArtistsContext, FilterContext, SortContext } from 'contexts';
import React, { useContext, useMemo } from 'react';

import { Artist } from './Artist';

const sortFunctions = {
  Name: (one, two) => (one.name.toLowerCase() < two.name.toLowerCase() ? -1 : 1),
  Random: () => Math.random() - 0.5,
  'Release Count': (one, two) => one.numReleases - two.numReleases,
};

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
    if (!filter || sortField !== 'Fuzzy Score') {
      results.sort(sortFunctions[sortField]);
    }
    if (!asc) results.reverse();

    // And return!
    return results;
  }, [artists, fuse, asc, sortField, filter, artistType]);

  return (
    <div className="Artists">
      {filteredArtists.map((artist) => {
        return <Artist key={artist.id} artist={artist} />;
      })}
    </div>
  );
};

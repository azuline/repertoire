import { FilterContext, SortContext } from 'components/Contexts';
import React, { useContext, useMemo } from 'react';

import { Artist } from './Artist';
import { mockArtists } from 'mockData';

const sortFunctions = {
  1: (one, two) => (one.name.toLowerCase() < two.name.toLowerCase() ? -1 : 1),
  2: (one, two) => one.numReleases - two.numReleases,
  3: () => Math.random() - 0.5,
};

export const Artists = () => {
  const { asc, sortField } = useContext(SortContext);
  const { filter, selection } = useContext(FilterContext);

  // Remap `selection` to the thing it's selecting.
  const artistType = selection;

  // Filter artists based on the filter context.
  const artists = useMemo(() => {
    const results = mockArtists.filter((artist) => {
      try {
        // Filter by name...
        if (artist.name.search(new RegExp(filter)) === -1) {
          return false;
        }

        // Filter by type...
        switch (artistType) {
          case 'Favorite':
            return artist.favorite;
          case 'All':
          default:
            return true;
        }
      } catch (e) {
        return false;
      }
    });

    // Sort artists based on the sort context.
    results.sort(sortFunctions[sortField]);
    if (!asc) results.reverse();

    return results;
  }, [asc, sortField, filter, artistType]);

  return (
    <div className="Artists">
      {artists.map((artist) => {
        return <Artist key={artist.id} artist={artist} />;
      })}
    </div>
  );
};

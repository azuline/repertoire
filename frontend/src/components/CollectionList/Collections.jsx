import { FilterContext, SortContext } from 'components/Contexts';
import React, { useContext, useMemo } from 'react';

import { Collection } from './Collection';
import { collectionTypeNamesToIds } from 'common/collections';
import { mockCollections } from 'mockData';

const sortFunctions = {
  1: (one, two) => two.lastUpdatedOn - one.lastUpdatedOn,
  2: (one, two) => (one.name.toLowerCase() < two.name.toLowerCase() ? -1 : 1),
  3: (one, two) => one.numReleases - two.numReleases,
  4: () => Math.random() - 0.5,
};

export const Collections = () => {
  const { asc, sortField } = useContext(SortContext);
  const { filter, selection } = useContext(FilterContext);

  // Remap `selection` to the thing it's selecting.
  const collectionType = selection;

  // Filter the collections based on the context.
  const collections = useMemo(() => {
    const results = mockCollections.filter((collection) => {
      try {
        // Filter by the name.
        if (collection.name.search(new RegExp(filter)) === -1) {
          return false;
        }

        // Filter by the collection.
        switch (collectionType) {
          case 'All':
            return true;
          case 'Favorite':
            return collection.favorite;
          default:
            // One of the other collections...
            return collection.type === collectionTypeNamesToIds[collectionType];
        }
      } catch (e) {
        return false;
      }
    });

    // Sort collections based on the sort context.
    results.sort(sortFunctions[sortField]);
    if (!asc) results.reverse();

    return results;
  }, [asc, sortField, filter, collectionType]);

  return (
    <div className="Collections">
      {collections.map((collection) => {
        return <Collection key={collection.id} collection={collection} />;
      })}
    </div>
  );
};

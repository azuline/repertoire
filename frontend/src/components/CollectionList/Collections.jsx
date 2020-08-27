import { CollectionsContext, FilterContext, SortContext } from 'contexts';
import React, { useContext, useMemo } from 'react';

import { Collection } from './Collection';
import { collectionTypeNamesToIds } from 'common/collections';

const sortFunctions = {
  Name: (one, two) => (one.name.toLowerCase() < two.name.toLowerCase() ? -1 : 1),
  Random: () => Math.random() - 0.5,
  'Recently Updated': (one, two) => two.lastUpdatedOn - one.lastUpdatedOn,
  'Release Count': (one, two) => one.numReleases - two.numReleases,
};

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
    if (!filter || sortField !== 'Fuzzy Score') {
      results.sort(sortFunctions[sortField]);
    }
    if (!asc) results.reverse();

    // And return!
    return results;
  }, [collections, fuse, asc, sortField, filter, collectionType]);

  return (
    <div className="Collections">
      {filteredCollections.map((collection) => {
        return <Collection key={collection.id} collection={collection} />;
      })}
    </div>
  );
};

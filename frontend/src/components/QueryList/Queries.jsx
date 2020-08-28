import React, { useContext, useMemo } from 'react';
import { Query } from './Query';
import { FilterContext, QueriesContext, SortContext } from 'contexts';

const sortFunctions = {
  Name: (one, two) => (one.name.toLowerCase() < two.name.toLowerCase() ? -1 : 1),
  Random: () => Math.random() - 0.5,
  recentlyAdded: (one, two) => two.addedOn - one.addedOn,
  releaseCount: (one, two) => one.numReleases - two.numReleases,
};

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

  return (
    <div className="Queries">
      {filteredQueries.map((query) => (
        <Query key={query.id} query={query} />
      ))}
    </div>
  );
};

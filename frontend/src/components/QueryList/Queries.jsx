import { FilterContext, QueriesContext, SortContext } from 'contexts';
import React, { useContext, useMemo } from 'react';

import { Query } from './Query';
import { recentlyAdded, name, releaseCount, random } from 'common/sorts';

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

  return (
    <div className="Queries">
      {filteredQueries.map((query) => (
        <Query key={query.id} query={query} />
      ))}
    </div>
  );
};
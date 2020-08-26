import React, { useMemo } from 'react';

import { Button } from '@blueprintjs/core';
import { CollectionTag } from 'components/common/CollectionTag';
import { collectionTypeIdsToNamesPlural } from 'common/collections';

export const ReleaseCollections = ({ collections }) => {
  // Generate a map of collection type => list of collections of that type.
  // ideally, this data-massaging would be done at a higher level before we
  // pass it to this component - probably married to data-fetching logic
  const collectionsByType = useMemo(
    () =>
      collections.reduce(
        (map, col) => {
          const colList = map[collectionTypeIdsToNamesPlural[col.type]];
          if (colList) {
            colList.push(col);
          }
          return map;
        },
        { Collages: [], Genres: [], Labels: [] }
      ),
    [collections]
  );

  return (
    <div className="ReleaseCollections">
      {Object.entries(collectionsByType).map(
        ([type, collections]) =>
          collections.length > 0 && (
            <div key={type} className="ReleaseCollection">
              <Button className="CollectionType" minimal disabled text={type} />
              <div className="CollectionTags">
                {collections.map((col) => (
                  <CollectionTag key={col.name} collection={col} />
                ))}
              </div>
            </div>
          )
      )}
    </div>
  );
};

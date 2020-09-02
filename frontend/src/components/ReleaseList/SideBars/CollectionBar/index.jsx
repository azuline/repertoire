import React, { useCallback, useState, useMemo, useContext } from 'react';
import { SearchContext, CollectionsContext } from 'contexts';
import { Type } from './Type';
import { Card } from '@blueprintjs/core';

const typeRankings = [1, 2, 4, 3];

const sortTypes = ([a], [b]) => typeRankings.indexOf(a) - typeRankings.indexOf(b);

export const CollectionBar = ({ hidden }) => {
  const [collapsedTypes, setCollapsedTypes] = useState([]);
  const { collections } = useContext(CollectionsContext);
  const { collections: activeCollections } = useContext(SearchContext);

  const collectionsByType = useMemo(() => {
    const types = collections.reduce((accumulator, collection) => {
      accumulator[collection.type] = accumulator[collection.type] ?? [];
      accumulator[collection.type].push(collection);
      return accumulator;
    }, {});

    const entries = Object.entries(types);
    entries.sort(sortTypes);
    return entries;
  }, [collections]);

  const toggleCollapsedType = useCallback(
    (type) =>
      setCollapsedTypes((types) => {
        const index = types.indexOf(type);
        if (index !== -1) {
          return [...types.slice(0, index), ...types.slice(index + 1)];
        } else {
          return [...types, type];
        }
      }),
    [setCollapsedTypes]
  );

  return (
    <Card className={'SideBar CollectionBar' + (hidden ? ' Hidden' : '')}>
      <Card className="SideBarHeader">Collections</Card>
      {collectionsByType.map(([type, typeCollections]) => (
        <Type
          key={type}
          type={type}
          collections={typeCollections}
          collapsedTypes={collapsedTypes}
          toggleCollapsedType={toggleCollapsedType}
          activeCollections={activeCollections}
        />
      ))}
    </Card>
  );
};

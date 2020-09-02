import React, { useMemo } from 'react';
import { Icon, Card } from '@blueprintjs/core';
import { collectionTypeIdsToNamesPlural } from 'common/collections';
import { Entry } from './Entry';

export const Type = ({
  type,
  collections,
  activeCollections,
  collapsedTypes,
  toggleCollapsedType,
}) => {
  const collapsed = useMemo(() => {
    return collapsedTypes.includes(type);
  }, [type, collapsedTypes]);

  return (
    <>
      <Card className="TypeHeading" onClick={() => toggleCollapsedType(type)}>
        <Icon icon={collapsed ? 'chevron-right' : 'chevron-down'} />
        {collectionTypeIdsToNamesPlural[type]}
      </Card>
      {!collapsed &&
        collections.map((collection) => (
          <Entry
            key={collection.id}
            collection={collection}
            activeCollections={activeCollections}
          />
        ))}
    </>
  );
};

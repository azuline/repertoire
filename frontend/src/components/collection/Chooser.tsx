import * as React from 'react';
import { Chooser, ToggleStarFactory } from 'src/components/Chooser';
import { useFetchCollections, useMutateCollection } from 'src/lib';
import { CollectionType } from 'src/types';

export const CollectionChooser: React.FC<{
  collectionTypes: CollectionType[];
  urlPrefix: string;
  active: number | null;
  className?: string;
}> = ({ collectionTypes, urlPrefix, active, className }) => {
  const { data, error, loading } = useFetchCollections(collectionTypes);
  const [mutateCollection] = useMutateCollection();

  const urlFactory = (id: number): string => `${urlPrefix}/${id}`;

  const toggleStarFactory: ToggleStarFactory = ({ id, starred, type }) => {
    if (type === 'SYSTEM') return;

    return async (): Promise<void> => {
      mutateCollection({ variables: { id, starred: !starred } });
    };
  };

  if (!data || loading || error) return null;

  return (
    <Chooser
      active={active}
      className={className}
      results={data.collections.results}
      toggleStarFactory={toggleStarFactory}
      urlFactory={urlFactory}
    />
  );
};

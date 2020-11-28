import * as React from 'react';
import { Chooser, ElementT } from 'src/components/Chooser';
import { fetchCollections, useMutateCollection } from 'src/lib';
import { CollectionType } from 'src/types';

export const CollectionChooser: React.FC<{
  collectionTypes: CollectionType[];
  urlPrefix: string;
  active: number | null;
  className?: string;
}> = ({ collectionTypes, urlPrefix, active, className }) => {
  const { data, error, loading } = fetchCollections(collectionTypes);
  const [mutateCollection] = useMutateCollection();

  const urlFactory = React.useCallback((id: number): string => `${urlPrefix}/${id}`, [urlPrefix]);

  const toggleStarFactory = React.useCallback(
    ({ id, starred }: ElementT) => async (): Promise<void> => {
      mutateCollection({ variables: { id, starred: !starred } });
    },
    [mutateCollection],
  );

  if (!data || loading || error) return null;

  return (
    <Chooser
      className={className}
      results={data.collections.results}
      active={active}
      urlFactory={urlFactory}
      toggleStarFactory={toggleStarFactory}
    />
  );
};

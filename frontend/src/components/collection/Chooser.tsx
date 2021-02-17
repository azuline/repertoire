import * as React from 'react';

import { Chooser, IToggleStarFactory } from '~/components/Chooser';
import {
  ICollection,
  ICollectionType,
  useFetchCollectionsQuery,
  useUpdateCollectionStarredMutation,
} from '~/graphql';

type ICollectionChooser = React.FC<{
  collectionTypes: ICollectionType[];
  urlPrefix: string;
  active: number | null;
  className?: string;
}>;

export const CollectionChooser: ICollectionChooser = ({
  collectionTypes,
  urlPrefix,
  active,
  className,
}) => {
  const { data, error, loading } = useFetchCollectionsQuery({
    variables: { types: collectionTypes },
  });
  const [mutateCollection] = useUpdateCollectionStarredMutation();

  const urlFactory = (id: number): string => `${urlPrefix}/${id}`;

  const toggleStarFactory: IToggleStarFactory = ({ id, starred, type }) => {
    if (type === 'SYSTEM') return;

    return async (): Promise<void> => {
      mutateCollection({ variables: { id, starred: !starred } });
    };
  };

  if (!data || !data.collections || loading || error) return null;

  return (
    <Chooser
      active={active}
      className={className}
      results={data.collections.results as ICollection[]}
      toggleStarFactory={toggleStarFactory}
      urlFactory={urlFactory}
    />
  );
};

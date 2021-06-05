import { gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Chooser, NoChooserOption } from '~/components/Chooser';
import { StarrableChooserRow } from '~/components/ChooserRow';
import {
  ICollectionFieldsFragment,
  ICollectionType,
  useFetchCollectionsChooserQuery,
  useStarCollectionChooserMutation,
  useUnstarCollectionChooserMutation,
} from '~/graphql';
import { compareByStarThenName } from '~/util';

type ICollectionChooser = React.FC<{
  collectionTypes: ICollectionType[];
  urlPrefix: string;
  active: number | null;
  className?: string;
  emptyString: string;
  filterEmpty?: boolean;
}>;

export const CollectionChooser: ICollectionChooser = ({
  collectionTypes,
  urlPrefix,
  active,
  className,
  emptyString,
  filterEmpty = false,
}) => {
  const { data, error, loading } = useFetchCollectionsChooserQuery({
    variables: { types: collectionTypes },
  });
  const [starCollection] = useStarCollectionChooserMutation();
  const [unstarCollection] = useUnstarCollectionChooserMutation();
  const { addToast } = useToasts();

  const toggleStar = async (collection: ICollectionFieldsFragment): Promise<void> => {
    if (collection.type === 'SYSTEM') {
      addToast('Cannot unstar system collections.', { appearance: 'error' });
      return;
    }

    if (collection.starred) {
      await unstarCollection({ variables: { id: collection.id } });
    } else {
      await starCollection({ variables: { id: collection.id } });
    }
  };

  if (!data || loading || error) {
    return null;
  }

  const collections = ((): ICollectionFieldsFragment[] => {
    const xs = filterEmpty
      ? data.collections.results.filter((col) => col.numReleases !== 0)
      : data.collections.results;

    return xs
      .map((c) =>
        c.user === null ? c : { ...c, name: `${c.user.nickname}'s ${c.name}` },
      )
      .sort(compareByStarThenName);
  })();

  const renderElement = (index: number): React.ReactNode => {
    const element = collections[index];

    return (
      <StarrableChooserRow
        element={element}
        isActive={element.id === active}
        url={`${urlPrefix}/${element.id}`}
        onToggle={(): Promise<void> => toggleStar(element)}
      />
    );
  };

  if (collections.length === 0) {
    return <NoChooserOption>No {emptyString} :(</NoChooserOption>;
  }

  return (
    <Chooser
      active={active}
      className={className}
      renderElement={renderElement}
      results={collections}
    />
  );
};

/* eslint-disable */
gql`
  query FetchCollectionsChooser($types: [CollectionType!]) {
    collections(types: $types) {
      results {
        ...CollectionFields
      }
    }
  }

  mutation StarCollectionChooser($id: Int!) {
    starCollection(id: $id) {
      id
      starred
    }
  }

  mutation UnstarCollectionChooser($id: Int!) {
    unstarCollection(id: $id) {
      id
      starred
    }
  }
`;

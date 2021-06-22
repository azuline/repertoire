import { gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import tw from 'twin.macro';

import { Icon } from '~/components';
import {
  IRelease,
  useInFavoritesAddReleaseToCollectionMutation,
  useInFavoritesDelReleaseFromCollectionMutation,
  useInFavoritesFetchFavoritesIdQuery,
} from '~/graphql';

type IInFavorites = React.FC<{
  className?: string;
  release: Pick<IRelease, 'id' | 'inFavorites'>;
}>;

export const InFavorites: IInFavorites = ({ className, release }) => {
  const { addToast } = useToasts();

  const { data } = useInFavoritesFetchFavoritesIdQuery();
  const [mutateAdd] = useInFavoritesAddReleaseToCollectionMutation();
  const [mutateDel] = useInFavoritesDelReleaseFromCollectionMutation();

  const toggleFavorite = async (): Promise<void> => {
    if (data === undefined) {
      addToast('Failed to fetch favorites.', { appearance: 'error' });
      return;
    }

    const toggleFunc = release.inFavorites ? mutateDel : mutateAdd;
    await toggleFunc({
      variables: {
        collectionId: data.user.favoritesCollectionId,
        releaseId: release.id,
      },
    });
  };

  return (
    <Icon
      className={className}
      css={[
        tw`w-8 cursor-pointer`,
        release.inFavorites
          ? tw`text-pink-500 hover:text-gray-500`
          : tw`text-gray-500 hover:text-pink-500`,
      ]}
      icon="heart-medium"
      title={release.inFavorites ? 'In favorites' : 'Not in favorites'}
      onClick={toggleFavorite}
    />
  );
};

gql`
  query InFavoritesFetchFavoritesId {
    user {
      id
      favoritesCollectionId
    }
  }

  mutation InFavoritesAddReleaseToCollection($collectionId: Int!, $releaseId: Int!) {
    addReleaseToCollection(collectionId: $collectionId, releaseId: $releaseId) {
      collection {
        id
        numReleases
        lastUpdatedOn
      }
      release {
        id
        inInbox
        inFavorites
        genres {
          id
          name
        }
        labels {
          id
          name
        }
        collages {
          id
          name
        }
      }
    }
  }

  mutation InFavoritesDelReleaseFromCollection($collectionId: Int!, $releaseId: Int!) {
    delReleaseFromCollection(collectionId: $collectionId, releaseId: $releaseId) {
      collection {
        id
        numReleases
        lastUpdatedOn
      }
      release {
        id
        inInbox
        inFavorites
        genres {
          id
          name
        }
        labels {
          id
          name
        }
        collages {
          id
          name
        }
      }
    }
  }
`;

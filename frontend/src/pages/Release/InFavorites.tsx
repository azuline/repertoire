import { gql } from '@apollo/client';
import * as React from 'react';
import tw from 'twin.macro';

import { Icon } from '~/components';
import {
  IRelease,
  useInFavoritesAddReleaseToCollectionMutation,
  useInFavoritesDelReleaseFromCollectionMutation,
} from '~/graphql';

const FAVORITES_COLLECTION_ID = 2;

type IInFavorites = React.FC<{ className?: string; release: IRelease }>;

export const InFavorites: IInFavorites = ({ className, release }) => {
  const [mutateAdd] = useInFavoritesAddReleaseToCollectionMutation();
  const [mutateDel] = useInFavoritesDelReleaseFromCollectionMutation();

  const toggleFavorite = async (): Promise<void> => {
    const toggleFunc = release.inFavorites ? mutateDel : mutateAdd;
    await toggleFunc({
      variables: { collectionId: FAVORITES_COLLECTION_ID, releaseId: release.id },
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

/* eslint-disable */
gql`
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

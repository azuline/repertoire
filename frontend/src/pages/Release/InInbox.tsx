import { gql } from '@apollo/client';
import * as React from 'react';
import tw from 'twin.macro';

import { Icon } from '~/components';
import {
  IRelease,
  useInInboxAddReleaseToCollectionMutation,
  useInInboxDelReleaseFromCollectionMutation,
} from '~/graphql';

const INBOX_COLLECTION_ID = 1;

type IInInbox = React.FC<{ className?: string; release: IRelease }>;

export const InInbox: IInInbox = ({ className, release }) => {
  const [mutateAdd] = useInInboxAddReleaseToCollectionMutation();
  const [mutateDel] = useInInboxDelReleaseFromCollectionMutation();

  const toggleInbox = (): void => {
    if (release.inInbox) {
      mutateDel({ variables: { collectionId: INBOX_COLLECTION_ID, releaseId: release.id } });
    } else {
      mutateAdd({ variables: { collectionId: INBOX_COLLECTION_ID, releaseId: release.id } });
    }
  };

  return (
    <Icon
      className={className}
      css={[
        tw`w-8 ml-2 cursor-pointer`,
        release.inInbox
          ? tw`text-blue-500 hover:text-gray-500`
          : tw`text-gray-500 hover:text-blue-500`,
      ]}
      icon="inbox-medium"
      title={release.inInbox ? 'In inbox' : 'Not in inbox'}
      onClick={toggleInbox}
    />
  );
};

/* eslint-disable */
gql`
  mutation InInboxAddReleaseToCollection($collectionId: Int!, $releaseId: Int!) {
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

  mutation InInboxDelReleaseFromCollection($collectionId: Int!, $releaseId: Int!) {
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

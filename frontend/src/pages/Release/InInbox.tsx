import { gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import tw from 'twin.macro';

import { Icon } from '~/components';
import {
  IRelease,
  useInInboxAddReleaseToCollectionMutation,
  useInInboxDelReleaseFromCollectionMutation,
  useInInboxFetchInboxIdQuery,
} from '~/graphql';

type IInInbox = React.FC<{
  className?: string;
  release: Pick<IRelease, 'id' | 'inInbox'>;
}>;

export const InInbox: IInInbox = ({ className, release }) => {
  const { addToast } = useToasts();

  const { data } = useInInboxFetchInboxIdQuery();
  const [mutateAdd] = useInInboxAddReleaseToCollectionMutation();
  const [mutateDel] = useInInboxDelReleaseFromCollectionMutation();

  const toggleInbox = async (): Promise<void> => {
    if (data === undefined) {
      addToast('Failed to fetch inbox.', { appearance: 'error' });
      return;
    }

    const toggleFunc = release.inInbox ? mutateDel : mutateAdd;
    await toggleFunc({
      variables: {
        collectionId: data.user.inboxCollectionId,
        releaseId: release.id,
      },
    });
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
  query InInboxFetchInboxId {
    user {
      inboxCollectionId
    }
  }

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

import * as React from 'react';
import tw from 'twin.macro';

import { Icon } from '~/components';
import {
  IRelease,
  useAddReleaseToCollectionMutation,
  useDelReleaseFromCollectionMutation,
} from '~/graphql';

const INBOX_COLLECTION_ID = 1;

type IInInbox = React.FC<{ className?: string; release: IRelease }>;

export const InInbox: IInInbox = ({ className, release }) => {
  const [mutateAdd] = useAddReleaseToCollectionMutation();
  const [mutateDel] = useDelReleaseFromCollectionMutation();

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
      css={[tw`w-8 ml-2 cursor-pointer`, release.inInbox ? tw`text-blue-500` : tw`text-gray-500`]}
      icon="inbox-medium"
      title={release.inInbox ? 'In inbox' : 'Not in inbox'}
      onClick={toggleInbox}
    />
  );
};

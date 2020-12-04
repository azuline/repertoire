import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components';
import { useAddReleaseToCollection, useDelReleaseFromCollection } from 'src/lib';
import { ReleaseT } from 'src/types';

const INBOX_COLLECTION_ID = 1;

export const InInbox: React.FC<{ className?: string; release: ReleaseT }> = ({
  className,
  release,
}) => {
  const [mutateAdd] = useAddReleaseToCollection();
  const [mutateDel] = useDelReleaseFromCollection();

  const toggleInbox = (): void => {
    if (release.inInbox) {
      mutateDel({ variables: { collectionId: INBOX_COLLECTION_ID, releaseId: release.id } });
    } else {
      mutateAdd({ variables: { collectionId: INBOX_COLLECTION_ID, releaseId: release.id } });
    }
  };

  return (
    <Icon
      className={clsx(
        className,
        'w-8 ml-2 cursor-pointer',
        release.inInbox ? 'text-blue-500' : 'text-gray-500',
      )}
      icon="inbox-medium"
      title={release.inInbox ? 'In inbox' : 'Not in inbox'}
      onClick={toggleInbox}
    />
  );
};

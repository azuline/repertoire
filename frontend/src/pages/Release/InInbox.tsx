import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components';
import { useAddReleaseToCollection, useDelReleaseFromCollection } from 'src/lib';
import { ReleaseT } from 'src/types';

const INBOX_COLLECTION_ID = 1;

export const InInbox: React.FC<{ release: ReleaseT }> = ({ release }) => {
  const [mutateAdd] = useAddReleaseToCollection();
  const [mutateDel] = useDelReleaseFromCollection();

  const toggleInbox = React.useCallback(() => {
    if (release.inInbox) {
      mutateDel({ variables: { releaseId: release.id, collectionId: INBOX_COLLECTION_ID } });
    } else {
      mutateAdd({ variables: { releaseId: release.id, collectionId: INBOX_COLLECTION_ID } });
    }
  }, [mutateAdd, mutateDel, release]);

  return (
    <Icon
      className={clsx(
        'ml-2 w-9 cursor-pointer',
        release.inInbox ? 'text-blue-400 dark:text-blue-600' : 'text-gray-400 dark:text-gray-600',
      )}
      icon="inbox-medium"
      title={release.inInbox ? 'In inbox' : 'Not in inbox'}
      onClick={toggleInbox}
    />
  );
};

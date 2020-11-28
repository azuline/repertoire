import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components';
import { useAddReleaseToCollection, useDelReleaseFromCollection } from 'src/lib';
import { ReleaseT } from 'src/types';

const FAVORITES_COLLECTION_ID = 2;

export const InFavorites: React.FC<{ release: ReleaseT }> = ({ release }) => {
  const [mutateAdd] = useAddReleaseToCollection();
  const [mutateDel] = useDelReleaseFromCollection();

  const toggleFavorite = React.useCallback(() => {
    if (release.inFavorites) {
      mutateDel({ releaseId: release.id, collectionId: FAVORITES_COLLECTION_ID });
    } else {
      mutateAdd({ releaseId: release.id, collectionId: FAVORITES_COLLECTION_ID });
    }
  }, [mutateAdd, mutateDel, release]);

  return (
    <Icon
      className={clsx(
        'w-9 cursor-pointer',
        release.inFavorites
          ? 'text-pink-400 dark:text-pink-600'
          : 'text-gray-400 dark:text-gray-600',
      )}
      icon="heart-medium"
      title={release.inFavorites ? 'In favorites' : 'Not in favorites'}
      onClick={toggleFavorite}
    />
  );
};

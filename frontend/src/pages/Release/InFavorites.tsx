import * as React from 'react';
import tw from 'twin.macro';

import { Icon } from '~/components';
import {
  IRelease,
  useAddReleaseToCollectionMutation,
  useDelReleaseFromCollectionMutation,
} from '~/graphql';

const FAVORITES_COLLECTION_ID = 2;

export const InFavorites: React.FC<{ className?: string; release: IRelease }> = ({
  className,
  release,
}) => {
  const [mutateAdd] = useAddReleaseToCollectionMutation();
  const [mutateDel] = useDelReleaseFromCollectionMutation();

  const toggleFavorite = (): void => {
    if (release.inFavorites) {
      mutateDel({ variables: { collectionId: FAVORITES_COLLECTION_ID, releaseId: release.id } });
    } else {
      mutateAdd({ variables: { collectionId: FAVORITES_COLLECTION_ID, releaseId: release.id } });
    }
  };

  return (
    <Icon
      className={className}
      css={[tw`w-8 cursor-pointer`, release.inFavorites ? tw`text-pink-500` : tw`text-gray-500`]}
      icon="heart-medium"
      title={release.inFavorites ? 'In favorites' : 'Not in favorites'}
      onClick={toggleFavorite}
    />
  );
};

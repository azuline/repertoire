import React from 'react';

import { PagedReleases } from '~/components/Releases';
import { usePagination, useViewOptions } from '~/hooks';

type ICollectionReleases = React.FC<{ active: number }>;

export const CollectionReleases: ICollectionReleases = ({ active }) => {
  const viewOptions = useViewOptions({ collectionIds: [active] });
  const pagination = usePagination();

  React.useEffect(() => viewOptions.setCollectionIds([active]), [active]);

  return <PagedReleases partial pagination={pagination} viewOptions={viewOptions} />;
};

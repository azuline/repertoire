import * as React from 'react';
import { PagedReleases } from 'src/components/Releases';
import { usePagination, useViewOptions } from 'src/hooks';

export const CollectionReleases: React.FC<{ active: number }> = ({ active }) => {
  const viewOptions = useViewOptions({ collectionIds: [active] });
  const pagination = usePagination();

  return <PagedReleases partial pagination={pagination} viewOptions={viewOptions} />;
};

import * as React from 'react';
import { PagedReleases } from 'src/components/Releases';
import { usePagination, useViewOptions } from 'src/hooks';

export const CollectionReleases: React.FC<{ active: number }> = ({ active }) => {
  const viewOptionsSeed = React.useMemo(() => ({ collectionIds: [active] }), [active]);
  const viewOptions = useViewOptions(viewOptionsSeed);
  const pagination = usePagination();

  return <PagedReleases partial pagination={pagination} viewOptions={viewOptions} />;
};

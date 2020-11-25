import * as React from 'react';

import { usePagination, useViewOptions } from 'src/hooks';

import { PagedReleases } from 'src/components';

export const ArtistReleases: React.FC<{ active: number }> = ({ active }) => {
  const viewOptionsSeed = React.useMemo(() => ({ artistIds: [active] }), [active]);
  const viewOptions = useViewOptions(viewOptionsSeed);
  const pagination = usePagination();

  return <PagedReleases viewOptions={viewOptions} pagination={pagination} partial />;
};

import * as React from 'react';
import { PagedReleases } from '~/components';
import { usePagination, useViewOptions } from '~/hooks';

export const ArtistReleases: React.FC<{ active: number }> = ({ active }) => {
  const viewOptions = useViewOptions({ artistIds: [active] });
  const pagination = usePagination();

  return <PagedReleases partial pagination={pagination} viewOptions={viewOptions} />;
};

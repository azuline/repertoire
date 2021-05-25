import * as React from 'react';

import { PagedReleases } from '~/components';
import { usePagination, useViewOptions } from '~/hooks';

type IArtistReleases = React.FC<{ active: number }>;

export const ArtistReleases: IArtistReleases = ({ active }) => {
  const viewOptions = useViewOptions({ artistIds: [active] });
  const pagination = usePagination();

  React.useEffect(() => viewOptions.setArtistIds([active]), [active, viewOptions]);

  return <PagedReleases partial pagination={pagination} viewOptions={viewOptions} />;
};

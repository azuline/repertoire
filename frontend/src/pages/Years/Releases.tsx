import * as React from 'react';
import { PagedReleases } from 'src/components';
import { usePagination, useViewOptions } from 'src/hooks';

export const YearReleases: React.FC<{ active: number }> = ({ active }) => {
  const viewOptionsSeed = React.useMemo(() => ({ years: [active] }), [active]);
  const viewOptions = useViewOptions(viewOptionsSeed);
  const pagination = usePagination();

  return <PagedReleases partial pagination={pagination} viewOptions={viewOptions} />;
};

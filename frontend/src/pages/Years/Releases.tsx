import * as React from 'react';

import { PagedReleases } from '~/components';
import { usePagination, useViewOptions } from '~/hooks';

type IYearReleases = React.FC<{ active: number }>;

export const YearReleases: IYearReleases = ({ active }) => {
  const viewOptions = useViewOptions({ years: [active] });
  const pagination = usePagination();

  React.useEffect(() => viewOptions.setYears([active]), [active, viewOptions]);

  return <PagedReleases partial pagination={pagination} viewOptions={viewOptions} />;
};

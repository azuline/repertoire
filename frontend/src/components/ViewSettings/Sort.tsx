import * as React from 'react';

import { ReleaseSort } from 'src/types';
import { Select } from 'src/components/common/Select';
import { ViewOptionsType } from 'src/hooks';

const displays: { [k in ReleaseSort]: string } = {
  [ReleaseSort.RECENTLY_ADDED]: 'Recently Added',
  [ReleaseSort.TITLE]: 'Title',
  [ReleaseSort.YEAR]: 'Year',
  [ReleaseSort.RANDOM]: 'Random',
};

export const Sort: React.FC<{ viewOptions: ViewOptionsType; className?: string }> = ({
  viewOptions,
  className,
}) => {
  // prettier-ignore
  const updateSort = React.useCallback(
    (e) => viewOptions.setSort(e.currentTarget.value),
    [viewOptions],
  );

  return (
    <Select
      className={className}
      value={viewOptions.sort}
      label="Sort"
      name="select-sort"
      onChange={updateSort}
    >
      {Object.values(ReleaseSort).map((value) => (
        <option key={value} value={value}>
          {displays[value]}
        </option>
      ))}
    </Select>
  );
};

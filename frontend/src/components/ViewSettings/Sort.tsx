import * as React from 'react';

import { RVOCType } from 'src/hooks';
import { ReleaseSort } from 'src/types';
import { Select } from 'src/components/common/Select';

const SortDisplay: { [k in ReleaseSort]: string } = {
  [ReleaseSort.RECENTLY_ADDED]: 'Recently Added',
  [ReleaseSort.TITLE]: 'Title',
  [ReleaseSort.YEAR]: 'Year',
  [ReleaseSort.RANDOM]: 'Random',
};

export const Sort: React.FC<{ viewOptions: RVOCType; className?: string }> = ({
  viewOptions,
  className = '',
}) => {
  const updateSort = React.useCallback((e) => viewOptions.setSort(e.currentTarget.value), [
    viewOptions,
  ]);

  return (
    <Select className={className} label="Sort" onChange={updateSort}>
      {Object.values(ReleaseSort).map((value) => (
        <option key={value} value={value} selected={value === viewOptions.sort}>
          {SortDisplay[value]}
        </option>
      ))}
    </Select>
  );
};

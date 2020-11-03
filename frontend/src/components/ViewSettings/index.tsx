import * as React from 'react';
import clsx from 'clsx';
import { RVOCType } from 'src/hooks';
import { ReleaseSort } from 'src/types';
import { Select } from 'src/components/common/Select';

const SortDisplay: { [k in ReleaseSort]: string } = {
  [ReleaseSort.RECENTLY_ADDED]: 'Recently Added',
  [ReleaseSort.TITLE]: 'Title',
  [ReleaseSort.YEAR]: 'Year',
  [ReleaseSort.RANDOM]: 'Random',
};

export const ViewSettings: React.FC<{ viewOptions: RVOCType; className?: string }> = ({
  viewOptions,
  className = '',
}) => {
  const updateSort = React.useCallback((e) => viewOptions.setSort(e.currentTarget.value), [
    viewOptions,
  ]);
  const updateOrder = React.useCallback(
    (e) => viewOptions.setAsc(e.currentTarget.value === 'true'),
    [viewOptions],
  );

  return (
    <div className={clsx('flex justify-center', className)}>
      <Select label="Sort" onChange={updateSort}>
        {Object.values(ReleaseSort).map((value) => (
          <option key={value} value={value} selected={value === viewOptions.sort}>
            {SortDisplay[value]}
          </option>
        ))}
      </Select>
      <Select label="Order" onChange={updateOrder} className="ml-4">
        <option value="true" selected={viewOptions.asc}>
          Asc
        </option>
        <option value="false" selected={!viewOptions.asc}>
          Desc
        </option>
      </Select>
    </div>
  );
};

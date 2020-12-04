import * as React from 'react';
import { Select } from 'src/components/common';
import { ViewOptionsT } from 'src/hooks';
import { ReleaseSort } from 'src/types';

const displays: { [k in ReleaseSort]: string } = {
  [ReleaseSort.RECENTLY_ADDED]: 'Recently Added',
  [ReleaseSort.TITLE]: 'Title',
  [ReleaseSort.YEAR]: 'Year',
  [ReleaseSort.RATING]: 'Rating',
  [ReleaseSort.RANDOM]: 'Random',
};

export const Sort: React.FC<{ viewOptions: ViewOptionsT; className?: string }> = ({
  viewOptions,
  className,
}) => {
  const updateSort = (e: React.FormEvent<HTMLSelectElement>): void =>
    viewOptions.setSort(e.currentTarget.value as ReleaseSort);

  return (
    <Select
      className={className}
      label="Sort"
      name="select-sort"
      value={viewOptions.sort}
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

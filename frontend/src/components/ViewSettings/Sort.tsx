import * as React from 'react';

import { Select } from '~/components/common';
import { IReleaseSort } from '~/graphql';
import { IViewOptions } from '~/hooks';

const displays: { [k in IReleaseSort]: string } = {
  [IReleaseSort.RecentlyAdded]: 'Recently Added',
  [IReleaseSort.Title]: 'Title',
  [IReleaseSort.Year]: 'Year',
  [IReleaseSort.Rating]: 'Rating',
  [IReleaseSort.Random]: 'Random',
};

export const Sort: React.FC<{ viewOptions: IViewOptions; className?: string }> = ({
  viewOptions,
  className,
}) => {
  const updateSort = (e: React.FormEvent<HTMLSelectElement>): void =>
    viewOptions.setSort(e.currentTarget.value as IReleaseSort);

  return (
    <Select
      className={className}
      label="Sort"
      name="select-sort"
      value={viewOptions.sort}
      onChange={updateSort}
    >
      {Object.values(IReleaseSort).map((value) => (
        <option key={value} value={value}>
          {displays[value]}
        </option>
      ))}
    </Select>
  );
};

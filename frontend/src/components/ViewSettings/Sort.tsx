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
  [IReleaseSort.SearchRank]: 'Relevance',
};

type ISort = React.FC<{ viewOptions: IViewOptions; className?: string }>;

export const Sort: ISort = ({ viewOptions, className }) => {
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
      {Object.entries(displays)
        .filter(([k]) => k !== IReleaseSort.SearchRank)
        .map(([k, display]) => (
          <option key={k} value={k}>
            {display}
          </option>
        ))}
    </Select>
  );
};

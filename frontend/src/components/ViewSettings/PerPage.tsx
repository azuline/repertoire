import * as React from 'react';

import { Select } from '~/components/common';
import { PaginationT } from '~/hooks';

const options = [40, 80, 120, 160, 200];

export const PerPage: React.FC<{ pagination: PaginationT; className?: string }> = ({
  pagination,
  className,
}) => {
  const updatePerPage = (e: React.FormEvent<HTMLSelectElement>): void =>
    pagination.setPerPage(parseInt(e.currentTarget.value, 10));

  return (
    <Select
      className={className}
      label="Per Page"
      name="select-perPage"
      value={pagination.perPage}
      onChange={updatePerPage}
    >
      {options.map((value) => (
        <option key={value} value={value}>
          {value}
        </option>
      ))}
    </Select>
  );
};

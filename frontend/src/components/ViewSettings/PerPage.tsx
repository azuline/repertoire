import * as React from 'react';
import { Select } from 'src/components/common';
import { PaginationT } from 'src/hooks';

const options = [40, 80, 120, 160, 200];

export const PerPage: React.FC<{ pagination: PaginationT; className?: string }> = ({
  pagination,
  className,
}) => {
  const updatePerPage = React.useCallback(
    (e) => pagination.setPerPage(parseInt(e.currentTarget.value, 10)),
    [pagination],
  );

  return (
    <Select
      className={className}
      value={pagination.perPage}
      label="Per Page"
      name="select-perPage"
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

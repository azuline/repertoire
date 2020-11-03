import * as React from 'react';
import { Select } from 'src/components/common/Select';
import { PCType } from 'src/hooks';

const options = [10, 25, 50, 100, 200];

export const PerPage: React.FC<{ pagination: PCType; className?: string }> = ({
  pagination,
  className = '',
}) => {
  const updatePerPage = React.useCallback(
    (e) => pagination.setPerPage(parseInt(e.currentTarget.value)),
    [pagination],
  );

  return (
    <Select className={className} label="Per Page" onChange={updatePerPage}>
      {options.map((value) => (
        <option key={value} value={value} selected={value === pagination.perPage}>
          {value}
        </option>
      ))}
    </Select>
  );
};

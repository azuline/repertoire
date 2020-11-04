import * as React from 'react';

import { PCType } from 'src/hooks';
import { Select } from 'src/components/common/Select';

const options = [25, 50, 100, 200];

export const PerPage: React.FC<{ pagination: PCType; className?: string }> = ({
  pagination,
  className = '',
}) => {
  const updatePerPage = React.useCallback(
    (e) => pagination.setPerPage(parseInt(e.currentTarget.value)),
    [pagination],
  );

  return (
    <Select className={className} label="Per Page" name="select-perPage" onChange={updatePerPage}>
      {options.map((value) => (
        <option key={value} value={value} selected={value === pagination.perPage}>
          {value}
        </option>
      ))}
    </Select>
  );
};

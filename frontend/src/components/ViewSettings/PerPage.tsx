import * as React from 'react';

import { PaginationType } from 'src/hooks';
import { Select } from 'src/components/common/Select';

const options = [40, 80, 120, 160, 200];

export const PerPage: React.FC<{ pagination: PaginationType; className?: string | undefined }> = ({
  pagination,
  className,
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

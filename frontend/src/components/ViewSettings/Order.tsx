import * as React from 'react';
import { Select } from 'src/components/common/Select';
import { RVOCType } from 'src/hooks';

export const Order: React.FC<{ viewOptions: RVOCType; className?: string }> = ({
  viewOptions,
  className = '',
}) => {
  const updateOrder = React.useCallback(
    (e) => viewOptions.setAsc(e.currentTarget.value === 'true'),
    [viewOptions],
  );

  return (
    <Select label="Order" onChange={updateOrder} className={className}>
      <option value="true" selected={viewOptions.asc}>
        Asc
      </option>
      <option value="false" selected={!viewOptions.asc}>
        Desc
      </option>
    </Select>
  );
};

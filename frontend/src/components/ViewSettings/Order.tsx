import * as React from 'react';
import { Select } from 'src/components/common';
import { ViewOptionsType } from 'src/hooks';

export const Order: React.FC<{ viewOptions: ViewOptionsType; className?: string }> = ({
  viewOptions,
  className,
}) => {
  const updateOrder = React.useCallback(
    (e) => viewOptions.setAsc(e.currentTarget.value === 'true'),
    [viewOptions],
  );

  return (
    <Select
      onChange={updateOrder}
      value={viewOptions.asc.toString()}
      label="Order"
      name="select-order"
      className={className}
    >
      <option value="true">Asc</option>
      <option value="false">Desc</option>
    </Select>
  );
};

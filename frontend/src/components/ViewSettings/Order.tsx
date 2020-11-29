import * as React from 'react';
import { Select } from 'src/components/common';
import { ViewOptionsT } from 'src/hooks';

export const Order: React.FC<{ viewOptions: ViewOptionsT; className?: string }> = ({
  viewOptions,
  className,
}) => {
  const updateOrder = React.useCallback(
    (e) => viewOptions.setAsc(e.currentTarget.value === 'true'),
    [viewOptions],
  );

  return (
    <Select
      className={className}
      label="Order"
      name="select-order"
      value={viewOptions.asc.toString()}
      onChange={updateOrder}
    >
      <option value="true">Asc</option>
      <option value="false">Desc</option>
    </Select>
  );
};

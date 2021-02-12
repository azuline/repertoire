import * as React from 'react';

import { Select } from '~/components/common';
import { IViewOptions } from '~/hooks';

export const Order: React.FC<{ viewOptions: IViewOptions; className?: string }> = ({
  viewOptions,
  className,
}) => {
  const updateOrder = (e: React.FormEvent<HTMLSelectElement>): void =>
    viewOptions.setAsc(e.currentTarget.value === 'true');

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

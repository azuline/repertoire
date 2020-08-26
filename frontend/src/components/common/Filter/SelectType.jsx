import { Button, MenuItem } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { FilterContext } from 'contexts';
import { Select } from '@blueprintjs/select';

export const SelectType = ({ selections }) => {
  const { selection, updateFilter } = useContext(FilterContext);

  const renderItem = (item) => {
    return (
      <MenuItem
        active={selection === item}
        key={item}
        onClick={() => updateFilter({ selection: item })}
        text={item}
      />
    );
  };

  return (
    <Select
      className="SelectType"
      filterable={false}
      items={selections}
      itemRenderer={renderItem}
      popoverProps={{ minimal: true, transitionDuration: 50 }}
    >
      <Button text={selection} rightIcon="caret-down" />
    </Select>
  );
};

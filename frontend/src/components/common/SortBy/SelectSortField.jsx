import { Button, MenuItem } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { Select } from '@blueprintjs/select';
import { SortContext } from 'contexts';

export const SelectSortField = ({ criteria }) => {
  const { sortField, updateSort } = useContext(SortContext);

  const renderCriteria = ({ id, name, icon }) => {
    return (
      <MenuItem
        active={id === sortField}
        key={id}
        onClick={() => updateSort({ sortField: id })}
        icon={icon}
        text={name}
      />
    );
  };

  return (
    <Select
      className="SelectSortField"
      filterable={false}
      items={Object.values(criteria)}
      itemRenderer={renderCriteria}
      popoverProps={{ minimal: true, transitionDuration: 50 }}
    >
      <Button
        text={criteria[sortField].name}
        icon={criteria[sortField].icon}
        rightIcon="caret-down"
      />
    </Select>
  );
};

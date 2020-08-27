import { Button, MenuItem } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { Select } from '@blueprintjs/select';
import { SortContext } from 'contexts';

export const SelectSortField = ({ criteria }) => {
  const { sortField, setSortField } = useContext(SortContext);

  const renderCriteria = ([name, { icon }]) => {
    return (
      <MenuItem
        active={name === sortField}
        key={name}
        onClick={() => setSortField(name)}
        icon={icon}
        text={name}
      />
    );
  };

  return (
    <Select
      className="SelectSortField"
      filterable={false}
      items={Object.entries(criteria)}
      itemRenderer={renderCriteria}
      popoverProps={{ minimal: true, transitionDuration: 50 }}
    >
      <Button text={sortField} icon={criteria[sortField].icon} rightIcon="caret-down" />
    </Select>
  );
};

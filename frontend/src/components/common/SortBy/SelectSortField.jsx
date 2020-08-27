import { Button, MenuItem } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { Select } from '@blueprintjs/select';
import { SortContext } from 'contexts';

export const SelectSortField = ({ criteria }) => {
  const { sortField, setSortField } = useContext(SortContext);

  const renderCriteria = ([key, { label, icon }]) => {
    return (
      <MenuItem
        active={key === sortField}
        key={key}
        onClick={() => setSortField(key)}
        icon={icon}
        text={label}
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
      <Button
        text={criteria[sortField].label}
        icon={criteria[sortField].icon}
        rightIcon="caret-down"
      />
    </Select>
  );
};

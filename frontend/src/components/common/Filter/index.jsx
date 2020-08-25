import { ControlGroup } from '@blueprintjs/core';
import { FilterByName } from './FilterByName';
import React from 'react';
import { SelectType } from './SelectType';

export const Filter = ({ selections }) => {
  return (
    <ControlGroup className="Filter" fill>
      <SelectType selections={selections} />
      <FilterByName />
    </ControlGroup>
  );
};

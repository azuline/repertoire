import './index.scss';

import { ChooseSortOrder } from './ChooseSortOrder';
import { ControlGroup } from '@blueprintjs/core';
import React from 'react';
import { SelectSortField } from './SelectSortField';

export const SortBy = ({ criteria }) => {
  return (
    <ControlGroup className="SortBy">
      <SelectSortField criteria={criteria} />
      <ChooseSortOrder />
    </ControlGroup>
  );
};

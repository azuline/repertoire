import './index.scss';

import { Filter } from 'components/common/Filter';
import React from 'react';
import { SortBy } from 'components/common/SortBy';

export const ListOptions = ({ selections, sortCriteria }) => {
  return (
    <div className="ListOptions">
      <Filter selections={selections} />
      <SortBy criteria={sortCriteria} />
    </div>
  );
};

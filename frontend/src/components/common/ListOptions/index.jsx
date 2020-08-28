import { Filter } from 'components/common/Filter';
import React from 'react';
import { SortBy } from 'components/common/SortBy';
import './index.scss';

export const ListOptions = ({ selections, sortCriteria }) => {
  return (
    <div className="ListOptions">
      <Filter selections={selections} />
      <SortBy criteria={sortCriteria} />
    </div>
  );
};

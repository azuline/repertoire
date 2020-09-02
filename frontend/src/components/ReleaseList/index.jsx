import './index.scss';

import { Pagination } from 'components/common/Pagination';
import React from 'react';
import { ReleaseListOptions } from './ReleaseListOptions';
import { Releases } from './Releases';
import { SideBars } from './SideBars';

export const ReleaseList = () => {
  return (
    <div className="ReleaseList">
      <SideBars />
      <div className="TheActualList">
        <ReleaseListOptions />
        <Pagination />
        <Releases />
        <Pagination />
      </div>
    </div>
  );
};

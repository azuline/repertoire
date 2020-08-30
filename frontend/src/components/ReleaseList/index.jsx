import './index.scss';

import { Pagination } from 'components/common/Pagination';
import React from 'react';
import { ReleaseListOptions } from './ReleaseListOptions';
import { Releases } from './Releases';

export const ReleaseList = () => {
  return (
    <div className="ReleaseList">
      <ReleaseListOptions />
      <Pagination />
      <Releases />
      <Pagination />
    </div>
  );
};

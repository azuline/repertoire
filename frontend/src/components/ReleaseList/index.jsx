import './index.scss';
import { Pagination } from 'components/common/Pagination';

import { ReleaseListOptions } from './ReleaseListOptions';
import React from 'react';
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

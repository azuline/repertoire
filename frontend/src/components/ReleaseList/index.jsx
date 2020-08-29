import './index.scss';

import { ReleaseListOptions } from './ReleaseListOptions';
import React from 'react';
import { Releases } from './Releases';
import { Pagination } from 'components/common/Pagination';

export const ReleaseList = () => {
  return (
    <div className="ReleaseList">
      <ReleaseListOptions />
      <Pagination />
      <Releases />
    </div>
  );
};

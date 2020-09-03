import './index.scss';

import { Pagination } from 'components/common/Pagination';
import React, { useContext } from 'react';
import { ReleaseListOptions } from './ReleaseListOptions';
import { Releases } from './Releases';
import { SideBarContext } from 'contexts';
import { SideBars } from './SideBars';

export const ReleaseList = () => {
  const { numVisible } = useContext(SideBarContext);

  return (
    <div className={`ReleaseList SideBars${numVisible}`}>
      <SideBars />
      <div className="TheActualList">
        <ReleaseListOptions />
        <Pagination />
        <div className="ReleasesWrapper">
          <Releases />
        </div>
        <Pagination />
      </div>
    </div>
  );
};

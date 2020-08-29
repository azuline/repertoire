import './index.scss';

import { ReleaseSortContextProvider, ViewContextProvider } from 'contexts';

import { ReleaseListOptions } from './ReleaseListOptions';
import React from 'react';
import { Releases } from './Releases';

export const ReleaseList = () => {
  return (
    <div className="ReleaseList">
      <ReleaseSortContextProvider>
        <ViewContextProvider>
          <ReleaseListOptions />
          <Releases />
        </ViewContextProvider>
      </ReleaseSortContextProvider>
    </div>
  );
};

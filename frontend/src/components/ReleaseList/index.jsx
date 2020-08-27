import './index.scss';

import { ReleaseSortContextProvider, ViewContextProvider } from 'contexts';

import { ListOptions } from './ListOptions';
import React from 'react';
import { Releases } from './Releases';

export const ReleaseList = () => {
  return (
    <div className="ReleaseList">
      <ReleaseSortContextProvider>
        <ViewContextProvider>
          <ListOptions />
          <Releases />
        </ViewContextProvider>
      </ReleaseSortContextProvider>
    </div>
  );
};

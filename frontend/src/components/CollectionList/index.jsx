import './index.scss';

import {
  CollectionFilterContextProvider,
  CollectionSortContextProvider,
} from 'contexts';

import { Collections } from './Collections';
import { ListOptions } from './ListOptions';
import React from 'react';

// Fetch the stored context variables from localStorage.

export const CollectionList = () => {
  return (
    <div className="CollectionList">
      <CollectionSortContextProvider>
        <CollectionFilterContextProvider>
          <ListOptions />
          <Collections />
        </CollectionFilterContextProvider>
      </CollectionSortContextProvider>
    </div>
  );
};

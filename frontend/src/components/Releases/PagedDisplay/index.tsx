import * as React from 'react';
import { ReleaseSort } from 'src/types';
import { PaginationProvider } from 'src/contexts';

type PropsT = {
  search?: string;
  artistIds?: number[];
  collectionIds?: number[];
  releaseTypes?: string[];
  sort?: ReleaseSort;
  asc?: boolean;
};

export const PagedReleases: React.FC<PropsT> = (props) => (
  <PaginationProvider>
    <Wrapped {...props} />
  </PaginationProvider>
);

const Wrapped: React.FC<PropsT> = ({
  search = '',
  artistIds = [],
  collectionIds = [],
  releaseTypes = [],
  sort = 'RECENTLY_ADDED',
  asc = true,
}) => {
  return <div></div>;
};

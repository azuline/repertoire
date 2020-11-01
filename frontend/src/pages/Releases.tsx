import * as React from 'react';
import { PagedReleases } from 'src/components/Releases';
import { Pagination } from 'src/components/Pagination';
import { ViewSettings } from 'src/components/ViewSettings';
import {
  PaginationContext,
  ReleaseViewOptionsContext,
  ReleaseViewOptionsProvider,
} from 'src/contexts';
import { fetchReleases } from 'src/lib';

export const Releases: React.FC = () => (
  <ReleaseViewOptionsProvider>
    <Wrapped />
  </ReleaseViewOptionsProvider>
);

const Wrapped: React.FC = (): React.ReactElement => {
  const viewOptions = React.useContext(ReleaseViewOptionsContext);
  const pagination = React.useContext(PaginationContext);

  const { status, data } = fetchReleases(viewOptions, pagination);

  const releases = data && status === 'success' ? data.releases.results : [];

  return (
    <div>
      <span className="sect-header">Releases</span>
      <ViewSettings />
      <Pagination />
      <PagedReleases releases={releases} />
      <Pagination popperPlacement="top" />
    </div>
  );
};

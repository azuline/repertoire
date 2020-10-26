import * as React from 'react';
import { PagedReleases } from 'src/components/Releases';

export const Releases: React.FC = (): React.ReactElement => {
  return (
    <div className="">
      <span className="sect-header">Releases</span>
      <PagedReleases />
    </div>
  );
};

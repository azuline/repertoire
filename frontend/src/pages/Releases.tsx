import * as React from 'react';
import { PagedReleases } from 'src/components/Releases';
import { ReleaseViewOptionsProvider } from 'src/contexts';

export const Releases: React.FC = (): React.ReactElement => {
  return (
    <div className="">
      <span className="sect-header">Releases</span>
      <ReleaseViewOptionsProvider>
        <PagedReleases />
      </ReleaseViewOptionsProvider>
    </div>
  );
};

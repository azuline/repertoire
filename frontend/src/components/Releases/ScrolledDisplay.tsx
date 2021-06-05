import * as React from 'react';

import { ArtRelease } from '~/components/Release';
import { IReleaseFieldsFragment } from '~/graphql';

type IScrolledReleases = React.FC<{
  className?: string;
  releases: IReleaseFieldsFragment[];
}>;

export const ScrolledReleases: IScrolledReleases = ({ className, releases }) => (
  <div className={className} tw="py-8 flex overflow-x-auto">
    {releases.map((rls) => (
      <div key={rls.id} tw="flex-shrink-0 w-56 h-56 mr-4">
        <ArtRelease release={rls} />
      </div>
    ))}
  </div>
);

import * as React from 'react';
import { ReleaseT } from 'src/types';
import { Release } from 'src/components/common/Release';

export const ScrollingReleases: React.FC<{ releases: ReleaseT[] }> = ({ releases }) => {
  return (
    <div className="flex flex-row flex-no-wrap w-full h-64 rounded bg-gray-200 mt-4 overflow-x-auto p-2">
      {releases.map((rls) => (
        <Release className="w-48 flex-shrink-0 mr-2" key={rls.id} release={rls} />
      ))}
    </div>
  );
};

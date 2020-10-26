import * as React from 'react';
import { ReleaseT } from 'src/types';
import { ArtRelease } from 'src/components/Release';

const style = { height: '20rem' };

export const ScrolledReleases: React.FC<{ releases: ReleaseT[] }> = ({ releases }) => {
  return (
    <div
      className="flex flex-row flex-no-wrap w-full mt-4 overflow-x-auto py-2"
      style={style}
    >
      {releases.map((rls) => (
        <ArtRelease className="w-48 flex-shrink-0 mr-4" key={rls.id} release={rls} />
      ))}
    </div>
  );
};

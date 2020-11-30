import * as React from 'react';
import { Icon } from 'src/components';
import { ReleaseT } from 'src/types';

export const Rating: React.FC<{ release: ReleaseT }> = ({ release }) => {
  return (
    <>
      <div className="items-center hidden lg:flex">
        <span className="mr-1 text-foreground-200">{release.rating}</span>
        {Array.from(new Array(release.rating ?? 0), (_, i) => {
          return <Icon key={i} className="w-5 pr-0.5 text-primary-500" icon="star-small-filled" />;
        })}
      </div>
      <div className="flex items-center lg:hidden">
        <span className="mr-1 text-foreground-200">{release.rating ?? 0}</span>
        <Icon className="w-5 text-primary-500" icon="star-small-filled" />
      </div>
    </>
  );
};

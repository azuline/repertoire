import * as React from 'react';
import { ArtistT, ReleaseT } from 'src/types';
import { CoverArt } from './CoverArt';
import { ArtistList } from './ArtistList';
import { Card } from 'src/components/common/Card';

export const ArtRelease: React.FC<{ release: ReleaseT; className?: string }> = ({
  release,
  className = '',
}) => {
  return (
    <Card className={className}>
      <div className="relative h-0 pb-full">
        <a href={`/releases/${release.id}`}>
          <CoverArt className="absolute h-full w-full object-cover" release={release} />
        </a>
      </div>
      <div className="flex-1 mt-1">
        <a href={`/releases/${release.id}`}>
          <span className="truncate-2 font-medium" title={release.title}>
            {release.title}
          </span>
        </a>
        <ArtistList className="truncate-2" artists={release.artists as ArtistT[]} />
      </div>
    </Card>
  );
};

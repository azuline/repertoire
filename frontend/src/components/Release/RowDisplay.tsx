import clsx from 'clsx';
import * as React from 'react';
import { Link } from 'src/components/common';
import { Image } from 'src/components/Image';
import { ArtistList, GenreList } from 'src/components/Lists';
import { ReleaseT } from 'src/types';

import { InInboxIndicator } from './InInboxIndicator';
import { Rating } from './Rating';

const rowStyle = { width: 'calc(100% + 1.5rem)' };

export const RowRelease: React.FC<{ release: ReleaseT; className?: string }> = ({
  release,
  className,
}) => (
  <Link
    className={clsx(className, 'flex items-center -mx-3 p-3 cursor-pointer hover-emph-bg')}
    href={`/releases/${release.id}`}
    style={rowStyle}
  >
    {release.inInbox ? <InInboxIndicator className="w-5" /> : <div className="w-5" />}
    <div className="relative flex-none w-12 h-12 mr-2">
      <Image
        thumbnail
        className="absolute object-cover rounded-lg full"
        imageId={release.imageId}
      />
    </div>
    <div className="flex-1 overflow-hidden">
      <div className="flex">
        <div className="flex flex-1 mb-0.5 mr-4 truncate">
          <div className="font-semibold truncate text-primary-400">{release.title}</div>
          {release.releaseYear ? (
            <div className="flex-none hidden ml-1 sm:block text-foreground-200">
              {' '}
              [{release.releaseYear}]
            </div>
          ) : null}
        </div>
        <div className="flex-none ml-auto">
          {release.rating && <Rating rating={release.rating} />}
        </div>
      </div>
      <div className="flex text-foreground-300">
        <ArtistList className="mr-8 truncate max-w-3/5" elements={release.artists} />
        <div className="flex-1 hidden overflow-hidden text-right md:block rtl">
          <GenreList className="truncate" elements={release.genres} />
        </div>
      </div>
    </div>
  </Link>
);

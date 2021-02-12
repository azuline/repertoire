import clsx from 'clsx';
import * as React from 'react';

import { Link } from '~/components/common';
import { Image } from '~/components/Image';
import { ArtistList, GenreList } from '~/components/Lists';
import { IRelease } from '~/graphql';
import { filterNulls } from '~/util';

import { InInboxIndicator } from './InInboxIndicator';
import { Rating } from './Rating';

export const RowRelease: React.FC<{ release: IRelease; className?: string }> = ({
  release,
  className,
}) => {
  return (
    <Link
      className={clsx(className, 'flex items-center -mx-3 p-3 cursor-pointer hover-emph-bg')}
      href={`/releases/${release.id}`}
      style={{ width: 'calc(100% + 1.5rem)' }}
    >
      {release.inInbox ? <InInboxIndicator className="w-5" /> : <div className="w-5" />}
      <div className="relative flex-none w-12 h-12 mr-3">
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
            {release.rating ? (
              <Rating rating={release.rating} />
            ) : (
              <span className="text-foreground-400">No Rating</span>
            )}
          </div>
        </div>
        <div className="flex text-foreground-300">
          <ArtistList className="mr-8 truncate max-w-3/5" elements={filterNulls(release.artists)} />
          <div className="flex-1 hidden overflow-hidden text-right md:block rtl">
            <GenreList className="truncate" elements={filterNulls(release.genres)} />
          </div>
        </div>
      </div>
    </Link>
  );
};

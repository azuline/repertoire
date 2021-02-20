import * as React from 'react';

import { Link } from '~/components/common';
import { Image } from '~/components/Image';
import { ArtistList, GenreList } from '~/components/Lists';
import { IRelease } from '~/graphql';
import { filterNulls } from '~/util';

import { InInboxIndicator } from './InInboxIndicator';
import { Rating } from './Rating';

type IRowRelease = React.FC<{ release: IRelease; className?: string }>;

export const RowRelease: IRowRelease = ({ release, className }) => {
  return (
    <Link
      className={className}
      href={`/releases/${release.id}`}
      tw="flex items-center -mx-3 p-3 cursor-pointer hover-bg width[calc(100% + 1.5rem)]"
    >
      {release.inInbox ? <InInboxIndicator tw="w-5" /> : <div tw="w-5" />}
      <div tw="relative flex-none w-12 h-12 mr-3">
        <Image thumbnail imageId={release.imageId} tw="absolute object-cover rounded-lg full" />
      </div>
      <div tw="flex-1 overflow-hidden">
        <div tw="flex">
          <div tw="flex flex-1 mb-0.5 mr-4 truncate">
            <div tw="font-semibold truncate text-primary-400">{release.title}</div>
            {release.releaseYear ? (
              <div tw="flex-none hidden ml-1 sm:block text-foreground-200">
                {' '}
                [{release.releaseYear}]
              </div>
            ) : null}
          </div>
          <div tw="flex-none ml-auto">
            {release.rating ? (
              <Rating rating={release.rating} />
            ) : (
              <span tw="text-foreground-400">No Rating</span>
            )}
          </div>
        </div>
        <div tw="flex text-foreground-300">
          <ArtistList elements={filterNulls(release.artists)} tw="mr-8 truncate max-w-3/5" />
          <div tw="flex-1 hidden overflow-hidden text-right md:block rtl">
            <GenreList elements={filterNulls(release.genres)} tw="truncate" />
          </div>
        </div>
      </div>
    </Link>
  );
};

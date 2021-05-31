import * as React from 'react';
import tw from 'twin.macro';

import { Link } from '~/components/common';
import { Image } from '~/components/Image';
import { ArtistListWithRoles, GenreList } from '~/components/Lists';
import { IReleaseFieldsFragment } from '~/graphql';
import { filterNulls } from '~/util';

import { InInboxIndicator } from './InInboxIndicator';
import { Rating } from './Rating';

type IRowRelease = React.FC<{
  release: Pick<
    IReleaseFieldsFragment,
    | 'id'
    | 'title'
    | 'inInbox'
    | 'imageId'
    | 'releaseYear'
    | 'rating'
    | 'artists'
    | 'genres'
  >;
  className?: string;
}>;

export const RowRelease: IRowRelease = ({ release, className }) => {
  return (
    <Link
      className={className}
      css={[
        tw`flex items-center -mx-3 p-3 width[calc(100% + 1.5rem)]`,
        tw`cursor-pointer hover-bg`,
      ]}
      href={`/releases/${release.id}`}
    >
      {release.inInbox ? <InInboxIndicator tw="w-5" /> : <div tw="w-5" />}
      <div tw="relative flex-none w-12 h-12 mr-3">
        <Image
          thumbnail
          imageId={release.imageId}
          tw="absolute object-cover rounded-lg full"
        />
      </div>
      <div tw="flex-1 overflow-hidden">
        <div tw="flex">
          <div tw="flex flex-1 mb-0.5 mr-4 truncate">
            <div tw="font-semibold truncate text-primary-400">{release.title}</div>
            {release.releaseYear !== null ? (
              <div tw="flex-none hidden ml-1 sm:block text-foreground-200">
                {' '}
                [{release.releaseYear}]
              </div>
            ) : null}
          </div>
          <div tw="flex-none ml-auto">
            {release.rating !== null ? (
              <Rating rating={release.rating} />
            ) : (
              <span tw="text-foreground-500">No Rating</span>
            )}
          </div>
        </div>
        <div tw="flex text-foreground-300">
          <ArtistListWithRoles
            artists={filterNulls(release.artists)}
            tw="mr-8 truncate max-w-3/5"
          />
          <div tw="flex-1 hidden overflow-hidden text-right md:block rtl">
            <GenreList elements={filterNulls(release.genres)} tw="truncate" />
          </div>
        </div>
      </div>
    </Link>
  );
};

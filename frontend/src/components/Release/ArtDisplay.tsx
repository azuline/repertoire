import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { Link, TwoSided } from '~/components/common';
import { Image } from '~/components/Image';
import { ArtistList, GenreList } from '~/components/Lists';
import { IReleaseFieldsFragment } from '~/graphql';
import { filterNulls, secondsToLength } from '~/util';

import { InInboxIndicator } from './InInboxIndicator';

type IArtRelease = React.FC<{
  release: Pick<
    IReleaseFieldsFragment,
    | 'id'
    | 'runtime'
    | 'inInbox'
    | 'artists'
    | 'releaseYear'
    | 'numTracks'
    | 'genres'
    | 'imageId'
    | 'title'
  >;
  className?: string;
}>;

export const ArtRelease: IArtRelease = ({ release, className }) => {
  const runtime = secondsToLength(release.runtime);

  return (
    <Link href={`/releases/${release.id}`}>
      <div className={className} tw="relative h-0 pb-full">
        <Image
          thumbnail
          imageId={release.imageId}
          tw="absolute object-cover rounded-lg full"
        />
        <CustomTwoSided>
          <div tw="flex flex-col justify-end overflow-hidden full">
            <div tw="p-3 overflow-hidden">
              <div
                title={release.title}
                tw="flex min-w-0 text-lg font-semibold text-white"
              >
                <div tw="truncate">{release.title}</div>
                {release.inInbox && <InInboxIndicator tw="pl-2" />}
              </div>
              <ArtistList
                elements={filterNulls(release.artists)}
                tw="text-gray-200 truncate"
              />
            </div>
          </div>
          <div tw="relative full">
            <div tw="absolute top-0 left-0 bg-black rounded-lg bg-opacity-75 full" />
            <div
              css={[
                tw`absolute top-0 left-0 z-10 p-4 full`,
                tw`flex flex-col items-center justify-center`,
                tw`text-white text-base`,
              ]}
            >
              {release.releaseYear !== null ? (
                <div tw="py-1">{release.releaseYear}</div>
              ) : null}
              <div tw="py-1">
                {release.numTracks} Track{release.numTracks !== 1 && 's'} / {runtime}
              </div>
              {release.genres.length !== 0 ? (
                <GenreList
                  elements={filterNulls(release.genres)}
                  tw="mt-4 text-center truncate-2"
                />
              ) : null}
            </div>
          </div>
        </CustomTwoSided>
      </div>
    </Link>
  );
};

const CustomTwoSided = styled(TwoSided)`
  ${tw`absolute z-10 rounded-lg full`}

  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0),
    rgba(0, 0, 0, 0.1),
    rgba(0, 0, 0, 0.4),
    rgba(0, 0, 0, 0.7), 
    rgba(0, 0, 0, 0.9)
  );

  textshadow: '1px black';
`;

import 'twin.macro';

import clsx from 'clsx';
import * as React from 'react';

import { Link, TwoSided } from '~/components/common';
import { Image } from '~/components/Image';
import { ArtistList, GenreList } from '~/components/Lists';
import { IRelease } from '~/graphql';
import { filterNulls, secondsToLength } from '~/util';

import { InInboxIndicator } from './InInboxIndicator';

export const ArtRelease: React.FC<{ release: IRelease; className?: string }> = ({
  release,
  className,
}) => {
  const runtime = secondsToLength(release.runtime);

  return (
    <Link href={`/releases/${release.id}`}>
      <div className={className} tw="relative h-0 pb-full">
        <Image thumbnail imageId={release.imageId} tw="absolute object-cover rounded-lg full" />
        <TwoSided
          style={{
            background:
              'linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.9))',
            textShadow: '1px black',
          }}
          tw="absolute z-10 rounded-lg full"
        >
          <div tw="flex flex-col justify-end overflow-hidden full">
            <div tw="p-3 overflow-hidden">
              <div title={release.title} tw="flex min-w-0 text-lg font-semibold text-white">
                <div tw="truncate">{release.title}</div>
                {release.inInbox && <InInboxIndicator tw="pl-2" />}
              </div>
              <ArtistList elements={filterNulls(release.artists)} tw="text-gray-200 truncate" />
            </div>
          </div>
          <div tw="relative full">
            <div tw="absolute top-0 left-0 bg-black rounded-lg bg-opacity-75 full" />
            <div tw="absolute top-0 left-0 z-10 flex flex-col items-center justify-center p-4 text-white full text-base">
              {release.releaseYear ? <div tw="py-1">{release.releaseYear}</div> : null}
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
        </TwoSided>
      </div>
    </Link>
  );
};

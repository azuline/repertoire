import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { ArtistList, GenreList, LabelList, Link, SectionHeader } from '~/components';
import { IRelease } from '~/graphql';
import { filterNulls } from '~/util';

import { InFavorites } from './InFavorites';
import { InInbox } from './InInbox';
import { WhenReleased } from './WhenReleased';

export const Info: React.FC<{ release: IRelease }> = ({ release }) => {
  return (
    <div tw="flex flex-col flex-1 min-w-0 md:min-h-52">
      <SectionHeader tw="flex-none mb-6 md:mb-4 truncate-2">
        <div>
          <div tw="float-right ml-2 w-18 md:hidden">
            <div tw="flex">
              <InFavorites release={release} tw="flex-none" />
              <InInbox release={release} tw="flex-none" />
            </div>
          </div>
          {release.title}
        </div>
      </SectionHeader>
      <div tw="flex-none mb-2 truncate-2 text-foreground-100">
        <span tw="text-foreground-300">By </span>
        {release.artists.length === 0 ? (
          <Link href="/artists/1">Unknown Artist</Link>
        ) : (
          <CustomArtistList link elements={filterNulls(release.artists)} tw="inline" />
        )}
      </div>
      <div tw="flex-none mb-4 truncate-2 text-foreground-100">
        <WhenReleased release={release} />
        <span tw="text-foreground-300"> on </span>
        {release.labels.length === 0 ? (
          <span>No Label</span>
        ) : (
          <CustomLabelList link elements={filterNulls(release.labels)} tw="inline" />
        )}
      </div>
      <div tw="flex-none mt-2 truncate-2 md:mt-auto">
        {release.genres.length !== 0 && (
          <>
            <CustomGenreList link delimiter=" " elements={filterNulls(release.genres)} />
          </>
        )}
      </div>
    </div>
  );
};

const CustomArtistList = styled(ArtistList)`
  .list--element {
    ${tw`text-primary-400`}
  }
`;

const CustomLabelList = styled(LabelList)`
  .list--element {
    ${tw`text-primary-400`}
  }
`;

const CustomGenreList = styled(GenreList)`
  .list--element {
    ${tw`px-2 py-1 mr-1 rounded bg-primary-700 text-foreground hover:bg-primary-600 leading-9`}
  }
`;

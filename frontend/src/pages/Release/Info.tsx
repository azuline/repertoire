import * as React from 'react';

import { ArtistList, GenreList, LabelList, Link, SectionHeader } from '~/components';
import { IRelease } from '~/graphql';
import { filterNulls } from '~/util';

import { InFavorites } from './InFavorites';
import { InInbox } from './InInbox';
import { WhenReleased } from './WhenReleased';

export const Info: React.FC<{ release: IRelease }> = ({ release }) => {
  return (
    <div className="flex flex-col flex-1 min-w-0 md:min-h-52">
      <SectionHeader className="flex-none mb-6 md:mb-4 truncate-2">
        <div>
          <div className="float-right ml-2 w-18 md:hidden">
            <div className="flex">
              <InFavorites className="flex-none" release={release} />
              <InInbox className="flex-none" release={release} />
            </div>
          </div>
          {release.title}
        </div>
      </SectionHeader>
      <div className="flex-none mb-2 truncate-2 text-foreground-100">
        <span className="text-foreground-300">By </span>
        {release.artists.length === 0 ? (
          <Link href="/artists/1">Unknown Artist</Link>
        ) : (
          <ArtistList
            link
            className="inline"
            elementClassName="text-primary-400"
            elements={filterNulls(release.artists)}
          />
        )}
      </div>
      <div className="flex-none mb-4 truncate-2 text-foreground-100">
        <WhenReleased release={release} />
        <span className="text-foreground-300"> on </span>
        {release.labels.length === 0 ? (
          <span>No Label</span>
        ) : (
          <LabelList
            link
            className="inline"
            elementClassName="text-primary-400"
            elements={filterNulls(release.labels)}
          />
        )}
      </div>
      <div className="flex-none mt-2 truncate-2 md:mt-auto">
        {release.genres.length !== 0 && (
          <>
            <GenreList
              link
              delimiter=" "
              elementClassName="px-2 py-1 mr-1 rounded bg-primary-700 text-foreground hover:bg-primary-600 leading-9"
              elements={filterNulls(release.genres)}
            />
          </>
        )}
      </div>
    </div>
  );
};

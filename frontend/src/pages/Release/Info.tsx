import * as React from 'react';
import { ArtistList, GenreList, LabelList, Link, SectionHeader } from 'src/components';
import { ReleaseT } from 'src/types';

import { InFavorites } from './InFavorites';
import { InInbox } from './InInbox';
import { WhenReleased } from './WhenReleased';

export const Info: React.FC<{ release: ReleaseT }> = ({ release }) => {
  return (
    <div className="flex flex-col flex-1 min-w-0 md:min-h-52">
      <SectionHeader className="flex-none mb-4 truncate-2">
        <div>
          <div className="w-18 ml-2 float-right md:hidden">
            <div className="flex">
              <InFavorites className="flex-none" release={release} />
              <InInbox className="flex-none" release={release} />
            </div>
          </div>
          {release.title}
        </div>
      </SectionHeader>
      <div className="flex-none mb-1 text-lg truncate-2">
        {release.artists.length === 0 ? (
          <Link href="/artists/1">Unknown Artist</Link>
        ) : (
          <>
            <span className="text-foreground-400">By </span>
            <ArtistList
              link
              className="inline"
              elementClassName="text-primary-400"
              elements={release.artists}
            />
          </>
        )}
      </div>
      <div className="flex-none mb-2 text-lg truncate-2 text-foreground-300">
        <WhenReleased release={release} />
        <span className="text-foreground-400"> on </span>
        {release.labels.length === 0 ? (
          <span>No Label</span>
        ) : (
          <>
            <span>{release.labels.length !== 1 ? 'Labels' : 'Label'}: </span>
            <LabelList
              link
              className="inline"
              elementClassName="text-primary-400"
              elements={release.labels}
            />
          </>
        )}
      </div>
      <div className="flex-none text-md truncate-2 md:mt-auto">
        {release.genres.length !== 0 && (
          <>
            <GenreList
              link
              delimiter=" "
              elementClassName="px-2 py-1 mr-1 rounded bg-primary-700 text-foreground hover:bg-primary-600 leading-9"
              elements={release.genres}
            />
          </>
        )}
      </div>
    </div>
  );
};

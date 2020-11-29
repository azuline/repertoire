import * as React from 'react';
import { ArtistList, GenreList, LabelList, Link, SectionHeader } from 'src/components';
import { ReleaseT } from 'src/types';
import { formatReleaseDate } from 'src/util';

import { InFavorites } from './InFavorites';
import { InInbox } from './InInbox';

export const Info: React.FC<{ release: ReleaseT }> = ({ release }) => {
  const whenReleased = React.useMemo(() => formatReleaseDate(release), [release]);

  return (
    <div className="flex flex-col">
      <SectionHeader className="mb-2 truncate-2">{release.title}</SectionHeader>
      <div className="mb-4 text-xl truncate-2">
        {release.artists.length === 0 ? (
          <Link href="/artists/1">Unknown Artist</Link>
        ) : (
          <>
            <span>By: </span>
            <ArtistList
              className="inline"
              elementClassName="text-primary-400"
              elements={release.artists}
              link
            />
          </>
        )}
      </div>
      <div className="mb-1 text-foreground-300 text-md">{whenReleased}</div>
      <div className="mb-1 text-foreground-300 text-md truncate-2">
        {release.labels.length === 0 ? (
          <span>No Label</span>
        ) : (
          <>
            <span>{release.labels.length !== 1 ? 'Labels' : 'Label'}: </span>
            <LabelList
              className="inline"
              elementClassName="text-primary-400"
              elements={release.labels}
              link
            />
          </>
        )}
      </div>
      <div className="text-md truncate-2">
        {release.genres.length !== 0 && (
          <>
            <GenreList
              className="my-2"
              elementClassName="px-2 py-1 mr-1 rounded bg-primary-700 text-foreground hover:bg-primary-600 leading-9"
              elements={release.genres}
              delimiter=" "
              link
            />
          </>
        )}
      </div>
      <div className="flex items-center my-2">
        <InFavorites release={release} />
        <InInbox release={release} />
      </div>
    </div>
  );
};

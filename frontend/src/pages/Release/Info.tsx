import * as React from 'react';

import { ReleaseT } from 'src/types';
import { ArtistList, GenreList, LabelList } from 'src/components/Release';
import { ArtistT, CollectionT } from 'src/types';
import { formatReleaseDate } from 'src/common';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { Link } from 'src/components/common/Link';

export const Info: React.FC<{ release: ReleaseT }> = ({ release }) => {
  const whenReleased = React.useMemo(() => formatReleaseDate(release), [release]);

  return (
    <>
      <div className="ml-8 flex flex-col">
        <SectionHeader className="truncate-2 mb-4">{release.title}</SectionHeader>
        <div className="text-xl truncate-2 mb-2">
          {(release.artists as ArtistT[]).length === 0 ? (
            <Link href="/artists/1">Unknown Artist</Link>
          ) : (
            <>
              <span>By: </span>
              <ArtistList
                className="inline"
                elementClassName="text-primary-alt3"
                elements={release.artists}
                link
              />
            </>
          )}
        </div>
        <div className="text-lg mb-1 text-gray-800 dark:text-gray-300">{whenReleased}</div>
        <div className="text-lg truncate-2 mb-1 text-gray-800 dark:text-gray-300">
          {(release.labels as CollectionT[]).length === 0 ? (
            <span>No Label</span>
          ) : (
            <>
              <span>Labels: </span>
              <LabelList
                className="inline"
                elementClassName="text-primary-alt3"
                elements={release.labels}
                link
              />
            </>
          )}
        </div>
        <div className="text-lg truncate-2 mb-1 text-gray-800 dark:text-gray-300">
          {(release.genres as CollectionT[]).length === 0 ? (
            <span>No Genres</span>
          ) : (
            <>
              <span>Genres: </span>
              <GenreList
                className="inline"
                elementClassName="bg-primary-alt px-2 py-1 rounded leading-9"
                elements={release.genres}
                delimiter={'  '}
                link
              />
            </>
          )}
        </div>
      </div>
    </>
  );
};

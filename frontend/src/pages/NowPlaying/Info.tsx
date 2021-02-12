import * as React from 'react';

import { GenreList, Image, Link, SectionHeader, TrackArtistList } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useFetchRelease } from '~/lib';
import { TrackT } from '~/types';

export const Info: React.FC<{ track: TrackT }> = ({ track }) => {
  const { setBackgroundImageId } = React.useContext(BackgroundContext);
  const { data } = useFetchRelease(track.release.id);

  const parentRelease = data?.release || null;

  React.useEffect(() => {
    if (!parentRelease) return;

    setBackgroundImageId(parentRelease.imageId);
    return (): void => setBackgroundImageId(null);
  }, [parentRelease, setBackgroundImageId]);

  return (
    <div className="flex">
      <Image
        className="flex-none hidden w-48 h-48 mr-8 rounded-lg md:block"
        imageId={track.release.imageId}
      />
      <div className="flex flex-col flex-1 min-w-0 md:min-h-48">
        <SectionHeader className="flex-none mb-6 md:mb-4 truncate-2">{track.title}</SectionHeader>
        <div className="flex-none mb-1 truncate-2">
          <span className="text-foreground-300">By </span>
          {track.artists.length === 0 ? (
            <Link href="/artists/1">Unknown Artist</Link>
          ) : (
            <TrackArtistList
              link
              artists={track.artists}
              className="inline"
              elementClassName="text-primary-400"
            />
          )}
        </div>
        <div className="flex-none mb-2">
          <span className="text-foreground-300">From </span>
          <Link href={`/releases/${track.release.id}`}>
            <span className="text-primary-400">{parentRelease?.title ?? 'Loading...'}</span>
          </Link>
        </div>
        <div className="flex-none mt-4 text-md truncate-2 md:mt-auto">
          {parentRelease && parentRelease.genres.length !== 0 && (
            <>
              <GenreList
                link
                delimiter=" "
                elementClassName="px-2 py-1 mr-1 rounded bg-primary-700 text-foreground hover:bg-primary-600 leading-9"
                elements={parentRelease.genres}
              />
            </>
          )}
        </div>
      </div>
    </div>
  );
};

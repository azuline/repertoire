import clsx from 'clsx';
import * as React from 'react';
import { GenreList, Image, Link, SectionHeader, TrackArtistList } from 'src/components';
import { BackgroundContext, SidebarContext } from 'src/contexts';
import { useFetchRelease } from 'src/lib';
import { TrackT } from 'src/types';

export const Info: React.FC<{ track: TrackT }> = ({ track }) => {
  const { setBackgroundImageId } = React.useContext(BackgroundContext);
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const { data } = useFetchRelease(track.release.id);

  const parentRelease = React.useMemo(() => data?.release || null, [data]);

  React.useEffect(() => {
    if (!parentRelease) return;

    setBackgroundImageId(parentRelease.imageId);
    return (): void => setBackgroundImageId(null);
  }, [parentRelease, setBackgroundImageId]);

  return (
    <div className="z-10 flex px-8">
      <Image
        className={clsx(
          'flex-none hidden w-44 h-44 mr-8 rounded-lg',
          isSidebarOpen ? 'md:block' : 'sm:block',
        )}
        imageId={track.release.imageId}
      />
      <div className="flex flex-col">
        <SectionHeader className="mb-2 truncate-2">{track.title}</SectionHeader>
        <div className="mb-4 text-xl truncate-2">
          {track.artists.length === 0 ? (
            <Link href="/artists/1">Unknown Artist</Link>
          ) : (
            <>
              <span>By: </span>
              <TrackArtistList
                className="inline"
                elementClassName="text-primary-400"
                artists={track.artists}
                link
              />
            </>
          )}
        </div>
        <div className="mb-2 text-md">
          <span className="text-gray-800 dark:text-gray-300">From </span>
          <Link href={`/releases/${track.release.id}`}>
            <span className="text-primary-400">{parentRelease?.title || 'Loading...'}</span>
          </Link>
        </div>
        <div className="text-gray-800 dark:text-gray-300 text-md truncate-2">
          {parentRelease && parentRelease.genres.length !== 0 && (
            <>
              <GenreList
                className="my-2"
                elementClassName="px-2 py-1 mr-1 rounded bg-primary-700 text-foreground hover:bg-primary-600 leading-9"
                elements={parentRelease.genres}
                delimiter=" "
                link
              />
            </>
          )}
        </div>
      </div>
    </div>
  );
};

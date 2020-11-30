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
          'flex-none hidden w-48 h-48 mr-8 rounded-lg',
          isSidebarOpen ? 'md:block' : 'sm:block',
        )}
        imageId={track.release.imageId}
      />
      <div
        className={clsx(
          'flex flex-col flex-1 min-w-0',
          isSidebarOpen ? 'md:min-h-48' : 'sm:min-h-48',
        )}
      >
        <SectionHeader className="flex-none mb-3 truncate-2">{track.title}</SectionHeader>
        <div className="flex-none mb-1 text-lg truncate-2">
          {track.artists.length === 0 ? (
            <Link href="/artists/1">Unknown Artist</Link>
          ) : (
            <>
              <span className="text-foreground-400">By </span>
              <TrackArtistList
                link
                artists={track.artists}
                className="inline"
                elementClassName="text-primary-400"
              />
            </>
          )}
        </div>
        <div className="flex-none mb-2 text-lg">
          <span className="text-foreground-400">From </span>
          <Link href={`/releases/${track.release.id}`}>
            <span className="text-primary-400">{parentRelease?.title ?? 'Loading...'}</span>
          </Link>
        </div>
        <div
          className={clsx(
            'flex-none mt-4 text-md truncate-2',
            isSidebarOpen ? 'md:mt-auto' : 'sm:mt-auto',
          )}
        >
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

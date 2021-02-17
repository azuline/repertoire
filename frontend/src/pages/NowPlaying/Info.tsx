import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { GenreList, Image, Link, SectionHeader, TrackArtistList } from '~/components';
import { BackgroundContext } from '~/contexts';
import { ITrack, useFetchReleaseQuery } from '~/graphql';
import { filterNulls } from '~/util';

export const Info: React.FC<{ track: ITrack }> = ({ track }) => {
  const { setBackgroundImageId } = React.useContext(BackgroundContext);
  const { data } = useFetchReleaseQuery({ variables: { id: track.release.id } });

  const parentRelease = data?.release || null;

  React.useEffect(() => {
    if (!parentRelease) return;

    setBackgroundImageId(parentRelease.imageId);
    return (): void => setBackgroundImageId(null);
  }, [parentRelease, setBackgroundImageId]);

  return (
    <div tw="flex">
      <Image
        imageId={track.release.imageId}
        tw="flex-none hidden w-48 h-48 mr-8 rounded-lg md:block"
      />
      <div tw="flex flex-col flex-1 min-w-0 md:min-h-48">
        <SectionHeader tw="flex-none mb-6 md:mb-4 truncate-2">{track.title}</SectionHeader>
        <div tw="flex-none mb-1 truncate-2">
          <span tw="text-foreground-300">By </span>
          {track.artists.length === 0 ? (
            <Link href="/artists/1">Unknown Artist</Link>
          ) : (
            <CustomTrackArtistList link artists={filterNulls(track.artists)} tw="inline" />
          )}
        </div>
        <div tw="flex-none mb-2">
          <span tw="text-foreground-300">From </span>
          <Link href={`/releases/${track.release.id}`}>
            <span tw="text-primary-400">{parentRelease?.title ?? 'Loading...'}</span>
          </Link>
        </div>
        <div tw="flex-none mt-4 text-base truncate-2 md:mt-auto">
          {parentRelease && parentRelease.genres.length !== 0 && (
            <>
              <CustomGenreList link delimiter=" " elements={filterNulls(parentRelease.genres)} />
            </>
          )}
        </div>
      </div>
    </div>
  );
};

const CustomTrackArtistList = styled(TrackArtistList)`
  .list--element {
    ${tw`text-primary-400`}
  }
`;

const CustomGenreList = styled(GenreList)`
  .list--element {
    ${tw`px-2 py-1 mr-1 rounded bg-primary-700 text-foreground hover:bg-primary-600 leading-9`}
  }
`;

import * as React from 'react';
import { Chooser, ElementT } from 'src/components';
import { fetchArtists, useMutateArtist } from 'src/lib';

const urlFactory = (id: number): string => `/artists/${id}`;

export const ArtistChooser: React.FC<{
  active: number | null;
  className?: string;
}> = ({ active, className }) => {
  const { status, data } = fetchArtists();
  const [mutateArtist] = useMutateArtist();

  const toggleStarFactory = React.useCallback(
    ({ id, starred }: ElementT) => {
      return async (): Promise<void> => {
        mutateArtist({ id, starred: !starred });
      };
    },
    [mutateArtist],
  );

  if (!data || status !== 'success') return null;

  return (
    <Chooser
      className={className}
      results={data.artists.results}
      active={active}
      urlFactory={urlFactory}
      toggleStarFactory={toggleStarFactory}
    />
  );
};

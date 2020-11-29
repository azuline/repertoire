import * as React from 'react';
import { Chooser, ElementT } from 'src/components';
import { useFetchArtists, useMutateArtist } from 'src/lib';

const urlFactory = (id: number): string => `/artists/${id}`;

export const ArtistChooser: React.FC<{
  active: number | null;
  className?: string;
}> = ({ active, className }) => {
  const { data, error, loading } = useFetchArtists();
  const [mutateArtist] = useMutateArtist();

  const toggleStarFactory = React.useCallback(
    ({ id, starred }: ElementT) => async (): Promise<void> => {
      mutateArtist({ variables: { id, starred: !starred } });
    },
    [mutateArtist],
  );

  if (!data || error || loading) return null;

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

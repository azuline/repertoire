import * as React from 'react';

import { Chooser, ToggleStarFactory } from '~/components';
import { useFetchArtists, useMutateArtist } from '~/lib';

const urlFactory = (id: number): string => `/artists/${id}`;

export const ArtistChooser: React.FC<{
  active: number | null;
  className?: string;
}> = ({ active, className }) => {
  const { data, error, loading } = useFetchArtists();
  const [mutateArtist] = useMutateArtist();

  const toggleStarFactory: ToggleStarFactory = ({ id, starred }) => {
    return async (): Promise<void> => {
      mutateArtist({ variables: { id, starred: !starred } });
    };
  };

  if (!data || error || loading) return null;

  return (
    <Chooser
      active={active}
      className={className}
      results={data.artists.results}
      toggleStarFactory={toggleStarFactory}
      urlFactory={urlFactory}
    />
  );
};

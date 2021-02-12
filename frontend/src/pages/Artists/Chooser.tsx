import * as React from 'react';

import { Chooser, ToggleStarFactory } from '~/components';
import { IArtist, useFetchArtistsQuery, useUpdateArtistStarredMutation } from '~/graphql';

const urlFactory = (id: number): string => `/artists/${id}`;

export const ArtistChooser: React.FC<{
  active: number | null;
  className?: string;
}> = ({ active, className }) => {
  const { data, error, loading } = useFetchArtistsQuery();
  const [mutateArtist] = useUpdateArtistStarredMutation();

  const toggleStarFactory: ToggleStarFactory = ({ id, starred }) => {
    return async (): Promise<void> => {
      mutateArtist({ variables: { id, starred: !starred } });
    };
  };

  if (!data || !data.artists || error || loading) return null;

  return (
    <Chooser
      active={active}
      className={className}
      results={data.artists.results as IArtist[]}
      toggleStarFactory={toggleStarFactory}
      urlFactory={urlFactory}
    />
  );
};

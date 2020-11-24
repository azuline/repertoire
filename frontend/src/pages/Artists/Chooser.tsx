import * as React from 'react';

import { Chooser, ElementT } from 'src/components/Chooser';
import { fetchArtists, useMutateArtist } from 'src/lib';

const urlFactory = (id: number): string => `/artists/${id}`;

export const ArtistChooser: React.FC<{
  active: number | null;
  className?: string;
}> = ({ active, className }) => {
  const { status, data } = fetchArtists();
  const [mutateArtist] = useMutateArtist();

  const results = React.useMemo(() => {
    if (!data || status !== 'success') return null;

    const results = data.artists.results;
    results.sort((a, b) => a.name.localeCompare(b.name));
    return results;
  }, [data, status]);

  const toggleStarFactory = React.useCallback(
    ({ id, starred }: ElementT) => {
      return async (): Promise<void> => {
        mutateArtist({ id, starred: !starred });
      };
    },
    [mutateArtist],
  );

  if (!results) return null;

  return (
    <Chooser
      className={className}
      results={results}
      active={active}
      urlFactory={urlFactory}
      toggleStarFactory={toggleStarFactory}
    />
  );
};

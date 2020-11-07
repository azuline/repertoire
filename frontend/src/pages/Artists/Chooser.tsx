import * as React from 'react';
import { useHistory } from 'react-router-dom';
import Fuse from 'fuse.js';
import { fuseOptions } from 'src/constants';

import { Chooser } from 'src/components/Chooser';
import { fetchArtists } from 'src/lib';
import { useToasts } from 'react-toast-notifications';

export const ArtistChooser: React.FC<{
  active: number | null;
  className?: string | undefined;
}> = ({ active, className }) => {
  const [filter, setFilter] = React.useState<string>('');
  const { status, data } = fetchArtists();
  const history = useHistory();
  const { addToast } = useToasts();

  // Let user know that we are loading artists.
  React.useEffect(() => {
    if (status === 'loading') addToast('Loading artists...', { appearance: 'info' });
  }, [status]);

  // Fetch raw results from backend and sort them.
  const rawResults = React.useMemo(() => {
    if (!data || status !== 'success') return null;

    const results = data.artists.results;
    results.sort((a, b) => a.name.localeCompare(b.name));
    return results;
  }, [data, status]);

  // Construct the fuzzy-matcher class.
  const fuse = React.useMemo(() => {
    if (!rawResults) return null;

    return new Fuse(rawResults, { ...fuseOptions, keys: ['name'] });
  }, [rawResults]);

  // Given the fuzzy filter and the artists, build the artists to display.
  const results = React.useMemo(() => {
    if (!fuse || !rawResults) return [];

    return filter ? fuse.search(filter).map(({ item }) => item) : rawResults;
  }, [fuse, rawResults, filter]);

  const makeUrl = React.useCallback((id: number): string => `/artists/${id}`, [history]);

  return (
    <Chooser
      className={className}
      results={results}
      filter={filter}
      setFilter={setFilter}
      active={active}
      makeUrl={makeUrl}
    />
  );
};

import * as React from 'react';
import Fuse from 'fuse.js';
import { fuseOptions } from 'src/constants';

import { Chooser } from './Chooser';
import { RVOCType } from 'src/hooks';
import { fetchArtists } from 'src/lib';
import { useToasts } from 'react-toast-notifications';

export const ArtistChooser: React.FC<{
  viewOptions: RVOCType;
  className?: string | undefined;
}> = ({ viewOptions, className }) => {
  const [filter, setFilter] = React.useState<string>('');
  const { status, data } = fetchArtists();
  const { addToast } = useToasts();

  React.useEffect(() => {
    if (status === 'loading') addToast('Loading artists...', { appearance: 'info' });
  }, [status]);

  const rawResults = React.useMemo(() => {
    if (!data || status !== 'success') return null;

    const results = data.artists.results;
    results.sort((a, b) => a.name.localeCompare(b.name));
    return results;
  }, [data, status]);

  const fuse = React.useMemo(() => {
    if (!rawResults) return null;

    return new Fuse(rawResults, { ...fuseOptions, keys: ['name'] });
  }, [rawResults]);

  const results = React.useMemo(() => {
    if (!fuse || !rawResults) return [];

    return filter ? fuse.search(filter).map(({ item }) => item) : rawResults;
  }, [fuse, rawResults, filter]);

  return (
    <Chooser
      className={className}
      results={results}
      filter={filter}
      setFilter={setFilter}
      setter={viewOptions.setArtistIds}
    />
  );
};

import * as React from 'react';

import { Chooser } from 'src/components/Chooser';
import { fetchArtists } from 'src/lib';
import { useHistory } from 'react-router-dom';
import { useToasts } from 'react-toast-notifications';

export const ArtistChooser: React.FC<{
  active: number | null;
  className?: string | undefined;
}> = ({ active, className }) => {
  const { status, data } = fetchArtists();
  const history = useHistory();
  const { addToast } = useToasts();

  React.useEffect(() => {
    if (status === 'loading') addToast('Loading artists...', { appearance: 'info' });
  }, [status]);

  const results = React.useMemo(() => {
    if (!data || status !== 'success') return null;

    const results = data.artists.results;
    results.sort((a, b) => a.name.localeCompare(b.name));
    return results;
  }, [data, status]);

  const makeUrl = React.useCallback((id: number): string => `/artists/${id}`, [history]);

  if (!results) return null;

  return <Chooser className={className} results={results} active={active} makeUrl={makeUrl} />;
};

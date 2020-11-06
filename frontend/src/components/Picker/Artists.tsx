import * as React from 'react';

import { Chooser } from './Chooser';
import { RVOCType } from 'src/hooks';
import { Selector } from './Selector';
import { fetchArtists } from 'src/lib';
import { useToasts } from 'react-toast-notifications';

export const PickArtists: React.FC<{
  viewOptions: RVOCType;
  className?: string;
  picker: 'chooser' | 'selector';
}> = ({ viewOptions, className = '', picker }) => {
  const { status, data } = fetchArtists();
  const { addToast } = useToasts();

  React.useEffect(() => {
    if (status === 'loading') addToast('Loading artists...', { appearance: 'info' });
  }, [status]);

  const results = React.useMemo(() => {
    if (!data || status !== 'success') {
      return [];
    }

    const { results } = data.artists;
    results.sort((a, b) => a.name.localeCompare(b.name));
    return results;
  }, [status, data]);

  const Picker = React.useMemo(() => {
    switch (picker) {
      case 'chooser':
        return Chooser;
        break;
      case 'selector':
        return Selector;
    }
  }, [picker]);

  return <Picker className={className} results={results} setter={viewOptions.setArtistIds} />;
};

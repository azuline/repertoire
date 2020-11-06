import * as React from 'react';
import CSS from 'csstype';
import { RVOCType } from 'src/hooks';
import { fetchArtists } from 'src/lib';
import { useToasts } from 'react-toast-notifications';
import { Artist } from './Artist';

export const ChooseArtist: React.FC<{
  viewOptions: RVOCType;
  className?: string;
  style?: CSS.Properties | undefined;
}> = ({ viewOptions, className = '', style }) => {
  const [active, setActive] = React.useState<number>(0);
  const { status, data } = fetchArtists();
  const { addToast } = useToasts();

  React.useEffect(() => {
    if (status === 'loading') addToast('Loading artists...', { appearance: 'info' });
  }, [status]);

  React.useEffect(() => {
    viewOptions.setArtistIds(active !== 0 ? [active] : []);
  }, [active]);

  const results = React.useMemo(() => {
    if (!data || status !== 'success') {
      return [];
    }

    const { results } = data.artists;
    results.sort((a, b) => a.name.localeCompare(b.name));
    return results;
  }, [status, data]);

  return (
    <div className={className} style={style}>
      <Artist artist={null} active={active} setActive={setActive} />
      {results.map((art) => (
        <Artist key={art.id} artist={art} active={active} setActive={setActive} />
      ))}
    </div>
  );
};

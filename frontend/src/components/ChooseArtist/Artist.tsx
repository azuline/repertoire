import * as React from 'react';
import clsx from 'clsx';
import { ArtistT } from 'src/types';

// Null `artist` means it's the "All" select.

export const Artist: React.FC<{
  artist: ArtistT | null;
  active: number;
  setActive: (arg0: number) => void;
}> = ({ artist, active, setActive }) => {
  const isActive = React.useMemo(
    () => (active === 0 && !artist) || (artist && artist.id === active),
    [active, artist],
  );

  // prettier-ignore
  const onClick = React.useCallback(
    () => setActive(artist ? artist.id : 0),
    [artist, setActive],
  );

  return (
    <div
      className={clsx(
        'pl-4 pr-1 py-1 hover:bg-white hover:bg-opacity-5 cursor-pointer truncate',
        isActive ? 'text-bold font-bold' : '',
      )}
      onClick={onClick}
    >
      {artist ? artist.name : 'All'}
    </div>
  );
};

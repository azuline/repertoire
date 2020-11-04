import * as React from 'react';

import { ArtistT } from 'src/types';
import clsx from 'clsx';

export const ArtistList: React.FC<{
  artists: ArtistT[] | undefined;
  className?: string;
  prefix?: string;
}> = ({ artists, className = '', prefix = '' }) => {
  if (!artists || artists.length === 0) return null;

  return (
    <div className={clsx(className, 'flex')}>
      {prefix && <span>{prefix}&nbsp;</span>}
      {artists.map((art, i) => (
        <span key={art.id}>
          {i > 0 && ', '}
          <a href={`/artists/${art.id}`}>{art.name}</a>
        </span>
      ))}
    </div>
  );
};

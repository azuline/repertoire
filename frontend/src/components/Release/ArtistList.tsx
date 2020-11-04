import * as React from 'react';

import { ArtistT } from 'src/types';
import clsx from 'clsx';

export const ArtistList: React.FC<{ artists: ArtistT[]; className?: string }> = ({
  artists,
  className = '',
}) => {
  return (
    <div className={clsx(className, 'flex')}>
      {artists.map((art, i) => (
        <span key={art.id} className="tag mr-1">
          {i > 0 && ', '}
          <a href={`/artists/${art.id}`}>{art.name}</a>
        </span>
      ))}
    </div>
  );
};

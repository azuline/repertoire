import * as React from 'react';
import { Link } from 'src/components/common/Link';

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
        <React.Fragment key={art.id}>
          {i > 0 && ', '}
          <Link className="truncate" href={`/artists/${art.id}`}>
            {art.name}
          </Link>
        </React.Fragment>
      ))}
    </div>
  );
};

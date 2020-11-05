import * as React from 'react';
import { Link } from 'src/components/common/Link';

import { ArtistT } from 'src/types';

export const ArtistList: React.FC<{
  artists: ArtistT[] | undefined;
  className?: string;
  prefix?: string;
}> = ({ artists, className = '', prefix = '' }) => {
  if (!artists || artists.length === 0) return null;

  return (
    <div className={className}>
      {prefix && <span>{prefix}&nbsp;</span>}
      {artists.map((art, i) => (
        <React.Fragment key={art.id}>
          {i > 0 && <>,&nbsp;</>}
          <Link href={`/artists/${art.id}`}>{art.name}</Link>
        </React.Fragment>
      ))}
    </div>
  );
};

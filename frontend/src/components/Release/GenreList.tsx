import * as React from 'react';

import { CollectionT } from 'src/types';
import clsx from 'clsx';

export const GenreList: React.FC<{
  genres: CollectionT[] | undefined;
  className?: string;
  prefix?: string;
}> = ({ genres, className = '', prefix = '' }) => {
  if (!genres || genres.length === 0) return null;

  return (
    <div className={clsx(className, 'flex')}>
      {prefix && <span>{prefix}&nbsp;</span>}
      {genres.map((grn, i) => (
        <span key={grn.id}>
          {i > 0 && ', '}
          <a href={`/genres/${grn.id}`}>{grn.name}</a>
        </span>
      ))}
    </div>
  );
};

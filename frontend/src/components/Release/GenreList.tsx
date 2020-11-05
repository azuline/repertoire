import * as React from 'react';
import { Link } from 'src/components/common/Link';

import { CollectionT } from 'src/types';

export const GenreList: React.FC<{
  genres: CollectionT[] | undefined;
  className?: string;
  prefix?: string;
}> = ({ genres, className = '', prefix = '' }) => {
  if (!genres || genres.length === 0) return null;

  return (
    <div className={className}>
      {prefix && <span>{prefix}&nbsp;</span>}
      {genres.map((grn, i) => (
        <React.Fragment key={grn.id}>
          {i > 0 && <>,&nbsp;</>}
          <Link href={`/genres/${grn.id}`}>{grn.name}</Link>
        </React.Fragment>
      ))}
    </div>
  );
};

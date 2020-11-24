import * as React from 'react';

import { Link } from 'src/components/common/Link';

type ElementT = { id: number; name: string };
type ListT = React.FC<{
  elements?: ElementT[];
  className?: string;
}>;

export const makeList = (urlPrefix: string): ListT => {
  const ElementList: ListT = ({ elements, className }) => {
    if (!elements || elements.length === 0) return <div>&nbsp;</div>;

    return (
      <div className={className}>
        {elements.map((elem, i) => (
          <React.Fragment key={elem.id}>
            {i > 0 && <>, </>}
            <Link href={`${urlPrefix}/${elem.id}`}>{elem.name}</Link>
          </React.Fragment>
        ))}
      </div>
    );
  };

  return ElementList;
};

export const ArtistList = makeList('/artists');
export const GenreList = makeList('/genres');

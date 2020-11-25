import * as React from 'react';

import { Link } from 'src/components/common/Link';

type ElementT = { id: number; name: string };
type ListT = React.FC<{
  elements?: ElementT[];
  className?: string;
  elementClassName?: string;
  delimiter?: string;
  link?: boolean;
}>;

export const makeList = (urlPrefix: string): ListT => {
  const ElementList: ListT = ({
    elements,
    className,
    elementClassName,
    delimiter = ', ',
    link = false,
  }) => {
    if (!elements || elements.length === 0) return <div>&nbsp;</div>;

    return (
      <div className={className}>
        {elements.map((elem, i) => (
          <React.Fragment key={elem.id}>
            {i > 0 && delimiter}
            {link ? (
              <Link className={elementClassName} href={`${urlPrefix}/${elem.id}`}>
                {elem.name}
              </Link>
            ) : (
              <span className={elementClassName}>{elem.name}</span>
            )}
          </React.Fragment>
        ))}
      </div>
    );
  };

  return ElementList;
};

export const ArtistList = makeList('/artists');
export const GenreList = makeList('/genres');
export const LabelList = makeList('/labels');
export const CollageList = makeList('/collages');

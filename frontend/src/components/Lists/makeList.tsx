import * as React from 'react';

import { IElement } from '~/components/Chooser';
import { Link } from '~/components/common';

type IList = React.FC<{
  className?: string;
  delimiter?: string;
  elements?: IElement[];
  link?: boolean;
}>;

export const makeList = (urlPrefix: string): IList => {
  const ElementList: IList = ({
    className,
    delimiter = ', ',
    elements,
    link = false,
  }) => {
    if (!elements || elements.length === 0) {
      return <div> </div>;
    }

    return (
      <div className={className}>
        {elements.map((elem, i) => (
          <React.Fragment key={elem.id}>
            {i > 0 && delimiter}
            {link ? (
              <Link className="list--element" href={`${urlPrefix}/${elem.id}`}>
                {elem.name}
              </Link>
            ) : (
              <span className="list--element">{elem.name}</span>
            )}
          </React.Fragment>
        ))}
      </div>
    );
  };

  return ElementList;
};

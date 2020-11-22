import * as React from 'react';

import { Link } from 'src/components/common/Link';
import clsx from 'clsx';

export type ElementT = { id: number; name: string };

export const Element: React.FC<{
  element: ElementT;
  active: number | null;
  makeUrl: (arg0: number) => string;
}> = ({ element, active, makeUrl }) => {
  const isActive = React.useMemo(() => element.id === active, [active, element]);

  const url = React.useMemo(() => makeUrl(element.id), [element, makeUrl]);

  return (
    <Link href={url}>
      <div
        className={clsx(
          'pl-8 pr-4 py-1 cursor-pointer truncate',
          isActive
            ? 'bg-primary-alt2'
            : 'hover:bg-black hover:bg-opacity-5 dark:hover:bg-white dark:hover:bg-opacity-5',
        )}
      >
        {element.name}
      </div>
    </Link>
  );
};

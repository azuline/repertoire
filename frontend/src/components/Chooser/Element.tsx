import clsx from 'clsx';
import * as React from 'react';
import { Icon, Link } from 'src/components/common';

export type ElementT = { id: number; name: string; starred?: boolean; type?: string };
export type ToggleStarFactory = (elem: ElementT) => (() => Promise<void>) | undefined;

export const Element: React.FC<{
  element: ElementT;
  active: number | null;
  urlFactory: (arg0: number) => string;
  starrable?: boolean;
  toggleStarFactory: ToggleStarFactory;
}> = ({ element, active, urlFactory, starrable = true, toggleStarFactory }) => {
  const isActive = element.id === active;

  const url = React.useMemo(() => urlFactory(element.id), [element, urlFactory]);
  const toggleStar = React.useMemo(() => toggleStarFactory(element), [toggleStarFactory, element]);

  return (
    <div className="relative">
      {starrable && (
        <div
          className={clsx(
            'absolute top-0 left-0 flex items-center h-full pl-8',
            toggleStar && 'cursor-pointer',
            element.starred ? 'text-primary-500 fill-current' : 'text-gray-500 stroke-current',
            toggleStar &&
              (element.starred
                ? 'hover:text-gray-500 hover:stroke-current'
                : 'hover:text-primary-400 hover:fill-current'),
          )}
          onClick={toggleStar}
        >
          <Icon className="w-4" icon="star-small" />
        </div>
      )}
      <Link href={url}>
        <div
          className={clsx(
            'pr-10 h-8 flex items-center cursor-pointer hover-emph-bg',
            starrable ? 'pl-14' : 'pl-8',
            isActive ? 'font-bold text-primary-400' : 'text-foreground',
          )}
        >
          <div className="min-w-0 truncate">{element.name}</div>
        </div>
      </Link>
    </div>
  );
};

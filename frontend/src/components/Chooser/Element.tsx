import clsx from 'clsx';
import * as React from 'react';
import { Icon, Link } from 'src/components/common';

export type ElementT = { id: number; name: string; starred: boolean; type?: string };
export type ToggleStarFactory = (elem: ElementT) => () => Promise<void>;

export const Element: React.FC<{
  element: ElementT;
  active: number | null;
  urlFactory: (arg0: number) => string;
  toggleStarFactory: ToggleStarFactory;
}> = ({ element, active, urlFactory, toggleStarFactory }) => {
  const isActive = element.id === active;
  const isToggleable = element.type !== 'SYSTEM';

  const url = React.useMemo(() => urlFactory(element.id), [element, urlFactory]);
  const toggleStar = React.useMemo(() => toggleStarFactory(element), [toggleStarFactory, element]);

  return (
    <div className="relative">
      <div
        className={clsx(
          'absolute top-0 left-0 flex items-center h-full pl-8',
          isToggleable && 'cursor-pointer',
          element.starred ? 'text-primary-500 fill-current' : 'text-gray-500 stroke-current',
          isToggleable &&
            (element.starred
              ? 'hover:text-gray-500 hover:fill-transparent hover:stroke-current'
              : 'hover:text-primary-400 hover:fill-current'),
        )}
        onClick={toggleStar}
      >
        <Icon className="w-4" icon="star-small" />
      </div>
      <Link href={url}>
        <div
          className={clsx(
            'pr-10 h-8 flex items-center cursor-pointer pl-14 hover-emph-bg',
            isActive ? 'font-bold text-primary-400' : 'text-foreground',
          )}
        >
          <div className="min-w-0 truncate">{element.name}</div>
        </div>
      </Link>
    </div>
  );
};

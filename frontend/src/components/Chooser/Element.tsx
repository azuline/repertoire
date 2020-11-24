import * as React from 'react';

import { Icon } from 'src/components/common/Icon';
import { Link } from 'src/components/common/Link';
import clsx from 'clsx';

export type ElementT = { id: number; name: string; starred: boolean; type?: string };
export type ToggleStarFactory = (elem: ElementT) => () => Promise<void>;

export const Element: React.FC<{
  element: ElementT;
  active: number | null;
  urlFactory: (arg0: number) => string;
  toggleStarFactory: ToggleStarFactory;
}> = ({ element, active, urlFactory, toggleStarFactory }) => {
  const isActive = React.useMemo(() => element.id === active, [active, element]);
  const isToggleable = React.useMemo(() => element.type !== 'SYSTEM', [element]);

  const url = React.useMemo(() => urlFactory(element.id), [element, urlFactory]);
  const toggleStar = React.useMemo(() => toggleStarFactory(element), [toggleStarFactory, element]);

  return (
    <div className="relative">
      <div
        className={clsx(
          'absolute flex items-center top-0 h-full left-0 pl-8',
          isToggleable && 'cursor-pointer',
          element.starred && 'text-primary-alt3',
          isToggleable && (element.starred ? 'hover:text-foreground' : 'hover:text-primary-alt3'),
        )}
        onClick={toggleStar}
      >
        <Icon className="w-4" icon={element.starred ? 'star-small-filled' : 'star-small-outline'} />
      </div>
      <Link href={url}>
        <div
          className={clsx(
            'pl-14 pr-10 py-1 cursor-pointer truncate hover:bg-black hover:bg-opacity-5 dark:hover:bg-white dark:hover:bg-opacity-5',
            isActive && 'text-primary font-bold',
          )}
        >
          {element.name}
        </div>
      </Link>
    </div>
  );
};

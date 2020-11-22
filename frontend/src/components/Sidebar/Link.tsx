import * as React from 'react';

import clsx from 'clsx';
import { useHistory } from 'react-router-dom';

export const NavLink: React.FC<{
  url: string;
  label: string;
  activeRoute?: string | undefined | null;
  className?: string | undefined;
}> = ({ url, label, activeRoute, className }) => {
  const history = useHistory();
  const handleClick = React.useCallback(() => history.push(url), [history, url]);

  const active = React.useMemo(() => url === activeRoute, [activeRoute, url]);

  return (
    <div
      className={clsx(
        className,
        active ? 'bg-primary-alt' : 'hover:bg-gray-200 hover:bg-opacity-5',
        'text-foreground cursor-pointer',
      )}
      onClick={handleClick}
    >
      {label}
    </div>
  );
};

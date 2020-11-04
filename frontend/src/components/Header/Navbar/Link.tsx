import * as React from 'react';
import clsx from 'clsx';

import { useHistory } from 'react-router-dom';

export const Link: React.FC<{
  children: React.ReactNode;
  url: string;
  activeRoute?: string | undefined;
  className?: string;
  padding?: boolean;
}> = ({ children, url, activeRoute, className = '', padding = true }) => {
  const history = useHistory();
  const handleClick = React.useCallback(() => history.push(url), [history, url]);

  const active = React.useMemo(() => activeRoute && url === activeRoute, [activeRoute, url]);

  return (
    <button
      className={clsx(
        className,
        padding ? 'px-4' : 'px-0',
        active ? 'border-b-2' : '',
        'bg-transparent hover:text-bold font-semibold border-bold rounded-none',
      )}
      onClick={handleClick}
    >
      {children}
    </button>
  );
};

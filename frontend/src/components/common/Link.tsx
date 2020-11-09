import * as React from 'react';

import { useHistory } from 'react-router-dom';

export const Link: React.FC<{
  href: string;
  children: React.ReactNode;
  className?: string | undefined;
  onClick?: () => void | undefined;
}> = ({ href, children, className, onClick }) => {
  const history = useHistory();

  const newOnClick = React.useCallback(
    (event) => {
      event.preventDefault();
      if (onClick) onClick();
      history.push(href);
    },
    [onClick, history, href],
  );

  return (
    <a className={className} onClick={newOnClick} href={href}>
      {children}
    </a>
  );
};

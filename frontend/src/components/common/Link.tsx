import * as React from 'react';
import { useHistory } from 'react-router-dom';
import clsx from 'clsx';

export const Link: React.FC<{ href: string; children: React.ReactNode; className?: string }> = ({
  href,
  children,
  className = '',
}) => {
  const history = useHistory();

  const onClick = React.useCallback(
    (event) => {
      event.preventDefault();
      history.push(href);
    },
    [history, href],
  );

  return (
    <a className={clsx(className, 'cursor-pointer')} onClick={onClick} href={href}>
      {children}
    </a>
  );
};

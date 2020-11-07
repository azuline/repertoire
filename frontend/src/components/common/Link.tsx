import * as React from 'react';

import { useHistory } from 'react-router-dom';

export const Link: React.FC<{
  href: string;
  children: React.ReactNode;
  className?: string | undefined;
}> = ({ href, children, className }) => {
  const history = useHistory();

  const onClick = React.useCallback(
    (event) => {
      event.preventDefault();
      history.push(href);
    },
    [history, href],
  );

  return (
    <a className={className} onClick={onClick} href={href}>
      {children}
    </a>
  );
};

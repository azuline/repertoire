import * as React from 'react';
import CSS from 'csstype';

import { useHistory } from 'react-router-dom';

export const Link: React.FC<{
  href: string;
  children: React.ReactNode;
  className?: string;
  style?: CSS.Properties;
  onClick?: () => void;
}> = ({ href, children, className, style, onClick }) => {
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
    <a className={className} onClick={newOnClick} style={style} href={href}>
      {children}
    </a>
  );
};

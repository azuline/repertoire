import CSS from 'csstype';
import * as React from 'react';
import { useHistory } from 'react-router-dom';

export const Link: React.FC<{
  children: React.ReactNode;
  className?: string;
  href: string;
  onClick?: () => void;
  style?: CSS.Properties;
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
    <a className={className} href={href} style={style} onClick={newOnClick}>
      {children}
    </a>
  );
};

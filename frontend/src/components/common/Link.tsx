import CSS from 'csstype';
import * as React from 'react';
import { useHistory } from 'react-router-dom';

type ILink = React.FC<{
  children: React.ReactNode;
  className?: string;
  href: string;
  onClick?: () => void;
  style?: CSS.Properties;
}>;

export const Link: ILink = ({ href, children, className, style, onClick }) => {
  const history = useHistory();

  const newOnClick = (event: React.MouseEvent<HTMLAnchorElement, MouseEvent>): void => {
    event.preventDefault();
    if (onClick) onClick();
    history.push(href);
  };

  return (
    <a className={className} href={href} style={style} onClick={newOnClick}>
      {children}
    </a>
  );
};

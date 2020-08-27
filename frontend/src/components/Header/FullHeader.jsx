import { Alignment, Button, Navbar } from '@blueprintjs/core';

import { NavLink } from 'react-router-dom';
import React from 'react';
import { ThemeButton } from './ThemeButton';

export const FullHeader = ({ pages, activeRoute }) => {
  return (
    <Navbar className="FullHeader">
      <Navbar.Group align={Alignment.LEFT}>
        {Object.entries(pages).map(([route, { name, icon, exact, hidden }]) => {
          return hidden ? null : (
            <NavLink key={route} to={route} exact={exact}>
              <Button
                icon={icon}
                text={name}
                intent={route === activeRoute ? 'primary' : undefined}
                minimal={route !== activeRoute}
              />
            </NavLink>
          );
        })}
      </Navbar.Group>
      <Navbar.Group align={Alignment.RIGHT}>
        <Navbar.Divider />
        <ThemeButton />
      </Navbar.Group>
    </Navbar>
  );
};

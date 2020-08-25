import { Alignment, Button, Navbar } from '@blueprintjs/core';

import { NavLink } from 'react-router-dom';
import React from 'react';
import { ThemeButton } from './ThemeButton';

export const FullHeader = ({ pages }) => {
  return (
    <Navbar className="FullHeader">
      <Navbar.Group align={Alignment.LEFT}>
        {Object.entries(pages).map(([route, { name, icon, exact, hidden }]) => {
          return hidden ? null : (
            <NavLink key={route} to={route} exact={exact}>
              <Button className="bp3-minimal" icon={icon} text={name} />
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

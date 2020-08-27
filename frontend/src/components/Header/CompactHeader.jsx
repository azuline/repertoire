import { Alignment, Button, MenuItem, Navbar } from '@blueprintjs/core';
import React from 'react';
import { useHistory } from 'react-router-dom';

import { Select } from '@blueprintjs/select';
import { ThemeButton } from './ThemeButton';

export const CompactHeader = ({ pages, activeRoute }) => {
  const history = useHistory();

  const renderPages = ([route, { name, icon, exact }]) => {
    return (
      <MenuItem
        active={route === activeRoute}
        key={route}
        icon={icon}
        text={name}
        onClick={() => history.push(route)}
      />
    );
  };

  const items = Object.entries(pages).filter(([, { hidden }]) => !hidden);

  return (
    <Navbar className="CompactHeader">
      <div className="LinkButton">
        <Select
          className="LinkSelect"
          filterable={false}
          items={items}
          itemRenderer={renderPages}
          popoverProps={{ minimal: true, transitionDuration: 50 }}
          resetOnQuery
        >
          <Button
            text={pages[activeRoute].name}
            icon={pages[activeRoute].icon}
            rightIcon="caret-down"
            minimal
          />
        </Select>
      </div>
      <Navbar.Group align={Alignment.RIGHT}>
        <Navbar.Divider />
        <ThemeButton />
      </Navbar.Group>
    </Navbar>
  );
};

import { Alignment, Button, MenuItem, Navbar } from '@blueprintjs/core';
import React, { useMemo } from 'react';
import { useHistory, useLocation } from 'react-router-dom';

import { Select } from '@blueprintjs/select';
import { ThemeButton } from './ThemeButton';
import { matchPath } from 'react-router';

export const CompactHeader = ({ pages }) => {
  const location = useLocation();
  const history = useHistory();

  const activeRoute = useMemo(() => {
    let [route] =
      Object.entries(pages).find(([route, { exact }]) => {
        return matchPath(location.pathname, { exact: exact, path: route });
      }) ?? '/404';

    return route;
  }, [location, pages]);

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

import * as React from 'react';
import { matchPath } from 'react-router';
import { useLocation } from 'react-router-dom';

import { IRoute, routeSections } from '~/routes';

import { NavLink } from './Link';

export const RouteList: React.FC = () => {
  const location = useLocation();

  const activeRoute = routeSections
    .reduce<IRoute[]>((acc, section) => acc.concat(section.routes), [])
    .find(({ path, exact }) => matchPath(location.pathname, { exact, path }))?.path;

  return (
    <div>
      {routeSections.map(({ name, routes }) => (
        <div key={name} tw="py-3 -mx-6 md:-mx-8">
          {name !== null && (
            <div tw="px-6 pb-6 text-sm uppercase md:px-8 text-primary-400">{name}</div>
          )}
          {routes.map(({ path, label }, i) => (
            <NavLink key={i} activeRoute={activeRoute} label={label} url={path} />
          ))}
        </div>
      ))}
    </div>
  );
};

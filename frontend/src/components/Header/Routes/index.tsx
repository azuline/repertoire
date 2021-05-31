import * as React from 'react';

import { routeSections } from '~/routes';

import { RouteGroup } from './Group';

type IComponent = React.FC<{ className?: string }>;

export const HeaderRoutes: IComponent = ({ className }) => (
  <div className={className}>
    <div tw="flex gap-2">
      {routeSections.map(({ name, routes }) => {
        if (name === null) {
          return routes.map(({ path, label }) => (
            <RouteGroup key={path} href={path} name={label} />
          ));
        }

        return (
          <RouteGroup key={name} href={routes[0].path} name={name}>
            {routes.map(({ path, label }) => {
              return <div key={path}>{label}</div>;
            })}
          </RouteGroup>
        );
      })}
    </div>
  </div>
);

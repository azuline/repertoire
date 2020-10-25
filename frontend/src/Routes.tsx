import * as React from 'react';
import clsx from 'clsx';
import { Releases } from 'src/pages/Releases';
import { Artists } from 'src/pages/Artists';
import { AuthorizationContext } from 'src/contexts';
import { Route, Switch } from 'react-router-dom';
import { Login } from 'src/pages/Login';

const routes = [
  { component: Releases, path: '/' },
  { component: Releases, path: '/releases' },
  { component: Artists, path: '/artists' },
];

export const Routes: React.FC<{ className?: string }> = ({ className = '' }) => {
  const { token } = React.useContext(AuthorizationContext);

  if (!token) {
    return <Login className={className} />;
  }

  return (
    <div className={clsx('Page', className)}>
      <Switch>
        {routes.map((route) => (
          <Route {...route} key={route.path} />
        ))}
      </Switch>
    </div>
  );
};

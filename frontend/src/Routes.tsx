import * as React from 'react';
import clsx from 'clsx';
import { Releases, Artists, Login, Landing } from 'src/pages';
import { AuthorizationContext } from 'src/contexts';
import { Route, Switch } from 'react-router-dom';

const routes = [
  { component: Landing, path: '/' },
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

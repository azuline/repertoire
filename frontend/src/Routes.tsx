import * as React from 'react';
import clsx from 'clsx';
import { Releases } from 'pages/Releases';
import { Artists } from 'pages/Artists';
import { AuthorizationContext } from 'contexts';
import { Route, Switch } from 'react-router-dom';
import { Login } from 'pages/Login';

const routes = [
  { component: Releases, path: '/' },
  { component: Releases, path: '/releases' },
  { component: Artists, path: '/artists' },
];

type RoutesProps = { className: string };

export const Routes: React.FC<RoutesProps> = ({ className }) => {
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

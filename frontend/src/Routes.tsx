import * as React from 'react';

import { Artists, Home, Login, Releases } from 'src/pages';
import { Route, Switch } from 'react-router-dom';

import { AuthorizationContext } from 'src/contexts';

export const Routes: React.FC<{ className?: string }> = ({ className = '' }) => {
  const { token } = React.useContext(AuthorizationContext);

  if (!token) {
    return <Login className={className} />;
  }

  return (
    <div className={className}>
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/releases" component={Releases} />
        <Route path="/artists" component={Artists} />
      </Switch>
    </div>
  );
};

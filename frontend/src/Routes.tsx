import * as React from 'react';

import { Artists, Home, Releases } from 'src/pages';
import { Route, Switch } from 'react-router-dom';

export const Routes: React.FC<{ className?: string }> = ({ className = '' }) => {
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

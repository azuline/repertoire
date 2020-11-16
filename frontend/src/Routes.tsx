import * as React from 'react';

import {
  Artists,
  Collages,
  Genres,
  Home,
  Help,
  Settings,
  Labels,
  Metadata,
  NotFound,
  Release,
  Releases,
} from 'src/pages';
import { Route, Switch } from 'react-router-dom';

export const Routes: React.FC = () => {
  return (
    <Switch>
      <Route path="/" component={Home} exact />
      <Route path="/404" component={NotFound} />
      <Route path="/releases/:id" component={Release} />
      <Route path="/releases" component={Releases} />
      <Route path="/artists/:id" component={Artists} />
      <Route path="/artists" component={Artists} />
      <Route path="/collages" component={Collages} />
      <Route path="/labels" component={Labels} />
      <Route path="/genres" component={Genres} />
      <Route path="/help" component={Help} />
      <Route path="/metadata" component={Metadata} />
      <Route path="/settings" component={Settings} />
    </Switch>
  );
};

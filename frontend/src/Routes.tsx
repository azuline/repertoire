import * as React from 'react';

import {
  Artists,
  Collages,
  Genres,
  Home,
  Labels,
  Metadata,
  NotFound,
  Release,
  Releases,
  Settings,
} from 'src/pages';
import { Route, Switch } from 'react-router-dom';

export const Routes: React.FC = () => (
  <Switch>
    <Route path="/" component={Home} exact />
    <Route path="/404" component={NotFound} />
    <Route path="/releases/:id" component={Release} />
    <Route path="/releases" component={Releases} />
    <Route path="/artists/:id" component={Artists} />
    <Route path="/artists" component={Artists} />
    <Route path="/collages/:id" component={Collages} />
    <Route path="/collages" component={Collages} />
    <Route path="/labels/:id" component={Labels} />
    <Route path="/labels" component={Labels} />
    <Route path="/genres/:id" component={Genres} />
    <Route path="/genres" component={Genres} />
    <Route path="/metadata" component={Metadata} />
    <Route path="/settings" component={Settings} />
  </Switch>
);

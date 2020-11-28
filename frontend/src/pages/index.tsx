import * as React from 'react';
import { Route, Switch } from 'react-router-dom';

import { Artists } from './Artists';
import { Collages } from './Collages';
import { Genres } from './Genres';
import { Home } from './Home';
import { Labels } from './Labels';
import { Metadata } from './Metadata';
import { Mobile } from './Mobile';
import { NotFound } from './NotFound';
import { NowPlaying } from './NowPlaying';
import { Release } from './Release';
import { Releases } from './Releases';
import { Settings } from './Settings';

export * from './Login';

export const Routes: React.FC = () => (
  <div className="z-10 flex-1 min-h-0">
    <Switch>
      <Route path="/" component={Home} exact />
      <Route path="/404" component={NotFound} />
      <Route path="/playing" component={NowPlaying} />
      <Route path="/mobile" component={Mobile} />
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
  </div>
);

import * as React from 'react';
import { Route, Switch } from 'react-router-dom';

import { Artists } from './Artists';
import { Collages } from './Collages';
import { Explore } from './Explore';
import { Genres } from './Genres';
import { Labels } from './Labels';
import { Metadata } from './Metadata';
import { Mobile } from './Mobile';
import { NotFound } from './NotFound';
import { NowPlaying } from './NowPlaying';
import { Playlists } from './Playlists';
import { Release } from './Release';
import { Releases } from './Releases';
import { Settings } from './Settings';

export * from './Login';

export const Routes: React.FC = () => (
  <div className="z-10 flex-1 min-h-0">
    <Switch>
      <Route exact component={Explore} path="/" />
      <Route component={NotFound} path="/404" />
      <Route component={NowPlaying} path="/playing" />
      <Route component={Mobile} path="/mobile" />
      <Route component={Release} path="/releases/:id" />
      <Route component={Releases} path="/releases" />
      <Route component={Artists} path="/artists/:id" />
      <Route component={Artists} path="/artists" />
      <Route component={Collages} path="/collages/:id" />
      <Route component={Collages} path="/collages" />
      <Route component={Labels} path="/labels/:id" />
      <Route component={Labels} path="/labels" />
      <Route component={Genres} path="/genres/:id" />
      <Route component={Genres} path="/genres" />
      <Route component={Playlists} path="/playlists/:id" />
      <Route component={Playlists} path="/playlists" />
      <Route component={Metadata} path="/metadata" />
      <Route component={Settings} path="/settings" />
    </Switch>
  </div>
);

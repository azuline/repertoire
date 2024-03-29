import * as React from 'react';
import { Route, Switch } from 'react-router-dom';

import {
  Artists,
  Collages,
  Explore,
  Genres,
  Invites,
  Labels,
  Metadata,
  Mobile,
  NotFound,
  NowPlaying,
  Playlists,
  Release,
  Releases,
  Settings,
  Years,
} from '~/pages';

export const AuthedRoutes: React.FC = () => {
  return (
    <Switch>
      <Route exact component={Explore} path="/" />
      <Route component={NowPlaying} path="/playing" />
      <Route component={Mobile} path="/mobile" />
      <Route component={Release} path="/releases/:id" />
      <Route component={Releases} path="/releases" />
      <Route component={Artists} path="/artists/:id" />
      <Route component={Artists} path="/artists" />
      <Route component={Labels} path="/labels/:id" />
      <Route component={Labels} path="/labels" />
      <Route component={Genres} path="/genres/:id" />
      <Route component={Genres} path="/genres" />
      <Route component={Years} path="/years/:id" />
      <Route component={Years} path="/years" />
      <Route component={Collages} path="/collages/:id" />
      <Route component={Collages} path="/collages" />
      <Route component={Playlists} path="/playlists/:id" />
      <Route component={Playlists} path="/playlists" />
      <Route component={Invites} path="/invites" />
      <Route component={Metadata} path="/metadata" />
      <Route component={Settings} path="/settings" />
      <Route component={NotFound} path="/" />
    </Switch>
  );
};

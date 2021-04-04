import * as React from 'react';
import { Route, Switch } from 'react-router-dom';

import { FullPageLoading } from '~/components';
import { useHasFirstUser } from '~/hooks';

import { Artists } from './Artists';
import { Collages } from './Collages';
import { NotFound } from './Error';
import { Explore } from './Explore';
import { Genres } from './Genres';
import { Labels } from './Labels';
import { Login } from './Login';
import { Metadata } from './Metadata';
import { Mobile } from './Mobile';
import { NowPlaying } from './NowPlaying';
import { Playlists } from './Playlists';
import { Register } from './Register';
import { Release } from './Release';
import { Releases } from './Releases';
import { Settings } from './Settings';
import { Years } from './Years';

export * from './Error';

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
      <Route component={Metadata} path="/metadata" />
      <Route component={Settings} path="/settings" />
      <Route component={NotFound} path="/" />
    </Switch>
  );
};

export const UnauthedRoutes: React.FC = () => {
  const { hasFirstUser, loading } = useHasFirstUser();

  if (loading) {
    return <FullPageLoading />;
  }

  if (!hasFirstUser) {
    return <Register />;
  }

  return (
    <Switch>
      <Route component={Register} path="/register" />
      <Route component={Login} path="/login" />
      <Route component={Login} path="/" />
    </Switch>
  );
};

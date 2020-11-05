import * as React from 'react';

import { Artists, Home, Releases, Playlists, Collages, Labels, Genres, Metadata } from 'src/pages';
import { Route, Switch } from 'react-router-dom';

export const Routes: React.FC<{ className?: string }> = ({ className = '' }) => {
  return (
    <div className={className}>
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/releases" component={Releases} />
        <Route path="/artists" component={Artists} />
        <Route path="/playlists" component={Playlists} />
        <Route path="/collages" component={Collages} />
        <Route path="/labels" component={Labels} />
        <Route path="/genres" component={Genres} />
        <Route path="/metadata" component={Metadata} />
      </Switch>
    </div>
  );
};

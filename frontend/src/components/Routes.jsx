import { Route, Switch } from 'react-router-dom';

import { ArtistList } from 'components/ArtistList';
import { Login } from 'components/Login';
import { AuthenticationContext } from 'contexts';
import { CollectionList } from 'components/CollectionList';
import { FourOhFour } from 'components/FourOhFour';
import { MetadataEditor } from 'components/MetadataEditor';
import { QueryList } from 'components/QueryList';
import React, { useContext } from 'react';
import { ReleaseList } from 'components/ReleaseList';

const routes = [
  { component: CollectionList, path: '/collections' },
  { component: ArtistList, path: '/artists' },
  { component: QueryList, path: '/queries' },
  { component: MetadataEditor, path: '/metadata' },
  { component: ReleaseList, exact: true, path: '/' },
  { component: FourOhFour, path: '' },
];

export const Routes = () => {
  const { token } = useContext(AuthenticationContext);

  if (!token) {
    return <Login />;
  }

  return (
    <Switch>
      {routes.map((route) => {
        const { path } = route;
        return <Route {...route} key={path} />;
      })}
    </Switch>
  );
};

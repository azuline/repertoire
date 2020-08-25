import { Route, Switch } from 'react-router-dom';

import { ArtistList } from './ArtistList';
import { CollectionList } from './CollectionList';
import { FourOhFour } from './FourOhFour';
import { MetadataEditor } from './MetadataEditor';
import { Queries } from './Queries';
import React from 'react';
import { ReleaseList } from './ReleaseList';

const routes = [
  {
    component: CollectionList,
    path: '/collections',
  },
  {
    component: ArtistList,
    path: '/artists',
  },
  {
    component: Queries,
    path: '/queries',
  },
  {
    component: MetadataEditor,
    path: '/metadata',
  },
  {
    component: ReleaseList,
    exact: true,
    path: '/',
  },
  {
    component: FourOhFour,
    path: '',
  },
];

export const Routes = () => {
  return (
    <Switch>
      {routes.map((route) => {
        const { path } = route;
        return <Route {...route} key={path} />;
      })}
    </Switch>
  );
};

import * as React from 'react';
import { matchPath } from 'react-router';
import { useLocation } from 'react-router-dom';

import { NavLink } from './Link';

type IRoute = { path: string; exact: boolean; label: string };

const sections = [
  {
    name: null,
    routes: [
      { exact: true, label: 'Explore', path: '/' },
      { exact: false, label: 'Now Playing', path: '/playing' },
    ],
  },
  {
    name: 'Library',
    routes: [
      { exact: false, label: 'Releases', path: '/releases' },
      { exact: false, label: 'Artists', path: '/artists' },
      { exact: false, label: 'Genres', path: '/genres' },
      { exact: false, label: 'Labels', path: '/labels' },
      { exact: false, label: 'Years', path: '/years' },
    ],
  },
  {
    name: 'Collections',
    routes: [
      { exact: false, label: 'Collages', path: '/collages' },
      { exact: false, label: 'Playlists', path: '/playlists' },
    ],
  },
  {
    name: 'Admin',
    routes: [{ exact: false, label: 'Invites', path: '/invites' }],
  },
];

export const RouteList: React.FC = () => {
  const location = useLocation();

  const activeRoute = sections
    .reduce<IRoute[]>((acc, section) => acc.concat(section.routes), [])
    .find(({ path, exact }) => matchPath(location.pathname, { exact, path }))?.path;

  return (
    <div>
      {sections.map(({ name, routes }) => (
        <div key={name} tw="py-3 -mx-6 md:-mx-8">
          {name !== null && (
            <div tw="px-6 pb-6 text-sm uppercase md:px-8 text-primary-400">{name}</div>
          )}
          {routes.map(({ path, label }, i) => (
            <NavLink key={i} activeRoute={activeRoute} label={label} url={path} />
          ))}
        </div>
      ))}
    </div>
  );
};

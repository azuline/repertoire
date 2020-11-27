import * as React from 'react';
import { matchPath } from 'react-router';
import { useLocation } from 'react-router-dom';

import { NavLink } from './Link';

type RouteT = { path: string; exact: boolean; label: string };

const sections = [
  {
    name: null,
    routes: [
      { path: '/', exact: true, label: 'Welcome' },
      { path: '/playing', exact: false, label: 'Now Playing' },
    ],
  },
  {
    name: 'Library',
    routes: [
      { path: '/releases', exact: false, label: 'Releases' },
      { path: '/artists', exact: false, label: 'Artists' },
      { path: '/genres', exact: false, label: 'Genres' },
      { path: '/labels', exact: false, label: 'Labels' },
    ],
  },
  {
    name: 'Collections',
    routes: [
      { path: '/collages', exact: false, label: 'Collages' },
      { path: '/playlists', exact: false, label: 'Playlists' },
    ],
  },
  { name: 'Utilities', routes: [{ path: '/metadata', exact: false, label: 'Metadata Tools' }] },
];

export const RouteList: React.FC = () => {
  const location = useLocation();

  const activeRoute = React.useMemo(() => {
    const active = sections
      .reduce<RouteT[]>((acc, section) => acc.concat(section.routes), [])
      .find(({ path, exact }) => matchPath(location.pathname, { path, exact }));

    return active ? active.path : null;
  }, [location]);

  return (
    <div>
      {sections.map(({ name, routes }) => (
        <div key={name} className="py-4">
          {name && <div className="px-8 pb-4 text-sm uppercase text-primary-alt3">{name}</div>}
          {routes.map(({ path, label }, i) => (
            <NavLink
              key={i}
              className="px-8 py-2"
              url={path}
              activeRoute={activeRoute}
              label={label}
            />
          ))}
        </div>
      ))}
    </div>
  );
};

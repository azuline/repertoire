import * as React from 'react';
import { matchPath } from 'react-router';
import { useHistory, useLocation } from 'react-router-dom';
import { Icon } from 'src/components/common';
import { Searchbar } from 'src/components/Header/Searchbar';
import { User } from 'src/components/Header/User';
import { SidebarContext } from 'src/contexts';

import { NavLink } from './Link';

type RouteT = { path: string; exact: boolean; label: string };

const unsortedRoutes = [
  { path: '/', exact: true, label: 'Home' },
  { path: '/playing', exact: false, label: 'Now Playing' },
];

const libraryRoutes = [
  { path: '/releases', exact: false, label: 'Releases' },
  { path: '/artists', exact: false, label: 'Artists' },
  { path: '/genres', exact: false, label: 'Genres' },
  { path: '/labels', exact: false, label: 'Labels' },
];

const collectionRoutes = [
  { path: '/collages', exact: false, label: 'Collages' },
  { path: '/playlists', exact: false, label: 'Playlists' },
];

const utilRoutes = [{ path: '/metadata', exact: false, label: 'Metadata Tools' }];

const sections = [
  { name: null, routes: unsortedRoutes },
  { name: 'Library', routes: libraryRoutes },
  { name: 'Collections', routes: collectionRoutes },
  { name: 'Utilities', routes: utilRoutes },
];

export const Sidebar: React.FC = () => {
  const location = useLocation();
  const history = useHistory();
  const { isSidebarOpen, setSidebarOpen } = React.useContext(SidebarContext);

  const activeRoute = React.useMemo(() => {
    const active = sections
      .reduce<RouteT[]>((acc, section) => acc.concat(section.routes), [])
      .find(({ path, exact }) => matchPath(location.pathname, { path, exact }));

    return active ? active.path : null;
  }, [location]);

  const goHome = React.useCallback(() => history.push('/'), [history]);
  const toggleOpen = React.useCallback(() => setSidebarOpen((o) => !o), [setSidebarOpen]);

  if (!isSidebarOpen) return null;

  return (
    <div className="sticky top-0 flex flex-col flex-none w-full h-full bg-background-alt2 sm:w-56">
      <div className="my-6">
        <div className="flex items-center pl-6 pr-8 sm:pr-4">
          <div className="flex items-center pr-4 cursor-pointer" onClick={goHome}>
            <Icon className="w-8 text-primary" icon="logo" />
            <div className="ml-2 font-semibold">
              <span className="text-primary">reper</span>toire
            </div>
          </div>
          <Icon
            icon="hamburger"
            className="flex-none hidden w-6 ml-auto cursor-pointer sm:block"
            onClick={toggleOpen}
          />
          <User className="ml-auto sm:hidden" />
        </div>
      </div>
      <Searchbar className="flex-none block h-16 mx-8 mb-4 sm:hidden" shrink={false} />
      {sections.map(({ name, routes }) => (
        <div key={name} className="my-6">
          {name && <div className="px-8 mb-4 text-sm uppercase text-primary-alt3">{name}</div>}
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

import * as React from 'react';
import { User } from 'src/components/Header/User';
import { Searchbar } from 'src/components/Header/Searchbar';

import { useHistory, useLocation } from 'react-router-dom';

import { Icon } from 'src/components/common/Icon';
import { NavLink } from './Link';
import { SidebarContext } from 'src/contexts';
import { matchPath } from 'react-router';

type RouteT = { path: string; exact: boolean; label: string };

const homeRoute = { path: '/', exact: true, label: 'Home' };

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
  { name: 'Library', routes: libraryRoutes },
  { name: 'Collections', routes: collectionRoutes },
  { name: 'Utilities', routes: utilRoutes },
];

export const Sidebar: React.FC = () => {
  const location = useLocation();
  const history = useHistory();
  const { openBar, setOpenBar } = React.useContext(SidebarContext);

  const activeRoute = React.useMemo(() => {
    const active = sections
      .reduce<RouteT[]>((acc, section) => acc.concat(section.routes), [homeRoute])
      .find(({ path, exact }) => matchPath(location.pathname, { path, exact }));

    return active ? active.path : null;
  }, [location]);

  const goHome = React.useCallback(() => history.push('/'), [history]);
  const toggleOpen = React.useCallback(() => setOpenBar((o) => !o), [setOpenBar]);

  if (!openBar) return null;

  return (
    <div className="h-full flex-none sticky bg-background-alt2 top-0 flex flex-col w-full sm:w-56">
      <div className="my-6">
        <div className="flex items-center pl-6 pr-4 cursor-pointer">
          <div className="flex items-center flex-1" onClick={goHome}>
            <Icon className="text-primary w-8" icon="logo" />
            <div className="font-semibold ml-2">
              <span className="text-primary">reper</span>toire
            </div>
          </div>
          <Icon
            icon="hamburger"
            className="flex-none ml-auto w-6 pointer-cursor hidden sm:block"
            onClick={toggleOpen}
          />
          <User className="sm:hidden" />
        </div>
      </div>
      <Searchbar className="flex-none block sm:hidden h-16 mb-4 mx-8" shrink={false} />
      <NavLink className="py-2 px-8" url={'/'} activeRoute={activeRoute} label={'Home'} />
      {sections.map(({ name, routes }) => (
        <div key={name} className="my-6">
          <div className="mb-4 px-8 text-primary-alt3 text-sm uppercase">{name}</div>
          {routes.map(({ path, label }, i) => (
            <NavLink
              key={i}
              className="py-2 px-8"
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

import * as React from 'react';

import { NavLink } from './NavLink';
import { Link } from 'src/components/common/Link';
import { useLocation } from 'react-router-dom';
import { Icon } from 'src/components/common/Icon';
import { matchPath } from 'react-router';

const routes = [
  { route: '/releases', exact: false },
  { route: '/artists', exact: false },
  { route: '/labels', exact: false },
  { route: '/genres', exact: false },
];

export const Navbar: React.FC = () => {
  const location = useLocation();

  const activeRoute = React.useMemo(() => {
    const { route } = routes.find(({ route, exact }) => {
      return matchPath(location.pathname, { exact: exact, path: route });
    }) ?? { route: '/404' };

    return route;
  }, [location]);

  return (
    <div className="relative w-full h-24 mb-2">
      <Link className="my-2 absolute z-10 left-1/2 -ml-10" href="/">
        <Icon className="text-bold w-20" icon="logo" />
      </Link>
      <div className="absolute right-1/2 flex justify-end w-1/2 pr-10 h-20 my-2 ml-12">
        <NavLink url="/releases" activeRoute={activeRoute}>
          Releases
        </NavLink>
        <NavLink url="/artists" activeRoute={activeRoute}>
          Artists
        </NavLink>
        <NavLink url="/genres" activeRoute={activeRoute}>
          Genres
        </NavLink>
        <NavLink url="/labels" activeRoute={activeRoute}>
          Labels
        </NavLink>
      </div>
      <div className="absolute left-1/2 flex w-1/2 pl-10 h-20 my-2 mr-12">
        <NavLink url="/collages" activeRoute={activeRoute}>
          Collages
        </NavLink>
        <NavLink url="/playlists" activeRoute={activeRoute}>
          Playlists
        </NavLink>
        <NavLink url="/history" activeRoute={activeRoute}>
          History
        </NavLink>
        <NavLink url="/tools" activeRoute={activeRoute}>
          <div className="flex items-center">
            Tools
            <Icon className="w-4 ml-1" icon="chevron-down-small" />
          </div>
        </NavLink>
      </div>
    </div>
  );
};

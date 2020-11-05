import * as React from 'react';

import { NavLink } from './Link';
import { useLocation } from 'react-router-dom';
import { Icon } from 'src/components/common/Icon';
import { matchPath } from 'react-router';

// TODO: At a certain breakpoint, turn these into the same kind of thing from earlier version.

const routes = [
  { route: '/releases' },
  { route: '/artists' },
  { route: '/playlists' },
  { route: '/collages' },
  { route: '/labels' },
  { route: '/genres' },
];

export const Navbar: React.FC = () => {
  const location = useLocation();

  const activeRoute = React.useMemo(() => {
    const { route } = routes.find(({ route }) => matchPath(location.pathname, { path: route })) ?? {
      route: '/404',
    };

    return route;
  }, [location]);

  return (
    <div className="relative w-11/12 mx-auto h-20 font-semibold">
      <NavLink className="absolute z-10 left-1/2 my-2 -ml-8" padding={false} url="/">
        <Icon className="text-bold w-16" icon="logo" />
      </NavLink>
      <div className="absolute right-1/2 flex w-1/2 max-w-sm pr-10 h-16 my-2 ml-8">
        <NavLink className="flex-1" url="/releases" activeRoute={activeRoute}>
          Releases
        </NavLink>
        <NavLink className="flex-1" url="/artists" activeRoute={activeRoute}>
          Artists
        </NavLink>
        <NavLink className="flex-1" url="/playlists" activeRoute={activeRoute}>
          Playlists
        </NavLink>
      </div>
      <div className="absolute left-1/2 flex w-1/2 max-w-sm pl-10 h-16 my-2 mr-8">
        <NavLink className="flex-1" url="/collages" activeRoute={activeRoute}>
          Collages
        </NavLink>
        <NavLink className="flex-1" url="/labels" activeRoute={activeRoute}>
          Labels
        </NavLink>
        <NavLink className="flex-1" url="/genres" activeRoute={activeRoute}>
          Genres
        </NavLink>
      </div>
    </div>
  );
};

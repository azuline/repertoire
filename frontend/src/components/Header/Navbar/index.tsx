import * as React from 'react';

import { NavLink } from './Link';
import { useLocation } from 'react-router-dom';
import { Icon } from 'src/components/common/Icon';
import { matchPath } from 'react-router';

// TODO: At a certain breakpoint, turn these into the same kind of thing from earlier version.

const routes = [
  { route: '/home', label: 'Home' },
  { route: '/releases', label: 'Releases' },
  { route: '/artists', label: 'Artists' },
  { route: '/playlists', label: 'Playlists' },
  { route: '/collages', label: 'Collages' },
  { route: '/labels', label: 'Labels' },
  { route: '/genres', label: 'Genres' },
  { route: '/metadata', label: 'Metadata' },
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
      <div className="absolute right-1/2 flex w-1/2 max-w-md pr-10 h-16 my-2 ml-8">
        {routes.slice(0, 4).map(({ route, label }, i) => (
          <NavLink key={i} className="flex-1" url={route} activeRoute={activeRoute}>
            {label}
          </NavLink>
        ))}
      </div>
      <div className="absolute left-1/2 flex w-1/2 max-w-md pl-10 h-16 my-2 mr-8">
        {routes.slice(4, 8).map(({ route, label }, i) => (
          <NavLink key={i} className="flex-1" url={route} activeRoute={activeRoute}>
            {label}
          </NavLink>
        ))}
      </div>
    </div>
  );
};

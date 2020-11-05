import * as React from 'react';

import { Icon } from 'src/components/common/Icon';
import { NavLink } from './Link';
import { matchPath } from 'react-router';
import { useLocation } from 'react-router-dom';

// TODO: At a certain breakpoint, turn these into the same kind of thing from earlier version.

const routes = [
  { path: '/', exact: true, label: 'Home' },
  { path: '/releases', exact: false, label: 'Releases' },
  { path: '/artists', exact: false, label: 'Artists' },
  { path: '/playlists', exact: false, label: 'Playlists' },
  { path: '/collages', exact: false, label: 'Collages' },
  { path: '/labels', exact: false, label: 'Labels' },
  { path: '/genres', exact: false, label: 'Genres' },
  { path: '/metadata', exact: false, label: 'Metadata' },
];

export const Navbar: React.FC = () => {
  const location = useLocation();

  const activeRoute = React.useMemo(() => {
    const { path } = routes.find(({ path, exact }) =>
      matchPath(location.pathname, { path, exact }),
    ) ?? {
      path: '/404',
    };

    return path;
  }, [location]);

  return (
    <div className="relative w-11/12 mx-auto h-20 font-semibold">
      <NavLink className="absolute z-10 left-1/2 my-2 -ml-8" padding={false} url="/">
        <Icon className="text-bold w-16" icon="logo" />
      </NavLink>
      <div className="absolute right-1/2 flex w-1/2 max-w-md pr-10 h-16 my-2 ml-8">
        {routes.slice(0, 4).map(({ path, label }, i) => (
          <NavLink key={i} className="flex-1" url={path} activeRoute={activeRoute}>
            {label}
          </NavLink>
        ))}
      </div>
      <div className="absolute left-1/2 flex w-1/2 max-w-md pl-10 h-16 my-2 mr-8">
        {routes.slice(4, 8).map(({ path, label }, i) => (
          <NavLink key={i} className="flex-1" url={path} activeRoute={activeRoute}>
            {label}
          </NavLink>
        ))}
      </div>
    </div>
  );
};

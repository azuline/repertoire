import * as React from 'react';

import { Link } from './Link';
import { useLocation } from 'react-router-dom';
import { Icon } from 'src/components/common/Icon';
import { matchPath } from 'react-router';

const routes = [
  { route: '/releases', exact: false },
  { route: '/artists', exact: false },
  { route: '/playlists', exact: false },
  { route: '/collages', exact: false },
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
    <div className="relative w-full h-20">
      <Link className="absolute z-10 left-1/2 -ml-8" padding={false} url="/">
        <Icon className="text-bold w-16" icon="logo" />
      </Link>
      <div className="absolute right-1/2 flex w-1/2 max-w-sm pr-10 h-16 my-2 ml-8">
        <Link className="flex-1" url="/releases" activeRoute={activeRoute}>
          Releases
        </Link>
        <Link className="flex-1" url="/artists" activeRoute={activeRoute}>
          Artists
        </Link>
        <Link className="flex-1" url="/playlists" activeRoute={activeRoute}>
          Playlists
        </Link>
      </div>
      <div className="absolute left-1/2 flex w-1/2 max-w-sm pl-10 h-16 my-2 mr-8">
        <Link className="flex-1" url="/collages" activeRoute={activeRoute}>
          Collages
        </Link>
        <Link className="flex-1" url="/labels" activeRoute={activeRoute}>
          Labels
        </Link>
        <Link className="flex-1" url="/genres" activeRoute={activeRoute}>
          Genres
        </Link>
      </div>
    </div>
  );
};

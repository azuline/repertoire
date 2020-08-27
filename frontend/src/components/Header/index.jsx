import './index.scss';

import React, { useMemo } from 'react';

import { CompactHeader } from './CompactHeader';
import { FullHeader } from './FullHeader';
import { matchPath } from 'react-router';
import { useLocation } from 'react-router-dom';

/* eslint-disable */
const pages = {
  '/': { name: 'Releases', icon: 'music', exact: true },
  '/collections': { name: 'Collections', icon: 'projects' },
  '/artists': { name: 'Artists', icon: 'people' },
  '/queries': { name: 'Queries', icon: 'search' },
  '/metadata': { name: 'Metadata', icon: 'annotation' },
  '/404': { name: '404', icon: 'help', hidden: true },
};
/* eslint-enable */

export const Header = () => {
  const location = useLocation();

  const activeRoute = useMemo(() => {
    let [route] =
      Object.entries(pages).find(([route, { exact }]) => {
        return matchPath(location.pathname, { exact: exact, path: route });
      }) ?? '/404';

    return route;
  }, [location]);

  return (
    <div className="Header">
      <FullHeader pages={pages} activeRoute={activeRoute} />
      <CompactHeader pages={pages} activeRoute={activeRoute} />
    </div>
  );
};

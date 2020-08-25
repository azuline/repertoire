import './index.scss';

import { CompactHeader } from './CompactHeader';
import { FullHeader } from './FullHeader';
import React from 'react';

/* eslint-disable */
const pages = {
  '/': { name: 'Releases', icon: 'music', exact: true },
  '/collections': { name: 'Collections', icon: 'projects' },
  '/artists': { name: 'Artists', icon: 'people' },
  '/queries': { name: 'Queries', icon: 'search' },
  '/metadata': { name: 'Metadata', icon: 'annotation' },
  '/404': {name: '404', icon: 'help', hidden: true },
};
/* eslint-enable */

export const Header = () => {
  return (
    <div className="Header">
      <FullHeader pages={pages} />
      <CompactHeader pages={pages} />
    </div>
  );
};

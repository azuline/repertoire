import * as React from 'react';

import { Link } from './Link';

export const Navbar: React.FC = () => {
  return (
    <div className="flex-1 flex">
      <Link name="Home" url="/" />
      <Link name="Releases" url="/releases" />
      <Link name="Artists" url="/artists" />
    </div>
  );
};

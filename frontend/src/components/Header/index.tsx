import * as React from 'react';

import { Navbar } from './Navbar';
import { Searchbar } from './Searchbar';
import { User } from './User';
import clsx from 'clsx';

export const Header: React.FC<{ className?: string | undefined }> = ({ className }) => {
  return (
    <>
      <div className={clsx(className, 'flex items-center w-full h-16 px-6')}>
        <Searchbar className="mr-6" />
        <User />
      </div>
      <Navbar />
    </>
  );
};

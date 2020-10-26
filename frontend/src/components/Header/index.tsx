import * as React from 'react';
import { Navbar } from './Navbar';
import { Searchbar } from './Searchbar';

export const Header: React.FC = () => {
  return (
    <div className="main-bar border-b-2 flex">
      <Navbar />
      <Searchbar />
    </div>
  );
};

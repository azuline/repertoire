import * as React from 'react';
import { useHistory } from 'react-router-dom';
import { Icon } from 'src/components/common';
import { RouteList } from 'src/components/Routelist';
import { SidebarContext } from 'src/contexts';

export const Sidebar: React.FC = () => {
  const history = useHistory();
  const { isSidebarOpen, setSidebarOpen } = React.useContext(SidebarContext);

  const goHome = (): void => history.push('/');
  const toggleOpen = (): void => setSidebarOpen((o) => !o);

  if (!isSidebarOpen) return null;

  return (
    <div
      className="sticky top-0 flex-col flex-none hidden w-56 bg-background-900 sm:flex"
      style={{ height: 'calc(100vh - 4rem)' }}
    >
      <div className="mt-6 mb-4">
        <div className="flex items-center pl-6 pr-4">
          <div className="flex items-center pr-4 cursor-pointer" onClick={goHome}>
            <Icon className="w-8 text-primary-500" icon="logo" />
            <div className="ml-2 font-semibold">
              <span className="text-primary-500">reper</span>toire
            </div>
          </div>
          <Icon
            className="flex-none block w-6 ml-auto cursor-pointer hover:text-primary-400 text-primary-500"
            icon="hamburger"
            onClick={toggleOpen}
          />
        </div>
      </div>
      <div className="px-6 overflow-y-auto md:px-8">
        <RouteList />
      </div>
    </div>
  );
};

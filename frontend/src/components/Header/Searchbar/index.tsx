import * as React from 'react';
import clsx from 'clsx';
import { Icon } from 'src/components/common/Icon';

// TODO: Implement a dropdown and stuff...

export const Searchbar: React.FC<{
  className?: string;
  focus: boolean;
  setFocus: (arg0: boolean) => void;
}> = ({ className = '', focus, setFocus }) => {
  const focusOn = React.useCallback(() => setFocus(true), [setFocus]);
  const focusOff = React.useCallback(() => setFocus(false), [setFocus]);

  return (
    <div className={clsx(className, focus ? 'flex-1' : '', 'w-64 relative')}>
      <div
        className="absolute top-0 right-0 full flex items-center w-full"
        onFocus={focusOn}
        onBlur={focusOff}
      >
        <input className="w-full pl-8 py-1 bg-bg-alt border-bg-embellish" placeholder="Search" />
        <div className="h-full absolute top-0 left-0 flex items-center pl-2 pr-1 pointer-events-none">
          <Icon icon="search-medium" className="w-5 text-bold" />
        </div>
      </div>
    </div>
  );
};

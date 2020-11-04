import * as React from 'react';
import clsx from 'clsx';
import { fetchUser } from 'src/lib';
import { Icon } from 'src/components/common/Icon';

// const arrowStyle = { transform: 'translate(50%, 50%) rotate(45deg)' };
const arrowStyle = {
  borderColor: 'transparent var(--color-bg-embellish) var(--color-bg-embellish) transparent',
};

export const User: React.FC<{ className?: string }> = ({ className }) => {
  const { status, data } = fetchUser();

  return (
    <div className={clsx(className, 'hover-pop-2nd-child')}>
      <button className="flex h-full items-center p-0 font-normal rounded-none">
        <Icon className="w-5 mr-2 text-bold" icon="user-large" />
        <div>{status === 'success' && data ? data.user.username : 'Loading...'}</div>
        <Icon className="w-4 ml-1" icon="chevron-down-small" />
      </button>
      <div className="relative z-40">
        <div className="absolute right-0 mr-1 border-8" style={arrowStyle} />
        <div className="absolute right-0 pt-3 z-10">
          <button className="px-4 py-2 border-highlight border-2 font-normal flex items-center bg-bg hover:bg-highlight">
            <Icon className="mr-1 w-4 text-bold" icon="logout-small" />
            <span>Logout!</span>
          </button>
        </div>
      </div>
    </div>
  );
};

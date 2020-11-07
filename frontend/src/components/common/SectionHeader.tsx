import * as React from 'react';

import clsx from 'clsx';

export const SectionHeader: React.FC<{
  children: React.ReactNode;
  className?: string;
  onClick?: () => void | undefined;
}> = ({ children, className = '', onClick }) => {
  return (
    <div className={clsx(className, 'mb-8')} onClick={onClick}>
      <span className="font-semibold text-2xl">{children}</span>
    </div>
  );
};

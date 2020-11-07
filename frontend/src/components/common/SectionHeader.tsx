import * as React from 'react';
import clsx from 'clsx';

export const SectionHeader: React.FC<{
  children: React.ReactNode;
  className?: string;
  onClick?: () => void | undefined;
}> = ({ children, className = '', onClick }) => {
  return (
    <div className={clsx(className, 'font-semibold text-3xl')} onClick={onClick}>
      {children}
    </div>
  );
};

import * as React from 'react';
import clsx from 'clsx';

export const SectionHeader: React.FC<{ children: React.ReactNode; className?: string }> = ({
  children,
  className = '',
}) => {
  return (
    <div className={clsx(className, 'mb-8')}>
      <span className="font-semibold text-3xl">{children}</span>
    </div>
  );
};

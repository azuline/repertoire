import clsx from 'clsx';
import * as React from 'react';

export const SectionHeader: React.FC<{
  children: React.ReactNode;
  className?: string;
}> = ({ children, className }) => (
  <div className={clsx(className, 'text-3xl font-semibold')}>{children}</div>
);

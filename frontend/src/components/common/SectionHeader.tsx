import clsx from 'clsx';
import * as React from 'react';

export const SectionHeader: React.FC<{
  children: React.ReactNode;
  className?: string;
}> = ({ children, className }) => (
  <div className={clsx(className, 'font-semibold text-3xl')}>{children}</div>
);

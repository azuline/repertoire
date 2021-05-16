import React from 'react';

type ISectionHeader = React.FC<{
  children: React.ReactNode;
  className?: string;
}>;

export const SectionHeader: ISectionHeader = ({ children, className }) => (
  <div className={className} tw="text-2xl sm:text-3xl font-semibold">
    {children}
  </div>
);

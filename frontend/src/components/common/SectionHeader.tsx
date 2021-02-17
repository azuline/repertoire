import 'twin.macro';

import * as React from 'react';

export const SectionHeader: React.FC<{
  children: React.ReactNode;
  className?: string;
}> = ({ children, className }) => (
  <div className={className} tw="text-2xl sm:text-3xl font-semibold">
    {children}
  </div>
);

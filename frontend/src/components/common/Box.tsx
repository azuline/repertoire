import * as React from 'react';

type BoxProps = { children: React.ReactNode };

export const Box: React.FC<BoxProps> = ({ children }) => {
  return <div className="Box">{children}</div>;
};

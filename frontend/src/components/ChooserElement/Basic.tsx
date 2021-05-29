import * as React from 'react';
import tw from 'twin.macro';

type IComponent = React.FC<{
  children: React.ReactNode;
  isActive: boolean;
}>;

/**
 * Element is a row component for a chooser element. It should be wrapped in a
 * hyperlink.
 */
export const BasicElement: IComponent = ({ children, isActive }) => (
  <div
    css={[
      tw`flex items-center h-8 pr-8 pl-6 md:pl-8 cursor-pointer md:pr-10 hover-bg`,
      isActive ? tw`font-bold text-primary-400` : tw`text-foreground-50`,
    ]}
  >
    <div tw="min-w-0 truncate">{children}</div>
  </div>
);

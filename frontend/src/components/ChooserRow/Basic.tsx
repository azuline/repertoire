import * as React from 'react';
import tw from 'twin.macro';

import { IElement } from '~/components/Chooser';

type IComponent = React.FC<{
  className?: string;
  element: IElement;
  isActive: boolean;
}>;

/**
 * BasicChooserRow is a row component for a chooser element. This is purely
 * presentational--it does not handle redirects.
 */
export const BasicChooserRow: IComponent = ({ className, element, isActive }) => (
  <div
    className={className}
    css={[
      tw`flex items-center h-8 pr-8 md:pr-10 pl-6 md:pl-8 cursor-pointer hover-bg`,
      isActive ? tw`font-bold text-primary-400` : tw`text-foreground-50`,
    ]}
  >
    <div tw="min-w-0 truncate">{element.name}</div>
  </div>
);

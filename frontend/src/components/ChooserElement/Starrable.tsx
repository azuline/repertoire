import * as React from 'react';
import tw from 'twin.macro';

import { Icon, Link } from '~/components/common';

import { BasicElement } from './Basic';

type IElementProps = React.ComponentProps<typeof BasicElement>;

type IComponent = React.FC<
  IElementProps & {
    starred: boolean;
    onToggle: () => Promise<void>;
    url: string;
  }
>;

/**
 * StarrableElement is a version of Element that displays the `starred` property and
 * allows toggling the star. This component handles the hyperlink.
 */
export const StarrableElement: IComponent = ({
  children,
  starred,
  isActive,
  onToggle,
  url,
}) => {
  return (
    <div tw="relative">
      <div
        css={[
          tw`absolute top-0 left-0 flex items-center h-full pl-6 md:pl-8`,
          tw`cursor-pointer`,
          starred === true
            ? tw`text-primary-500 fill-current hover:(text-gray-500 stroke-current)`
            : tw`text-gray-500 stroke-current hover:(text-primary-400 fill-current)`,
        ]}
        onClick={onToggle}
      >
        <Icon icon="star-small" tw="w-4" />
      </div>
      <Link href={url}>
        <BasicElement isActive={isActive}>{children}</BasicElement>
      </Link>
    </div>
  );
};

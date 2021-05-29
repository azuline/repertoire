import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { Icon, Link } from '~/components/common';

import { BasicChooserRow } from './Basic';

type IComponent = React.FC<
  React.ComponentProps<typeof BasicChooserRow> & {
    onToggle: () => Promise<void>;
    url: string;
  }
>;

/**
 * StarrableChooserRow is a version of Element that displays the `starred` property and
 * allows toggling the star. This component is responsible for rendering the redirect
 * hyperlink.
 */
export const StarrableChooserRow: IComponent = ({
  element,
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
          element.starred === true
            ? tw`text-primary-500 fill-current hover:(text-gray-500 stroke-current)`
            : tw`text-gray-500 stroke-current hover:(text-primary-400 fill-current)`,
        ]}
        onClick={onToggle}
      >
        <Icon icon="star-small" tw="w-4" />
      </div>
      <Link href={url}>
        <StyledRow element={element} isActive={isActive} />
      </Link>
    </div>
  );
};

const StyledRow = styled(BasicChooserRow)`
  ${tw`pl-12 md:pl-14`}
`;

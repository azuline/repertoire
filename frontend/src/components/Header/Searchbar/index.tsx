import React from 'react';
import tw, { styled } from 'twin.macro';

import { Icon, Input } from '~/components/common';

// TODO: Implement a dropdown and stuff... get a way to monitor searchbar focus in react
// and use that for width/whatnot.

type ISearchbar = React.FC<{
  className?: string;
  shrink?: boolean;
}>;

export const Searchbar: ISearchbar = ({ className, shrink = true }) => (
  <div className={className} tw="flex-1">
    <div tw="relative flex items-center h-full">
      <SearchbarInput
        css={shrink && tw`max-w-xs focus:max-w-none`}
        placeholder="Search"
      />
      <div
        css={[
          tw`absolute top-0 left-0 h-full pl-2 pr-1`,
          tw`flex items-center pointer-events-none`,
        ]}
      >
        <Icon icon="search-medium" tw="w-5 text-primary-400" />
      </div>
    </div>
  </div>
);

const SearchbarInput = styled(Input)`
  ${tw`w-full pl-9`}

  &::placeholder {
    opacity: 70%;
  }
`;

import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { Icon, Input } from '~/components/common';

type ISearchbar = React.FC<{
  className?: string;
}>;

export const Searchbar: ISearchbar = ({ className }) => (
  <div className={className}>
    <div tw="relative flex items-center h-full">
      <SearchbarInput placeholder="Search" />
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
  ${tw`w-64 pl-9`}

  &::placeholder {
    opacity: 70%;
  }
`;

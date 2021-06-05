import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { Icon, Input, Link } from '~/components/common';

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

export const SearchbarIcon: ISearchbar = ({ className }) => (
  <Link className={className} href="/search" tw="p-2 hover-bg rounded cursor-pointer">
    <Icon icon="search-medium" tw="w-6 hover:text-primary-400 text-primary-500" />
  </Link>
);

const SearchbarInput = styled(Input)`
  ${tw`w-64 pl-9`}

  &::placeholder {
    opacity: 70%;
  }
`;

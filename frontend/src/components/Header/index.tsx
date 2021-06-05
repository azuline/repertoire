import * as React from 'react';
import tw from 'twin.macro';

import { Icon, Link } from '~/components/common';
import { Searchbar, SearchbarIcon } from '~/components/Searchbar';

import { HeaderRoutes } from './Routes';
import { User } from './User';

export { User };

export const Header: React.FC = () => (
  <>
    <FullHeader />
    <MobileHeader />
  </>
);

export const FullHeader: React.FC = () => (
  <HeaderWrapper tw="hidden md:flex">
    <Link href="/" tw="flex items-center mr-4">
      <Icon icon="logo" tw="w-8 text-primary-500" />
      <div tw="mx-2 font-semibold">
        <span tw="text-primary-500">reper</span>toire
      </div>
    </Link>
    <HeaderRoutes />
    <Searchbar tw="hidden lg:block ml-auto mr-10" />
    <SearchbarIcon tw="lg:hidden ml-auto mr-4" />
    <User tw="flex" />
  </HeaderWrapper>
);

export const MobileHeader: React.FC = () => (
  <HeaderWrapper tw="md:hidden relative">
    <div tw="absolute left-1/2 transform -translate-x-1/2">
      <Link href="/" tw="flex items-center">
        <Icon icon="logo" tw="w-9 text-primary-500" />
      </Link>
    </div>
    <Link
      href="/mobile"
      tw="mr-4 flex items-center cursor-pointer hover:text-primary-400 text-primary-500"
    >
      <Icon icon="chevron-left-small" tw="w-8" />
      Go Back
    </Link>
    <SearchbarIcon tw="ml-auto mr-4" />
    <User tw="flex" />
  </HeaderWrapper>
);

const HeaderWrapper = tw.div`
  flex
  items-center
  flex-none
  w-full
  h-16
  px-6
  border-b-2
  border-background-950
  bg-background-700
  md:px-8
`;

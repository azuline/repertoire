import * as React from 'react';
import tw from 'twin.macro';

import { Icon, Link } from '~/components/common';
import { Searchbar } from '~/components/Searchbar';

import { HeaderRoutes } from './Routes';
import { User } from './User';

export { User };

export const Header: React.FC = () => (
  <div
    css={[
      tw`flex items-center flex-none w-full h-16 px-6 md:px-8`,
      tw`border-b-2 border-background-950 bg-background-700`,
    ]}
  >
    <Link href="/" tw="flex items-center mr-4">
      <Icon icon="logo" tw="w-8 text-primary-500" />
      <div tw="mx-2 font-semibold">
        <span tw="text-primary-500">reper</span>toire
      </div>
    </Link>
    <Link href="/mobile" tw="block md:hidden">
      <Icon
        icon="home-small"
        tw="w-6 mr-4 cursor-pointer hover:text-primary-400 text-primary-500"
      />
    </Link>
    <HeaderRoutes tw="hidden md:block" />
    <Searchbar tw="ml-auto" />
    <User tw="pl-6 flex" />
  </div>
);

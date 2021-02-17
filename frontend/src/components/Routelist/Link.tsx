import * as React from 'react';
import tw from 'twin.macro';

import { Link } from '~/components/common';

type INavLink = React.FC<{
  url: string;
  label: string;
  activeRoute?: string | null;
}>;

export const NavLink: INavLink = ({ url, label, activeRoute }) => {
  const active = url === activeRoute;

  return (
    <>
      <Link href={url} tw="hidden sm:block">
        <div
          css={[
            tw`text-sm cursor-pointer text-foreground border-l-4 pl-7 pr-8 py-2`,
            active
              ? tw`border-l-4 border-primary-500 bg-white bg-opacity-7`
              : tw`border-transparent hover-bg`,
          ]}
        >
          {label}
        </div>
      </Link>
      <Link href={url} tw="block sm:hidden">
        <div tw="px-6 py-2 cursor-pointer md:px-8 text-foreground hover-bg">{label}</div>
      </Link>
    </>
  );
};

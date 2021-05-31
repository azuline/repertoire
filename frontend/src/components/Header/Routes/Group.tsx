import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { Icon, Link } from '~/components/common';

type IRouteGroup = React.FC<{
  name: string;
  href: string;
  children?: React.ReactNode;
}>;

export const RouteGroup: IRouteGroup = ({ name, href, children }) => {
  const active = false;

  return (
    <Wrapper>
      <Link
        css={[
          tw`text-foreground-400 flex items-center px-3 py-2 rounded`,
          tw`cursor-pointer hover-bg`,
          active && tw`font-semibold text-foreground-200`,
        ]}
        href={href}
      >
        {name}
        {children !== undefined && (
          <Icon icon="chevron-down-small" tw="w-4 mt-0.5 ml-1.5 -mr-0.5" />
        )}
      </Link>
      {children !== undefined && <div className="route-links">{children}</div>}
    </Wrapper>
  );
};

const Wrapper = styled.div`
  position: relative;
  z-index: 10;

  > .route-links {
    display: none;
    position: absolute;
    top: 2.5rem;
  }

  &:hover > .route-links {
    display: block;
  }
`;

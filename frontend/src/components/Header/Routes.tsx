import { SerializedStyles } from '@emotion/react';
import * as React from 'react';
import tw, { css, styled } from 'twin.macro';

import { Icon, Link, Popover } from '~/components';
import { routeSections } from '~/routes';

/**
 * TODO: Clean the styling of this up. It's pretty ugly and crappy right now; the
 * dropdowns are atrocious. Do a proper hover popover; also change the dropdowns to be a
 * nice rounded popover. Give the popover a makeover too; don't need the arrow
 * complicating everything.
 *
 * But for now, I want to go do some other things, so leaving this as-is.
 */

type IComponent = React.FC<{ className?: string }>;

export const HeaderRoutes: IComponent = ({ className }) => (
  <div className={className}>
    <div tw="flex gap-2">
      {routeSections.map(({ name, routes }) => {
        if (name === null) {
          return routes.map(({ path, label }) => (
            <MainLink key={path} href={path}>
              {label}
            </MainLink>
          ));
        }

        return (
          <StyledPopover key={name} align="left" tw="mt-1.5 -ml-3">
            <MainLabel>
              <span>{name}</span>
              <Icon icon="chevron-down-small" tw="w-4 mt-0.5 ml-1.5 -mr-0.5" />
            </MainLabel>
            <RouteLinks>
              {routes.map(({ path, label }) => {
                return (
                  <RouteLink key={path} href={path}>
                    {label}
                  </RouteLink>
                );
              })}
            </RouteLinks>
          </StyledPopover>
        );
      })}
    </div>
  </div>
);

type ILinkProps = {
  active?: boolean;
};

const MainLink = styled(Link)<ILinkProps>`
  ${(props): SerializedStyles => headerLabelStyles(props)}
`;

const MainLabel = styled.div<ILinkProps>`
  ${(props): SerializedStyles => headerLabelStyles(props)}
`;

type IHeaderLabelStyles = (arg0: ILinkProps) => SerializedStyles;

const headerLabelStyles: IHeaderLabelStyles = ({ active }) => css`
  ${tw`
    text-foreground-400
    flex
    items-center
    px-3
    py-2
    rounded
    cursor-pointer
    hover-bg
  `}

  ${active === true && tw`font-semibold text-foreground-200`}
`;

const StyledPopover = styled(Popover)`
  .popover-body-wrapper {
    ${tw`border-t-0 rounded-t-none!`}
  }
`;

const RouteLinks = tw.div`
  flex
  flex-col
  bg-background-700
  pb-2
  border-t-0
`;

const RouteLink = styled(Link)`
  margin-left: -2px;

  ${tw`pl-6 py-2 text-foreground-400 cursor-pointer min-width[140px] hover-bg`}
`;

import * as React from 'react';
import tw from 'twin.macro';

import { Icon, Link } from '~/components/common';

export type IElement = { id: number; name: string; starred?: boolean; type?: string };
export type IToggleStarFactory = (elem: IElement) => (() => Promise<void>) | undefined;

type IElementComponent = React.FC<{
  element: IElement;
  active: number | null;
  urlFactory: (arg0: number) => string;
  starrable?: boolean;
  toggleStarFactory: IToggleStarFactory;
}>;

export const Element: IElementComponent = ({
  element,
  active,
  urlFactory,
  starrable = true,
  toggleStarFactory,
}) => {
  const isActive = element.id === active;
  const url = urlFactory(element.id);
  const toggleStar = toggleStarFactory(element);

  return (
    <div tw="relative">
      {starrable && (
        <div
          css={[
            tw`absolute top-0 left-0 flex items-center h-full pl-6 md:pl-8`,
            element.starred === true
              ? tw`text-primary-500 fill-current`
              : tw`text-gray-500 stroke-current`,
            toggleStar && tw`cursor-pointer`,
            toggleStar &&
              (element.starred === true
                ? tw`hover:(text-gray-500 stroke-current)`
                : tw`hover:(text-primary-400 fill-current)`),
          ]}
          onClick={toggleStar}
        >
          <Icon icon="star-small" tw="w-4" />
        </div>
      )}
      <Link href={url}>
        <div
          css={[
            tw`flex items-center h-8 pr-8 cursor-pointer md:pr-10 hover-bg`,
            starrable ? tw`pl-12 md:pl-14` : tw`pl-6 md:pl-8`,
            isActive ? tw`font-bold text-primary-400` : tw`text-foreground`,
          ]}
        >
          <div tw="min-w-0 truncate">{element.name}</div>
        </div>
      </Link>
    </div>
  );
};

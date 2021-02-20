import * as React from 'react';

import { Icon } from '~/components';

type IRating = React.FC<{ rating: number }>;

export const Rating: IRating = ({ rating }) => (
  <>
    <div tw="items-center hidden lg:flex">
      {Array.from(new Array(rating), (_, i) => {
        return <Icon key={i} icon="star-small" tw="w-5 mr-0.5 text-primary-500 fill-current" />;
      })}
      <span tw="ml-1 text-foreground-200">{rating}</span>
    </div>
    <div tw="flex items-center lg:hidden">
      <Icon icon="star-small" tw="w-5 fill-current text-primary-500" />
      <span tw="ml-1 text-foreground-200">{rating}</span>
    </div>
  </>
);

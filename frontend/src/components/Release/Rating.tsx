import * as React from 'react';

import { Icon } from '~/components';

export const Rating: React.FC<{ rating: number }> = ({ rating }) => (
  <>
    <div className="items-center hidden lg:flex">
      {Array.from(new Array(rating), (_, i) => {
        return (
          <Icon key={i} className="w-5 mr-0.5 text-primary-500 fill-current" icon="star-small" />
        );
      })}
      <span className="ml-1 text-foreground-200">{rating}</span>
    </div>
    <div className="flex items-center lg:hidden">
      <Icon className="w-5 fill-current text-primary-500" icon="star-small" />
      <span className="ml-1 text-foreground-200">{rating}</span>
    </div>
  </>
);

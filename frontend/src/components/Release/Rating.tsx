import * as React from 'react';
import { Icon } from 'src/components';

export const Rating: React.FC<{ rating: number }> = ({ rating }) => (
  <>
    <div className="items-center hidden lg:flex">
      <span className="mr-1 text-foreground-200">{rating}</span>
      {Array.from(new Array(rating), (_, i) => {
        return <Icon key={i} className="w-5 pr-0.5 text-primary-500" icon="star-small-filled" />;
      })}
    </div>
    <div className="flex items-center lg:hidden">
      <span className="mr-1 text-foreground-200">{rating}</span>
      <Icon className="w-5 text-primary-500" icon="star-small-filled" />
    </div>
  </>
);

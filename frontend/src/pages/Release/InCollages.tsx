import * as React from 'react';

import { Link } from '~/components';
import { ICollection } from '~/graphql';

type IInCollages = React.FC<{ collages: Pick<ICollection, 'id' | 'name'>[] }>;

export const InCollages: IInCollages = ({ collages }) => {
  if (collages.length === 0) {
    return <div tw="flex-none" />;
  }

  return (
    <div tw="flex-none w-full py-8 truncate border-t-2 text-base border-background-900">
      <div tw="mb-4 font-semibold">In Collages</div>
      <ul>
        {collages.map((collage) => (
          <li key={collage.id} tw="my-1 text-primary-400">
            <Link href={`/collages/${collage.id}`}>{collage.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

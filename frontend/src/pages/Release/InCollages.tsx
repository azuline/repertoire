import * as React from 'react';

import { Link } from '~/components';
import { CollectionT } from '~/types';

export const InCollages: React.FC<{ collages: CollectionT[] }> = ({ collages }) => {
  if (collages.length === 0) {
    return <div className="flex-none" />;
  }

  return (
    <div className="flex-none w-full py-8 truncate border-t-2 text-md border-background-900">
      <div className="mb-4 font-semibold">In Collages</div>
      <ul>
        {collages.map((collage) => (
          <li key={collage.id} className="my-1 text-primary-400">
            <Link href={`/collages/${collage.id}`}>{collage.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

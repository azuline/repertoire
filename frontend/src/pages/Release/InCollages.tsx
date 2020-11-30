import * as React from 'react';
import { Link } from 'src/components';
import { CollectionT } from 'src/types';

export const InCollages: React.FC<{ collages: CollectionT[] }> = ({ collages }) => (
  <div className="flex-none w-full px-8 truncate text-md">
    {collages.length !== 0 && (
      <>
        <div className="mb-4 font-semibold">In Collages</div>
        <ul>
          {collages.map((collage) => (
            <li key={collage.id} className="my-1 text-primary-400">
              <Link href={`/collages/${collage.id}`}>{collage.name}</Link>
            </li>
          ))}
        </ul>
      </>
    )}
  </div>
);

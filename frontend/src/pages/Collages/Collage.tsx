import * as React from 'react';

import { BackButton, CollectionReleases, Header, Link, SectionHeader } from 'src/components';
import { fetchCollection } from 'src/lib';

export const Collage: React.FC<{ active: number }> = ({ active }) => {
  const { status, data } = fetchCollection(active);

  // prettier-ignore
  const collection = React.useMemo(
    () => (data && status === 'success' ? data.collection : null),
    [status, data],
  );

  if (!collection) return null;

  return (
    <div className="relative flex-1 flex flex-col">
      <Header />
      <div className="overflow-y-auto">
        <div className="px-8 pb-8 mt-1">
          <Link href="/collages">
            <BackButton />
          </Link>
          <SectionHeader className="my-4">{collection.name}</SectionHeader>
          <CollectionReleases active={active} />
        </div>
      </div>
    </div>
  );
};

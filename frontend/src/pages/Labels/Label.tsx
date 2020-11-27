import * as React from 'react';
import { BackButton, CollectionReleases, Header, Link, SectionHeader } from 'src/components';
import { fetchCollection } from 'src/lib';

export const Label: React.FC<{ active: number }> = ({ active }) => {
  const { status, data } = fetchCollection(active);

  // prettier-ignore
  const collection = React.useMemo(
    () => (data && status === 'success' ? data.collection : null),
    [status, data],
  );

  if (!collection) return null;

  return (
    <div className="relative flex flex-col flex-1">
      <Header />
      <div className="overflow-y-auto">
        <div className="px-8 pb-8 mt-1">
          <div className="flex justify-start">
            <Link href="/labels">
              <BackButton />
            </Link>
          </div>
          <SectionHeader className="my-4">{collection.name}</SectionHeader>
          <CollectionReleases active={active} />
        </div>
      </div>
    </div>
  );
};

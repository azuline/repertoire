import * as React from 'react';

import { Header } from 'src/components/Header';
import { Releases } from 'src/components/collection';
import { BackButton } from 'src/components/common/BackButton';
import { Link } from 'src/components/common/Link';
import { SectionHeader } from 'src/components/common/SectionHeader';
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
    <div className="relative flex-1 flex flex-col">
      <Header />
      <div className="overflow-y-auto">
        <div className="px-8 pb-8 mt-1">
          <Link href="/labels">
            <BackButton />
          </Link>
          <SectionHeader className="my-4">{collection.name}</SectionHeader>
          <Releases active={active} />
        </div>
      </div>
    </div>
  );
};

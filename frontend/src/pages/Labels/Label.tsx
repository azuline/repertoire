import * as React from 'react';
import { BackButton, CollectionReleases, Header, Link, SectionHeader } from 'src/components';
import { BackgroundContext } from 'src/contexts';
import { fetchCollection } from 'src/lib';

export const Label: React.FC<{ active: number }> = ({ active }) => {
  const { data } = fetchCollection(active);
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const collection = React.useMemo(() => data?.collection || null, [data]);

  React.useEffect(() => {
    if (!collection) return;

    setBackgroundImageId(collection.imageId);
    return (): void => setBackgroundImageId(null);
  }, [collection]);

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
          <SectionHeader className="mt-4 mb-8">{collection.name}</SectionHeader>
          <CollectionReleases active={active} />
        </div>
      </div>
    </div>
  );
};

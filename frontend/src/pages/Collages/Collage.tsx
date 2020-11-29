import * as React from 'react';
import { BackButton, CollectionReleases, Header, Link, SectionHeader } from 'src/components';
import { BackgroundContext } from 'src/contexts';
import { useFetchCollection } from 'src/lib';

export const Collage: React.FC<{ active: number }> = ({ active }) => {
  const { data } = useFetchCollection(active);
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
            <Link href="/collages">
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

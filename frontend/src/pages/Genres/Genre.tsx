import * as React from 'react';
import { CollectionReleases, Header, SectionHeader } from 'src/components';
import { BackgroundContext } from 'src/contexts';
import { useFetchCollection } from 'src/lib';

export const Genre: React.FC<{ active: number }> = ({ active }) => {
  const { data } = useFetchCollection(active);
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const collection = React.useMemo(() => data?.collection || null, [data]);

  React.useEffect(() => {
    if (!collection) return;

    setBackgroundImageId(collection.imageId);
    return (): void => setBackgroundImageId(null);
  }, [collection, setBackgroundImageId]);

  if (!collection) return null;

  return (
    <div className="flex flex-col w-full">
      <Header />
      <div className="z-20 px-8">
        <SectionHeader className="mt-4 mb-8">{collection.name}</SectionHeader>
        <CollectionReleases active={active} />
      </div>
    </div>
  );
};

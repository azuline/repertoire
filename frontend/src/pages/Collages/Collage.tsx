import * as React from 'react';
import { BackButton, CollectionReleases, Header, Link, SectionHeader } from 'src/components';
import { BackgroundContext } from 'src/contexts';
import { fetchCollection } from 'src/lib';

export const Collage: React.FC<{ active: number }> = ({ active }) => {
  const { status, data } = fetchCollection(active);
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  // prettier-ignore
  const collection = React.useMemo(
    () => (data && status === 'success' ? data.collection : null),
    [status, data],
  );

  React.useEffect(() => {
    if (!data || status !== 'success') return;

    setBackgroundImageId(data.collection.imageId);
    return (): void => setBackgroundImageId(null);
  }, [active, status]);

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

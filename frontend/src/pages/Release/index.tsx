import clsx from 'clsx';
import * as React from 'react';
import { Disclist, Header, Image } from 'src/components';
import { BackgroundContext, SidebarContext } from 'src/contexts';
import { useId } from 'src/hooks';
import { useFetchRelease } from 'src/lib';

import { InCollages } from './InCollages';
import { InFavorites } from './InFavorites';
import { Info } from './Info';
import { InInbox } from './InInbox';
import { Rating } from './Rating';

export const Release: React.FC = () => {
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const id = useId();
  const { data } = useFetchRelease(id as number);
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const release = data?.release || null;

  React.useEffect(() => {
    if (!release) return;

    setBackgroundImageId(release.imageId);
    return (): void => setBackgroundImageId(null);
  }, [release, setBackgroundImageId]);

  return (
    <div className="flex flex-col">
      <Header />
      {release && (
        <div className="flex flex-col mt-4">
          <div className="flex">
            <Image
              className={clsx(
                'flex-none hidden w-52 h-52 mr-8 rounded-lg',
                isSidebarOpen ? 'md:block' : 'sm:block',
              )}
              imageId={release.imageId}
            />
            <Info release={release} />
          </div>
          <div className={clsx('flex items-center mt-3', isSidebarOpen ? 'md:mt-6' : 'sm:mt-6')}>
            <div
              className={clsx(
                'hidden items-center flex-none w-52 mr-9 -ml-1 ',
                isSidebarOpen ? 'md:flex' : 'sm:flex',
              )}
            >
              <InFavorites release={release} />
              <InInbox release={release} />
            </div>
            <Rating release={release} />
          </div>
          <Disclist className="py-8" tracks={release.tracks} />
          <InCollages collages={release.collages} />
        </div>
      )}
    </div>
  );
};

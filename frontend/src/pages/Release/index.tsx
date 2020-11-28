import clsx from 'clsx';
import * as React from 'react';
import { Disclist, Header, Image } from 'src/components';
import { BackgroundContext, SidebarContext } from 'src/contexts';
import { useId } from 'src/hooks';
import { fetchRelease } from 'src/lib';

import { InCollages } from './InCollages';
import { Info } from './Info';

export const Release: React.FC = () => {
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const id = useId();
  const { data } = fetchRelease(id as number);
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const release = React.useMemo(() => data?.release || null, [data]);

  React.useEffect(() => {
    if (!release) return;

    setBackgroundImageId(release.imageId);
    return (): void => setBackgroundImageId(null);
  }, [release]);

  return (
    <div className="flex flex-col full">
      <Header />
      {release && (
        <div className="z-10 flex flex-col mt-4 overflow-y-auto">
          <div className="z-10 flex px-8">
            <Image
              className={clsx(
                'flex-none hidden w-64 h-64 mr-8 rounded-lg',
                isSidebarOpen ? 'md:block' : 'sm:block',
              )}
              imageId={release.imageId}
            />
            <Info release={release} />
          </div>
          <Disclist className="py-8" tracks={release.tracks} />
          <InCollages collages={release.collages} />
        </div>
      )}
    </div>
  );
};

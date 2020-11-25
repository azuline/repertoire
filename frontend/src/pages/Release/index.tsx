import * as React from 'react';

import { CollectionT, TrackT } from 'src/types';

import { CoverArt, Disclist, Header, Link } from 'src/components';
import { Info } from './Info';
import { SidebarContext } from 'src/contexts';
import clsx from 'clsx';
import { fetchRelease } from 'src/lib';
import { useId } from 'src/hooks';

// TODO: Light theme-ify support this.
const backgroundStyle = {
  background:
    'linear-gradient(185deg, rgba(16, 16, 19, 0.2), rgba(16, 16, 19, 0.6), rgba(16, 16, 19, 0.7), rgba(16, 16, 19, 1), rgba(16, 16, 19, 1))',
};

export const Release: React.FC = () => {
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const id = useId();
  const { data, status } = fetchRelease(id as number);

  const collageLength = React.useMemo(
    () => (data ? (data.release.collages as CollectionT[]).length : 0),
    [data],
  );

  return (
    <div className="relative flex flex-col full">
      <Header />
      {data && status === 'success' && (
        <>
          <div className={clsx('absolute top-0 left-0 h-0 full')}>
            <div className="absolute top-0 left-0 full z-0 opacity-50">
              <CoverArt className="full object-cover" release={data.release} />
            </div>
            <div className="full max-h-screen absolute top-0 left-0" style={backgroundStyle} />
          </div>
          <div className="overflow-y-auto flex flex-col mt-4 z-10">
            <div className="flex px-8 z-10">
              <CoverArt
                className={clsx(
                  'hidden flex-none w-64 h-64 mr-8 rounded-lg',
                  isSidebarOpen ? 'md:block' : 'sm:block',
                )}
                release={data.release}
              />
              <Info release={data.release} />
            </div>
            <Disclist className="py-8" tracks={data.release.tracks as TrackT[]} />
            <div className="text-md px-8 w-full overflow-x-hidden">
              {collageLength !== 0 && (
                <>
                  <div className="mb-2">Member of</div>
                  <ul>
                    {(data.release.collages as CollectionT[]).map((collage) => (
                      <li className="my-0.5 text-primary-alt3" key={collage.id}>
                        <Link href={`/collages/${collage.id}`}>{collage.name}</Link>
                      </li>
                    ))}
                  </ul>
                </>
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
};

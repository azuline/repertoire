import clsx from 'clsx';
import * as React from 'react';
import { Background, CoverArt, Disclist, Header, Link } from 'src/components';
import { SidebarContext } from 'src/contexts';
import { useId } from 'src/hooks';
import { fetchRelease } from 'src/lib';
import { CollectionT, TrackT } from 'src/types';

import { Info } from './Info';

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
          <Background>
            <CoverArt className="object-cover full" release={data.release} />
          </Background>
          <div className="z-10 flex flex-col mt-4 overflow-y-auto">
            <div className="z-10 flex px-8">
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
            <div className="w-full px-8 overflow-x-hidden text-md">
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

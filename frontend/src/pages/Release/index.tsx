import clsx from 'clsx';
import * as React from 'react';
import { Background, CoverArt, Disclist, Header } from 'src/components';
import { SidebarContext } from 'src/contexts';
import { useId } from 'src/hooks';
import { fetchRelease } from 'src/lib';

import { InCollages } from './InCollages';
import { Info } from './Info';

export const Release: React.FC = () => {
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const id = useId();
  const { data, status } = fetchRelease(id as number);

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
                  'flex-none hidden w-64 h-64 mr-8 rounded-lg',
                  isSidebarOpen ? 'md:block' : 'sm:block',
                )}
                release={data.release}
              />
              <Info release={data.release} />
            </div>
            <Disclist className="py-8" tracks={data.release.tracks} />
            <InCollages collages={data.release.collages} />
          </div>
        </>
      )}
    </div>
  );
};

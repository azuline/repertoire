import * as React from 'react';

import { CoverArt } from 'src/components/Release';

import { Disclist } from 'src/components/Tracklist';
import { Header } from 'src/components/Header';
import { useId } from 'src/hooks';
import { fetchRelease } from 'src/lib';
import { Info } from './Info';

export const Release: React.FC = () => {
  const id = useId();
  const { data, status } = fetchRelease(id as number);

  return (
    <div className="flex flex-col full">
      <Header />
      {data && status === 'success' && (
        <div className="flex flex-col mt-4">
          <div className="flex px-8">
            <CoverArt className="w-48 h-48 rounded-lg" release={data.release} />
            <Info release={data.release} />
          </div>
          <Disclist tracks={data.release.tracks} />
        </div>
      )}
    </div>
  );
};

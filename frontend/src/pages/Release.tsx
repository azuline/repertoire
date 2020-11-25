import * as React from 'react';

import { ArtistList, CoverArt } from 'src/components/Release';
import { ArtistT } from 'src/types';
import { Header } from 'src/components/Header';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { Link } from 'src/components/common/Link';
import { useId } from 'src/hooks';
import { fetchRelease } from 'src/lib';
import { formatReleaseDate } from 'src/common';

export const Release: React.FC = () => {
  const id = useId();
  const { data, status } = fetchRelease(id as number);

  const whenReleased = React.useMemo(() => data && formatReleaseDate(data.release), [data]);

  return (
    <div className="flex flex-col full">
      <Header />
      {data && status === 'success' && (
        <div className="flex flex-col mt-4">
          <div className="flex px-8">
            <div className="w-64 pb-full">
              <CoverArt className="full object-cover rounded-lg" release={data.release} />
            </div>
            <div className="ml-8 flex flex-col">
              <SectionHeader className="truncate-2 mb-4">{data.release.title}</SectionHeader>
              <div className="text-xl truncate-2 mb-4">
                {(data.release.artists as ArtistT[]).length === 0 ? (
                  <Link href="/artists/1">Unknown Artist</Link>
                ) : (
                  <>
                    <span>By: </span>
                    <ArtistList className="inline" elements={data.release.artists} link />
                  </>
                )}
              </div>
              <div className="text-xl mb-4">{whenReleased}</div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

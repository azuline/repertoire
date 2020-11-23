import * as React from 'react';
import clsx from 'clsx';

import { Header } from 'src/components/Header';
import { SidebarContext } from 'src/contexts';
import { ArtistReleases } from './Releases';
import { BackButton } from 'src/components/common/BackButton';
import { Link } from 'src/components/common/Link';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { fetchArtist } from 'src/lib';

export const Artist: React.FC<{ active: number }> = ({ active }) => {
  const { status, data } = fetchArtist(active);
  const { openBar } = React.useContext(SidebarContext);

  // prettier-ignore
  const artist = React.useMemo(
    () => (data && status === 'success' ? data.artist : null),
    [status, data],
  );

  if (!artist) return null;

  return (
    <div className="relative flex-1 flex flex-col">
      <Header />
      <Link
        className={clsx('top-0 mt-5 px-8 hidden absolute z-40', openBar ? 'xl:block' : 'lg:block')}
        href="/artists"
      >
        <BackButton />
      </Link>
      <div className="overflow-y-auto">
        <div className="px-8 pb-8">
          <Link className={openBar ? 'xl:hidden' : 'lg:hidden'} href="/artists">
            <BackButton />
          </Link>
          <SectionHeader className="my-4">{artist.name}</SectionHeader>
          <ArtistReleases active={active} />
        </div>
      </div>
    </div>
  );
};

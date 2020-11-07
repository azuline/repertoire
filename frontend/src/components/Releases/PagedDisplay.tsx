import * as React from 'react';

import { ArtRelease, RowRelease } from 'src/components/Release';
import { ReleaseT, ReleaseView } from 'src/types';

import { SidebarContext } from 'src/contexts';
import clsx from 'clsx';

// Partial here means that we have an artist/collection selector open.

// prettier-ignore
const gridFullCss = 'grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 2xl:grid-cols-7';
// prettier-ignore
const gridOneCssSidebar = 'grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6';
// prettier-ignore
const gridOneCssPartial = 'grid-cols-2 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6';
// prettier-ignore
const gridTwoCss = 'grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5';

export const PagedReleases: React.FC<{
  releases: ReleaseT[];
  view: ReleaseView;
  partial?: boolean;
}> = ({ releases, view, partial = false }) => {
  const { openBar } = React.useContext(SidebarContext);

  const gridCss = React.useMemo(() => {
    if (openBar && partial) {
      return gridTwoCss;
    } else if (openBar) {
      return gridOneCssSidebar;
    } else if (partial) {
      return gridOneCssPartial;
    } else {
      return gridFullCss;
    }
  }, [openBar, partial]);

  switch (view) {
    case ReleaseView.ROW:
      return (
        <div className="flex divide-y-2 divide-bg-embellish flex-col bg-bg">
          {releases.map((rls) => (
            <div key={rls.id}>
              <RowRelease release={rls} className="px-4 py-4 rounded" />
            </div>
          ))}
        </div>
      );
    case ReleaseView.ARTWORK:
    default:
      return (
        <div className={clsx('grid gap-6', gridCss)}>
          {releases.map((rls) => (
            <ArtRelease key={rls.id} release={rls} />
          ))}
        </div>
      );
  }
};

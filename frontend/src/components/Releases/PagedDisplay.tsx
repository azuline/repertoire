import 'twin.macro';

import clsx from 'clsx';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Pagination } from '~/components/Pagination';
import { ArtRelease, RowRelease } from '~/components/Release';
import { ViewSettings } from '~/components/ViewSettings';
import { IRelease, useFetchReleasesQuery } from '~/graphql';
import { IPagination, IViewOptions } from '~/hooks';
import { IReleaseView } from '~/types';

// Partial here means that we have an artist/collection selector open.

export const PagedReleases: React.FC<{
  viewOptions: IViewOptions;
  pagination: IPagination;
  partial?: boolean;
}> = ({ viewOptions, pagination, partial = false }) => {
  const { addToast } = useToasts();
  const { data, error } = useFetchReleasesQuery({
    variables: { ...viewOptions, ...pagination },
  });

  // prettier-ignore
  const { total, results: rawResults } = data?.releases || { results: [], total: 0 };
  const results = rawResults as IRelease[];

  React.useEffect(() => {
    if (total) pagination.setTotal(total);
  }, [total, pagination]);

  if (error) {
    error.graphQLErrors.forEach(({ message }) => {
      addToast(message, { appearance: 'error' });
    });
  }

  let releasesDiv = null;

  switch (viewOptions.releaseView) {
    case IReleaseView.Row:
      releasesDiv = (
        <div tw="flex flex-col">
          {results.map((rls) => (
            <div key={rls.id}>
              <RowRelease release={rls} tw="-mx-3 rounded-lg" />
            </div>
          ))}
        </div>
      );
      break;
    case IReleaseView.Artwork:
      releasesDiv = (
        <div className={clsx('grid gap-4 md:gap-6', calculateGridCss(partial))}>
          {results.map((rls) => (
            <ArtRelease key={rls.id} release={rls} />
          ))}
        </div>
      );
      break;
    default:
  }

  return (
    <div tw="pb-8">
      <ViewSettings pagination={pagination} partial={partial} tw="mb-6" viewOptions={viewOptions} />
      {releasesDiv}
      <Pagination pagination={pagination} tw="mt-6" />
    </div>
  );
};

const calculateGridCss = (partial: boolean): string => {
  if (partial) {
    return 'grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 2xl:grid-cols-5';
  }
  return 'grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6';
};

import { gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import tw, { TwStyle } from 'twin.macro';

import { Pagination } from '~/components/Pagination';
import { ArtRelease, RowRelease } from '~/components/Release';
import { ViewSettings } from '~/components/ViewSettings';
import { IRelease, usePagedReleasesFetchReleasesQuery } from '~/graphql';
import { IPagination, IViewOptions } from '~/hooks';
import { IReleaseView } from '~/types';

// Partial here means that we have an artist/collection selector open.

type IPagedReleases = React.FC<{
  viewOptions: IViewOptions;
  pagination: IPagination;
  partial?: boolean;
}>;

export const PagedReleases: IPagedReleases = ({ viewOptions, pagination, partial = false }) => {
  const { addToast } = useToasts();
  const { data, error } = usePagedReleasesFetchReleasesQuery({
    variables: { ...viewOptions, ...pagination },
  });

  // prettier-ignore
  const { total, results: rawResults } = data?.releases || { results: [], total: 0 };
  const results = rawResults as IRelease[];

  React.useEffect(() => {
    if (total) pagination.setTotal(total);
  }, [total, pagination.setTotal]);

  React.useEffect(() => {
    if (!error) return;

    error.graphQLErrors.forEach(({ message }) => {
      addToast(message, { appearance: 'error' });
    });
  }, [error, addToast]);

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
        <div css={[tw`grid gap-4 md:gap-6`, calculateGridCss(partial)]}>
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

const calculateGridCss = (partial: boolean): TwStyle => {
  if (partial) {
    return tw`grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 2xl:grid-cols-5`;
  }
  return tw`grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6`;
};

/* eslint-disable */
gql`
  query PagedReleasesFetchReleases(
    $search: String
    $collectionIds: [Int]
    $artistIds: [Int]
    $releaseTypes: [ReleaseType]
    $years: [Int]
    $ratings: [Int]
    $page: Int
    $perPage: Int
    $sort: ReleaseSort
    $asc: Boolean
  ) {
    releases(
      search: $search
      collectionIds: $collectionIds
      artistIds: $artistIds
      releaseTypes: $releaseTypes
      years: $years
      ratings: $ratings
      page: $page
      perPage: $perPage
      sort: $sort
      asc: $asc
    ) {
      total
      results {
        ...ReleaseFields
        artists {
          id
          name
        }
        genres {
          id
          name
        }
      }
    }
  }
`;

import { gql } from '@apollo/client';
import * as React from 'react';
import { useHistory } from 'react-router-dom';

import { Link, ScrolledReleases, SectionHeader } from '~/components';
import { useRecentlyAddedFetchReleasesQuery } from '~/graphql';

export const RecentlyAdded: React.FC = () => {
  const { data } = useRecentlyAddedFetchReleasesQuery();
  const history = useHistory();

  const releases = data?.releases.results ?? [];

  const toRecentlyAdded = (): void => {
    // TODO: change these string keys to constants.
    localStorage.setItem(
      'release-view-options--sort',
      JSON.stringify('RECENTLY_ADDED'),
    );
    localStorage.setItem('release-view-options--asc', JSON.stringify(false));
    history.push('/releases');
  };

  return (
    <>
      <Link href="/releases" onClick={toRecentlyAdded}>
        <SectionHeader tw="pad-page cursor-pointer">
          Recently Added
          <span tw="text-xl ml-1 hover:text-primary-400 text-primary-500">
            {' '}
            (View All)
          </span>
        </SectionHeader>
      </Link>
      <ScrolledReleases releases={releases} tw="mt-6" />
    </>
  );
};

/* eslint-disable */
gql`
  query RecentlyAddedFetchReleases {
    releases(sort: RECENTLY_ADDED, asc: false, page: 1, perPage: 10) {
      results {
        ...ReleaseFields
      }
    }
  }
`;

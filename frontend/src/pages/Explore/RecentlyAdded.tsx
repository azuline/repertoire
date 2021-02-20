import { gql } from '@apollo/client';
import * as React from 'react';
import { useHistory } from 'react-router-dom';

import { Link, ScrolledReleases, SectionHeader } from '~/components';
import { IRelease, useRecentlyAddedFetchReleasesQuery } from '~/graphql';

export const RecentlyAdded: React.FC = () => {
  const { data } = useRecentlyAddedFetchReleasesQuery();
  const history = useHistory();

  const releases = (data?.releases?.results || []) as IRelease[];

  const toRecentlyAdded = (): void => {
    // TODO: change these string keys to an enum.
    localStorage.setItem('release-view-options--sort', JSON.stringify('RECENTLY_ADDED'));
    localStorage.setItem('release-view-options--asc', JSON.stringify(false));
    history.push('/releases');
  };

  return (
    <div>
      <Link href="/releases" onClick={toRecentlyAdded}>
        <SectionHeader tw="mt-4 cursor-pointer">
          Recently Added
          <span tw="text-xl ml-1 hover:text-primary-400 text-primary-500"> (View All)</span>
        </SectionHeader>
      </Link>
      <ScrolledReleases releases={releases} />
    </div>
  );
};

/* eslint-disable */
gql`
  query RecentlyAddedFetchReleases {
    releases(sort: RECENTLY_ADDED, asc: false, page: 1, perPage: 10) {
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

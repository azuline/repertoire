import * as React from 'react';

import { RELEASE_FIELDS } from 'src/fragments';
import { useGQLQuery } from 'src/hooks';
import { ScrolledReleases } from 'src/components/Releases';
import { ReleaseT } from 'src/types';

const QUERY = `
	query {
		releases(
			sort: RECENTLY_ADDED
			asc: false
			page: 1
			perPage: 10
		) {
			results {
				${RELEASE_FIELDS}

				artists {
				  id
					name
				}
			}
		}
	}
`;

type ResultType = { releases: { results: ReleaseT[] } };

export const RecentlyAdded: React.FC = () => {
  const { status, data } = useGQLQuery<ResultType>('recently-added', QUERY);

  const releases = data && status === 'success' ? data.releases.results : [];

  return (
    <div className="flex flex-col flex-no-wrap">
      <span className="sect-header">Recently Added</span>
      <ScrolledReleases releases={releases} />
    </div>
  );
};

import * as React from 'react';

import { RELEASE_FIELDS } from 'src/fragments';
import { ReleaseT } from 'src/types';
import { ScrolledReleases } from 'src/components/Releases';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { useGQLQuery } from 'src/hooks';

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
        labels {
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

type ResultType = { releases: { results: ReleaseT[] } };

export const RecentlyAdded: React.FC = () => {
  const { status, data } = useGQLQuery<ResultType>('recently-added', QUERY);

  const releases = data && status === 'success' ? data.releases.results : [];

  return (
    <div className="mt-8">
      <SectionHeader className="mx-8">Recently Added</SectionHeader>
      <ScrolledReleases
        className="rpr--home-recently-added px-8 py-4 overflow-x-auto"
        releases={releases}
      />
    </div>
  );
};

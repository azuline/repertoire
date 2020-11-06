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
    <div className="flex flex-col">
      <SectionHeader className="w-11/12 mx-auto">Recently Added</SectionHeader>
      <div className="w-full bg-bg border-t-2 border-b-2 border-bg-embellish">
        <ScrolledReleases className="rpr--home-recently-added px-1/24 py-6" releases={releases} />
      </div>
    </div>
  );
};

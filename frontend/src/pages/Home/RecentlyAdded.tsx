import * as React from 'react';

import { RELEASE_FIELDS } from 'src/fragments';
import { ReleaseT } from 'src/types';
import { ScrolledReleases } from 'src/components/Releases';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { useGQLQuery } from 'src/hooks';
import { useHistory } from 'react-router-dom';

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
  const history = useHistory();

  const releases = data && status === 'success' ? data.releases.results : [];

  const toRecentlyAdded = React.useCallback(() => {
    // TODO: change these string keys to an enum.
    localStorage.setItem('release-view-options--sort', JSON.stringify('RECENTLY_ADDED'));
    localStorage.setItem('release-view-options--asc', JSON.stringify(false));
    history.push('/releases');
  }, [history]);

  return (
    <div className="mt-8">
      <SectionHeader className="mx-8 cursor-pointer" onClick={toRecentlyAdded}>
        Recently Added
      </SectionHeader>
      <ScrolledReleases
        className="rpr--home-recently-added px-8 py-4 overflow-x-auto"
        releases={releases}
      />
    </div>
  );
};

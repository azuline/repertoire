import { gql } from '@apollo/client';
import * as React from 'react';

import { Chooser, IElement, StarrableChooserRow } from '~/components';
import {
  useArtistChooserFetchArtistsQuery,
  useArtistChooserUpdateArtistStarredMutation,
} from '~/graphql';

type IArtistChooser = React.FC<{
  active: number | null;
  className?: string;
}>;

export const ArtistChooser: IArtistChooser = ({ active, className }) => {
  const { data, error, loading } = useArtistChooserFetchArtistsQuery();
  const [mutateArtist] = useArtistChooserUpdateArtistStarredMutation();

  const toggleStar = async (element: IElement): Promise<void> => {
    await mutateArtist({
      variables: { id: element.id, starred: element.starred !== true },
    });
  };

  if (!data || error || loading) {
    return null;
  }

  const artists = data.artists.results.filter((art) => art.numReleases !== 0);

  const renderElement = (index: number): React.ReactNode => {
    const element = artists[index];

    return (
      <StarrableChooserRow
        element={element}
        isActive={element.id === active}
        url={`/artists/${element.id}`}
        onToggle={(): Promise<void> => toggleStar(element)}
      />
    );
  };

  return (
    <Chooser
      active={active}
      className={className}
      renderElement={renderElement}
      results={artists}
    />
  );
};

/* eslint-disable */
gql`
  query ArtistChooserFetchArtists {
    artists {
      results {
        ...ArtistFields
      }
    }
  }

  mutation ArtistChooserUpdateArtistStarred($id: Int!, $starred: Boolean) {
    updateArtist(id: $id, starred: $starred) {
      id
      starred
    }
  }
`;

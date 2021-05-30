import { gql } from '@apollo/client';
import * as React from 'react';

import { Chooser, IElement, StarrableChooserRow } from '~/components';
import {
  useFetchArtistsChooserQuery,
  useStarArtistChooserMutation,
  useUnstarArtistChooserMutation,
} from '~/graphql';
import { compareByStarThenName } from '~/util';

type IArtistChooser = React.FC<{
  active: number | null;
  className?: string;
}>;

export const ArtistChooser: IArtistChooser = ({ active, className }) => {
  const { data, error, loading } = useFetchArtistsChooserQuery();
  const [starArtist] = useStarArtistChooserMutation();
  const [unstarArtist] = useUnstarArtistChooserMutation();

  const toggleStar = async (element: IElement): Promise<void> => {
    if (element.starred === true) {
      await unstarArtist({ variables: { id: element.id } });
    } else {
      await starArtist({ variables: { id: element.id } });
    }
  };

  const artists = React.useMemo(
    () =>
      data?.artists.results
        .filter((art) => art.numReleases !== 0)
        .sort(compareByStarThenName),
    [data],
  );

  if (!artists || error || loading) {
    return null;
  }

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
  query FetchArtistsChooser {
    artists {
      results {
        ...ArtistFields
      }
    }
  }

  mutation StarArtistChooser($id: Int!) {
    starArtist(id: $id) {
      id
      starred
    }
  }

  mutation UnstarArtistChooser($id: Int!) {
    unstarArtist(id: $id) {
      id
      starred
    }
  }
`;

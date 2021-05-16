import { gql } from '@apollo/client';
import * as React from 'react';

import { Chooser, IToggleStarFactory } from '~/components';
import {
  IArtist,
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

  const toggleStarFactory: IToggleStarFactory = ({ id, starred }) => {
    return async (): Promise<void> => {
      await mutateArtist({ variables: { id, starred: starred !== true } });
    };
  };

  if (!data || !data.artists || error || loading) {
    return null;
  }

  const results = data.artists.results as IArtist[];
  const artists = results.filter((art) => art.numReleases !== 0);

  return (
    <Chooser
      active={active}
      className={className}
      results={artists}
      toggleStarFactory={toggleStarFactory}
      urlFactory={urlFactory}
    />
  );
};

const urlFactory = (id: number): string => `/artists/${id}`;

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

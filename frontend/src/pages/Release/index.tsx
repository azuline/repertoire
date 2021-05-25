import { gql } from '@apollo/client';
import * as React from 'react';

import { Disclist, Header, Image } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useReleaseFetchReleaseQuery } from '~/graphql';
import { useId } from '~/hooks';
import { AuthenticatedError } from '~/pages';
import { filterNulls } from '~/util';

import { InCollages } from './InCollages';
import { InFavorites } from './InFavorites';
import { Info } from './Info';
import { InInbox } from './InInbox';
import { Rating } from './Rating';

export const Release: React.FC = () => {
  const id = useId();
  return id !== null ? <Body id={id} /> : null;
};

type IBody = React.FC<{ id: number }>;

const Body: IBody = ({ id }) => {
  const { data, error } = useReleaseFetchReleaseQuery({ variables: { id } });
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const release = data?.release;

  React.useEffect(() => {
    if (!release) {
      return;
    }

    setBackgroundImageId(release.imageId);
    return (): void => setBackgroundImageId(null);
  }, [release, setBackgroundImageId]);

  if (error) {
    const errors = error.graphQLErrors.map(({ message }) => message);
    return <AuthenticatedError errors={errors} title="Could not fetch release." />;
  }

  return (
    <div tw="flex flex-col">
      <Header />
      {release && (
        <div tw="flex flex-col mt-4">
          <div tw="flex">
            <Image
              imageId={release.imageId}
              tw="flex-none hidden w-72 h-72 mr-8 rounded-lg md:block"
            />
            <Info release={release} />
          </div>
          <div tw="flex items-center mt-6">
            <div tw="items-center flex-none hidden w-72 -ml-1 mr-9 md:flex">
              <InFavorites release={release} />
              <InInbox release={release} />
            </div>
            <Rating release={release} />
          </div>
          <Disclist tracks={filterNulls(release.tracks)} tw="py-8" />
          <InCollages collages={filterNulls(release.collages)} />
        </div>
      )}
    </div>
  );
};

/* eslint-disable */
gql`
  query ReleaseFetchRelease($id: Int!) {
    release(id: $id) {
      ...FullReleaseFields
    }
  }
`;

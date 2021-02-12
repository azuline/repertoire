import * as React from 'react';

import { Disclist, Header, Image } from '~/components';
import { BackgroundContext } from '~/contexts';
import { IRelease, useFetchReleaseQuery } from '~/graphql';
import { useId } from '~/hooks';
import { ErrorP } from '~/pages';
import { filterNulls } from '~/util';

import { InCollages } from './InCollages';
import { InFavorites } from './InFavorites';
import { Info } from './Info';
import { InInbox } from './InInbox';
import { Rating } from './Rating';

export const Release: React.FC = () => {
  const id = useId();
  return id ? <RealRelease id={id} /> : null;
};

type IComponent = React.FC<{ id: number }>;

export const RealRelease: IComponent = ({ id }) => {
  const { data, error } = useFetchReleaseQuery({ variables: { id } });
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const release = data?.release as IRelease | null;

  React.useEffect(() => {
    if (!release) return;

    setBackgroundImageId(release.imageId);
    return (): void => setBackgroundImageId(null);
  }, [release, setBackgroundImageId]);

  if (error) {
    const errors = error.graphQLErrors.map(({ message }) => message);
    return <ErrorP errors={errors} title="Could not fetch release." />;
  }

  return (
    <div className="flex flex-col">
      <Header />
      {release && (
        <div className="flex flex-col mt-4">
          <div className="flex">
            <Image
              className="flex-none hidden w-56 h-56 mr-8 rounded-lg md:block"
              imageId={release.imageId}
            />
            <Info release={release} />
          </div>
          <div className="flex items-center mt-6">
            <div className="items-center flex-none hidden w-56 -ml-1 mr-9 md:flex">
              <InFavorites release={release} />
              <InInbox release={release} />
            </div>
            <Rating release={release} />
          </div>
          <Disclist className="py-8" tracks={filterNulls(release.tracks)} />
          <InCollages collages={filterNulls(release.collages)} />
        </div>
      )}
    </div>
  );
};

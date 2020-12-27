import * as React from 'react';
import { Disclist, Header, Image } from 'src/components';
import { BackgroundContext } from 'src/contexts';
import { useId } from 'src/hooks';
import { useFetchRelease } from 'src/lib';

import { InCollages } from './InCollages';
import { InFavorites } from './InFavorites';
import { Info } from './Info';
import { InInbox } from './InInbox';
import { Rating } from './Rating';

export const Release: React.FC = () => {
  const id = useId();
  const { data } = useFetchRelease(id as number);
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const release = data?.release || null;

  React.useEffect(() => {
    if (!release) return;

    setBackgroundImageId(release.imageId);
    return (): void => setBackgroundImageId(null);
  }, [release, setBackgroundImageId]);

  return (
    <div className="flex flex-col">
      <Header />
      {release && (
        <div className="flex flex-col mt-4">
          <div className="flex">
            <Image
              className="flex-none hidden mr-8 rounded-lg w-52 h-52 md:block"
              imageId={release.imageId}
            />
            <Info release={release} />
          </div>
          <div className="flex items-center mt-6">
            <div className="items-center flex-none hidden -ml-1 w-52 mr-9 md:flex">
              <InFavorites release={release} />
              <InInbox release={release} />
            </div>
            <Rating release={release} />
          </div>
          <Disclist className="py-8" tracks={release.tracks} />
          <InCollages collages={release.collages} />
        </div>
      )}
    </div>
  );
};

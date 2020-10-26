import * as React from 'react';
import { useRequestBlob } from 'src/hooks';
import clsx from 'clsx';
import loading from 'src/assets/loading.png';

export const CoverArt: React.FC<{
  className: string;
  release: { id: number; hasCover: boolean };
}> = ({ className, release: { id, hasCover } }) => {
  // prettier-ignore
  const [image, setImage] = React.useState<string>(loading);
  const requestBlob = useRequestBlob();

  React.useEffect(() => {
    (async (): Promise<void> => {
      if (hasCover) {
        const blob = await requestBlob(`/files/covers/${id}`);
        setImage(URL.createObjectURL(blob));
      } else {
        // TODO: Find a default no-image cover.
      }
    })();
  }, [id, hasCover, setImage]);

  return <img className={clsx(className, 'rounded')} src={image} />;
};

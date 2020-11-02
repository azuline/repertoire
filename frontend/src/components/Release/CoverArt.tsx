import * as React from 'react';
import { useRequestBlob } from 'src/hooks';
import clsx from 'clsx';
import loading from 'src/assets/loading.png';
import noArt from 'src/assets/noArt.jpg';

// TODO: I don't think these images are being cached. Figure out if we can do that.

export const CoverArt: React.FC<{
  className: string;
  release: { id: number; hasCover: boolean };
}> = ({ className, release: { id, hasCover } }) => {
  // prettier-ignore
  const [image, setImage] = React.useState<string>(loading);
  const requestBlob = useRequestBlob();

  React.useEffect(() => {
    (async (): Promise<void> => {
      if (!hasCover) {
        setImage(noArt);
      } else {
        const blob = await requestBlob(`/files/covers/${id}`);
        setImage(URL.createObjectURL(blob));
      }
    })();
  }, [id, hasCover, setImage]);

  return <img className={clsx(className, 'rounded')} src={image} />;
};

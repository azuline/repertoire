import * as React from 'react';

import loading from 'src/assets/loading.png';
import noArt from 'src/assets/noArt.jpg';
import { useRequestBlob } from 'src/hooks';

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
        const blob = await requestBlob(`/files/covers/${id}?thumbnail=true`);
        setImage(URL.createObjectURL(blob));
      }
    })();
  }, [id, hasCover, setImage]);

  return <img className={className} src={image} />;
};

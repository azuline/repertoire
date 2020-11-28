import * as React from 'react';
import noArt from 'src/assets/noArt.jpg';

const urlFactory = (id: number | null, thumbnail: boolean): string =>
  id ? `/files/images/${id}?thumbnail=${thumbnail}` : '';

export const Image: React.FC<{
  className?: string;
  thumbnail?: boolean;
  imageId: number | null;
}> = ({ className, thumbnail = false, imageId }) => {
  const [src, setSrc] = React.useState(urlFactory(imageId, thumbnail));
  const onError = React.useCallback(() => setSrc(noArt), [setSrc]);

  React.useEffect(() => setSrc(urlFactory(imageId, thumbnail)), [imageId, thumbnail]);

  if (!imageId) {
    return <img className={className} src={noArt} />;
  }
  return <img className={className} src={src} onError={onError} loading="lazy" />;
};

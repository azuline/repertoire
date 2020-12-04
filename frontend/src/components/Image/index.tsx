import * as React from 'react';
import noArt from 'src/assets/noArt.jpg';

const urlFactory = (id: number | null, thumbnail: boolean): string =>
  id ? `/files/images/${id}?thumbnail=${thumbnail}` : '';

export const Image: React.FC<{
  className?: string;
  alt?: string | undefined;
  thumbnail?: boolean;
  imageId: number | null;
}> = ({ className, alt, thumbnail = false, imageId }) => {
  const [src, setSrc] = React.useState(urlFactory(imageId, thumbnail));

  React.useEffect(() => setSrc(urlFactory(imageId, thumbnail)), [imageId, thumbnail]);

  if (!imageId) {
    return <img alt={alt} className={className} src={noArt} />;
  }

  return (
    <img
      alt={alt}
      className={className}
      loading="lazy"
      src={src}
      onError={(): void => setSrc(noArt)}
    />
  );
};

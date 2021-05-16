import React from 'react';

import noArt from '~/assets/noArt.jpg';

type IImage = React.FC<{
  className?: string;
  alt?: string;
  thumbnail?: boolean;
  imageId: number | null;
}>;

export const Image: IImage = ({ className, alt, thumbnail = false, imageId }) => {
  const [src, setSrc] = React.useState(urlFactory(imageId, thumbnail));

  React.useEffect(() => setSrc(urlFactory(imageId, thumbnail)), [imageId, thumbnail]);

  if (imageId === null) {
    return <img alt={alt} className={className} src={noArt} tw="outline-none!" />;
  }

  return (
    <img
      alt={alt}
      className={className}
      loading="lazy"
      src={src}
      tw="outline-none!"
      onError={(): void => setSrc(noArt)}
    />
  );
};

const urlFactory = (id: number | null, thumbnail: boolean): string =>
  id !== null ? `/api/files/images/${id}?thumbnail=${thumbnail}` : '';

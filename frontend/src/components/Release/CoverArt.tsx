import * as React from 'react';
import noArt from 'src/assets/noArt.jpg';

const urlFactory = (id: number, thumbnail: boolean): string =>
  `/files/covers/${id}?thumbnail=${thumbnail}`;

export const CoverArt: React.FC<{
  className?: string;
  thumbnail?: boolean;
  release: { id: number; hasCover: boolean };
}> = ({ className, thumbnail = false, release: { id, hasCover } }) => {
  const [src, setSrc] = React.useState(urlFactory(id, thumbnail));
  const onError = React.useCallback(() => setSrc(noArt), [setSrc]);

  React.useEffect(() => setSrc(urlFactory(id, thumbnail)), [id, thumbnail]);

  if (!hasCover) {
    return <img className={className} src={noArt} />;
  }
  return <img className={className} src={src} onError={onError} loading="lazy" />;
};

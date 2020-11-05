import { ReleaseT } from 'src/types';

export const secondsToLength = (totalSeconds: number): string => {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = (totalSeconds % 60).toString().padStart(2, '0');
  return `${minutes}:${seconds}`;
};

export const getWhenReleased = (release: ReleaseT): string | null => {
  if (release.releaseDate) {
    return `on ${release.releaseDate}`;
  } else if (release.releaseYear) {
    return `in ${release.releaseYear}`;
  } else {
    return null;
  }
};

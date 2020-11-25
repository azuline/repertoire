import { ReleaseT } from 'src/types';

export const secondsToLength = (totalSeconds: number): string => {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = (totalSeconds % 60).toString().padStart(2, '0');
  return `${minutes}:${seconds}`;
};

export const formatReleaseDate = (release: ReleaseT): string => {
  if (!release.releaseDate && !release.releaseYear) {
    return 'Release date unknown.';
  } else if (release.releaseDate) {
    const date = new Date(release.releaseDate);
    return `Released on ${formatDate(date)}`;
  } else {
    return `Released in ${release.releaseYear}`;
  }
};

const shortMonths = [
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec',
];

const formatDate = (date: Date): string => {
  const shortMonth = shortMonths[date.getMonth()];
  const day = date.getDate();
  const year = date.getFullYear();

  return `${shortMonth} ${day}, ${year}`;
};

import { ReleaseT } from 'src/types';

export const formatReleaseDate = (release: ReleaseT): string => {
  if (!release.releaseDate && !release.releaseYear) {
    return 'Release date unknown.';
  }
  if (release.releaseDate) {
    const date = new Date(release.releaseDate);
    return `Released on ${formatDate(date)}`;
  }
  return `Released in ${release.releaseYear}`;
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

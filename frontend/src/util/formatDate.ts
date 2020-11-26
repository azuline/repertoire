import { ReleaseT } from 'src/types';

export const formatReleaseDate = (release: ReleaseT): string => {
  if (release.releaseDate) {
    return `Released on ${formatDate(new Date(release.releaseDate))}`;
  }

  if (release.releaseYear) {
    return `Released in ${release.releaseYear}`;
  }

  return 'Release date unknown.';
};

const SHORT_MONTHS = [
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
  const shortMonth = SHORT_MONTHS[date.getMonth()];
  const day = date.getDate();
  const year = date.getFullYear();

  return `${shortMonth} ${day}, ${year}`;
};

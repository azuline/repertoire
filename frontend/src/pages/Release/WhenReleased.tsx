import * as React from 'react';
import { ReleaseT } from 'src/types';

export const WhenReleased: React.FC<{ release: ReleaseT }> = ({ release }) => {
  if (release.releaseDate) {
    return (
      <>
        <span className="text-foreground-400">Released on </span>
        <span>{formatDate(new Date(release.releaseDate))}</span>
      </>
    );
  }

  if (release.releaseYear) {
    return (
      <>
        <span className="text-foreground-400">Released in </span>
        <span>{release.releaseYear}</span>
      </>
    );
  }

  return <span className="text-foreground-400">Released on unknown date</span>;
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

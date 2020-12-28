import * as React from 'react';
import { Link } from 'src/components';
import { ReleaseT } from 'src/types';

export const WhenReleased: React.FC<{ release: ReleaseT }> = ({ release }) => {
  if (release.releaseDate) {
    return (
      <>
        <span className="text-foreground-300">Released on </span>
        <span>{formatDate(new Date(release.releaseDate))}</span>
      </>
    );
  }

  if (release.releaseYear) {
    return (
      <>
        <span className="text-foreground-300">Released in </span>
        <Link className="text-primary-400" href={`/years/${release.releaseYear}`}>
          {release.releaseYear}
        </Link>
      </>
    );
  }

  return <span className="text-foreground-300">Released on unknown date</span>;
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

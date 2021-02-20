import * as React from 'react';

import { Link } from '~/components';
import { IRelease } from '~/graphql';

type IWhenReleased = React.FC<{ release: IRelease }>;

export const WhenReleased: IWhenReleased = ({ release }) => {
  if (release.releaseDate) {
    return (
      <>
        <span tw="text-foreground-300">Released on </span>
        <span>{formatDate(new Date(release.releaseDate))}</span>
      </>
    );
  }

  if (release.releaseYear) {
    return (
      <>
        <span tw="text-foreground-300">Released in </span>
        <Link href={`/years/${release.releaseYear}`} tw="text-primary-400">
          {release.releaseYear}
        </Link>
      </>
    );
  }

  return <span tw="text-foreground-300">Released on unknown date</span>;
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

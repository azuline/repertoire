import { IElement } from '~/components';

/**
 * A function that filters the nulls from an array and recasts the type as a
 * non-null list.
 *
 * @param xs A list with nulls.
 * @returns A list without nulls.
 */
export function filterNulls<T>(xs: (T | null)[]): T[] {
  return xs.filter((x): x is T => x !== null);
}

/**
 * A comparison function for track/disc numbers. This properly sorts
 * track/disc numbers that are not zero-padded.
 *
 * @param a - Comparison element 1.
 * @param b - Comparison element 2.
 * @returns -1, 0, or 1 as per convention.
 */
export const stringNumberCompare = (a: string, b: string): number => {
  const aTn = a.padStart(3, '0');
  const bTn = b.padStart(3, '0');

  if (aTn < bTn) {
    return -1;
  }
  if (aTn > bTn) {
    return 1;
  }
  return 0;
};

/**
 * A comparison function for elements. This sorts first by starred status, then
 * lexographically by name.
 *
 * @param a - Comparison element 1.
 * @param b - Comparison element 2.
 * @returns -1, 0, or 1 as per convention.
 */
export const compareByStarThenName = (a: IElement, b: IElement): number => {
  if (a.starred === true && b.starred !== true) {
    return -1;
  }
  if (a.starred !== true && b.starred === true) {
    return 1;
  }
  return a.name.localeCompare(b.name);
};

/**
 * Convert the number of seconds into a MM:SS timestamp.
 *
 * @param totalSeconds - How many seconds to convert.
 * @returns The corresponding MM:SS timestamp.
 */
export const secondsToLength = (totalSeconds: number): string => {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = (totalSeconds % 60).toString().padStart(2, '0');
  return `${minutes}:${seconds}`;
};

/**
 * Convert a REM unit into a Pixels unit.
 *
 * This is useful because our CSS is styled in REMs, but some components
 * (e.g. react-virtualized) expect units in pixels.
 *
 * @param rem Number of REMs.
 * @returns Number of pixels.
 */
export const convertRemToPixels = (rem: number): number =>
  rem * parseFloat(getComputedStyle(document.documentElement).fontSize);

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

/**
 * Format a Javascript `Date` into the `Jan 06, 2002` format.
 *
 * @param A date.
 * @returns A date string in the format `Jan 06, 2002`.
 */
export const formatDate = (date: Date): string => {
  const shortMonth = SHORT_MONTHS[date.getMonth()];
  const day = date.getDate();
  const year = date.getFullYear();

  return `${shortMonth} ${day}, ${year}`;
};

/**
 * Return the time until the passed-in date in `2 hours and 1 minute`
 * format.
 *
 * @param A date.
 * @returns A string represention of the duration until the date.
 */
export const timeUntil = (date: Date): string => {
  // The unit of diffs is minutes. `getTime()` returns milliseconds.
  const diff = (date.getTime() - Date.now()) / (60 * 1000);

  if (diff <= 0) {
    return 'the past';
  }

  const hours = Math.floor(diff / 60);
  const minutes = Math.floor(diff % 60);

  let builder = '';

  if (hours === 1) {
    builder += '1 hour';
  } else if (hours > 1) {
    builder += `${hours} hours`;
  }

  if (hours !== 0 && minutes !== 0) {
    builder += ' and ';
  }

  if (minutes === 1) {
    builder += '1 minute';
  } else if (minutes > 1) {
    builder += `${minutes} minutes`;
  }

  return builder;
};

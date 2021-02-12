/**
 * A function that filters the nulls from an array and recasts the type as a non-null list.
 *
 * @param xs A list with nulls.
 * @returns A list without nulls.
 */
export function filterNulls<T>(xs: (T | null)[]): T[] {
  return xs.filter((x): x is T => x !== null);
}

/**
 * A comparison function for track/disc numbers. This properly sorts track/disc
 * numbers that are not zero-padded.
 *
 * @param a - Comparison element 1.
 * @param b - Comparison element 2.
 * @returns -1, 0, or 1 as per convention.
 */
export const stringNumberCompare = (a: string, b: string): number => {
  const aTn = a.padStart(3, '0');
  const bTn = b.padStart(3, '0');

  if (aTn < bTn) return -1;
  if (aTn > bTn) return 1;
  return 0;
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
 * This is useful because our CSS is styled in REMs, but some components (e.g. react-virtualized)
 * expect units in pixels.
 *
 * @param rem Number of REMs.
 * @returns Number of pixels.
 */
export const convertRemToPixels = (rem: number): number =>
  rem * parseFloat(getComputedStyle(document.documentElement).fontSize);

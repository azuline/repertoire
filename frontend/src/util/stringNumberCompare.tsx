/**
 * A comparison function for track/disc numbers. This properly sorts track/disc
 * numbers that are not zero-padded.
 *
 * @param a Comparison element 1.
 * @param b Comparison element 2.
 * @returns -1, 0, or 1 as per convention.
 */
export const stringNumberCompare = (a: string, b: string): number => {
  const aTn = a.padStart(3, '0');
  const bTn = b.padStart(3, '0');

  if (aTn < bTn) return -1;
  if (aTn > bTn) return 1;
  return 0;
};

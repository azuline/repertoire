// Compare track/disc numbers (and handle sorting numbers that aren't zero
// padded.
export const stringNumberCompare = (a: string, b: string): number => {
  const aTn = a.padStart(3, '0');
  const bTn = b.padStart(3, '0');

  if (aTn < bTn) return -1;
  if (aTn > bTn) return 1;
  return 0;
};

/**
 * Convert the number of seconds into a MM:SS timestamp.
 *
 * @param totalSeconds How many seconds to convert.
 * @returns string The corresponding MM:SS timestamp.
 */
export const secondsToLength = (totalSeconds: number): string => {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = (totalSeconds % 60).toString().padStart(2, '0');
  return `${minutes}:${seconds}`;
};

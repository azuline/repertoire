export const convertRemToPixels = (rem: number): number =>
  rem * parseFloat(getComputedStyle(document.documentElement).fontSize);

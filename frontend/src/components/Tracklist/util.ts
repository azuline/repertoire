import { TrackT } from 'src/types';

export const checkMatchingTracklists = (list1: TrackT[], list2: TrackT[]): boolean => {
  if (list1.length !== list2.length) return false;

  for (let i = 0; i < list1.length; i++) {
    if (list1[i] !== list2[i]) return false;
  }

  return true;
};

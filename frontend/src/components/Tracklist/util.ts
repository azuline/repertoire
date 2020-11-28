import { TrackT } from 'src/types';

export const checkMatchingTracklists = (list1: TrackT[], list2: TrackT[]): boolean =>
  list1.length === list2.length && list1.every((t1, idx) => t1.id === list2[idx].id);

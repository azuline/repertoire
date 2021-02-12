import { ITrack } from '~/graphql';

export const checkMatchingTracklists = (list1: ITrack[], list2: ITrack[]): boolean =>
  list1.length === list2.length && list1.every((t1, idx) => t1.id === list2[idx].id);

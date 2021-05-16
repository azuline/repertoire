import { ITrack } from '~/graphql';

type ITrackWithID = Pick<ITrack, 'id'>;

export const checkMatchingTracklists = (
  list1: ITrackWithID[],
  list2: ITrackWithID[],
): boolean =>
  list1.length === list2.length && list1.every((t1, idx) => t1.id === list2[idx].id);

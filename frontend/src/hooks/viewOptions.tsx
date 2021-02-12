import * as React from 'react';

import { IReleaseSort, IReleaseType } from '~/graphql';
import { IReleaseView, ISetValue } from '~/types';

import { usePersistentState } from './persistentState';

// TODO: Refactor this mess... I'm thinking that we should ditch all the useEffects here and just
// let the callers create their own useEffects.

export type IViewOptions = {
  search: string;
  setSearch: ISetValue<string>;
  collectionIds: number[];
  setCollectionIds: ISetValue<number[]>;
  artistIds: number[];
  setArtistIds: ISetValue<number[]>;
  releaseTypes: IReleaseType[];
  setReleaseTypes: ISetValue<IReleaseType[]>;
  years: number[];
  setYears: ISetValue<number[]>;
  ratings: number[];
  setRatings: ISetValue<number[]>;
  sort: IReleaseSort;
  setSort: ISetValue<IReleaseSort>;
  asc: boolean;
  setAsc: ISetValue<boolean>;
  releaseView: IReleaseView;
  setReleaseView: ISetValue<IReleaseView>;
};

type IParams = {
  search?: string;
  collectionIds?: number[];
  artistIds?: number[];
  releaseTypes?: IReleaseType[];
  years?: number[];
  ratings?: number[];
  sort?: IReleaseSort;
  asc?: boolean;
  releaseView?: IReleaseView;
};

/**
 * An aggregated state hook to provide the viewOptions parameters for searching/browsing
 * releases.
 *
 * @param root0 - The "seed" object: initial values for the hook.
 * @returns A mega-state object containing the viewOptions parameters.
 */
export const useViewOptions = ({
  search,
  collectionIds,
  artistIds,
  releaseTypes,
  years,
  ratings,
  sort,
  asc,
  releaseView,
}: IParams = {}): IViewOptions => {
  const [searchState, setSearch] = React.useState<string>(search ?? '');
  const [collectionIdsState, setCollectionIds] = React.useState<number[]>(collectionIds ?? []);
  const [artistIdsState, setArtistIds] = React.useState<number[]>(artistIds ?? []);
  const [releaseTypesState, setReleaseTypes] = React.useState<IReleaseType[]>(releaseTypes ?? []);
  const [yearsState, setYears] = React.useState<number[]>(years ?? []);
  const [ratingsState, setRatings] = React.useState<number[]>(ratings ?? []);
  const [sortState, setSort] = usePersistentState<IReleaseSort>(
    'release-view-options--sort',
    sort ?? IReleaseSort.RecentlyAdded,
  );
  const [ascState, setAsc] = usePersistentState<boolean>('release-view-options--asc', asc ?? false);
  const [releaseViewState, setReleaseView] = usePersistentState<IReleaseView>(
    'release-view-options--view',
    releaseView ?? IReleaseView.Artwork,
  );

  React.useEffect(() => (search !== undefined ? setSearch(search) : undefined), [
    search,
    setSearch,
  ]);
  React.useEffect(() => collectionIds && setCollectionIds(collectionIds), [
    collectionIds,
    setCollectionIds,
  ]);
  React.useEffect(() => artistIds && setArtistIds(artistIds), [artistIds, setArtistIds]);
  React.useEffect(() => releaseTypes && setReleaseTypes(releaseTypes), [
    releaseTypes,
    setReleaseTypes,
  ]);
  React.useEffect(() => years && setYears(years), [years, setYears]);
  React.useEffect(() => ratings && setRatings(ratings), [ratings, setRatings]);
  React.useEffect(() => sort && setSort(sort), [sort, setSort]);
  React.useEffect(() => (asc !== undefined ? setAsc(asc) : undefined), [asc, setAsc]);
  React.useEffect(() => releaseView && setReleaseView(releaseView), [releaseView, setReleaseView]);

  return {
    artistIds: artistIdsState,
    asc: ascState,
    collectionIds: collectionIdsState,
    ratings: ratingsState,
    releaseTypes: releaseTypesState,
    releaseView: releaseViewState,
    search: searchState,
    setArtistIds,
    setAsc,
    setCollectionIds,
    setRatings,
    setReleaseTypes,
    setReleaseView,
    setSearch,
    setSort,
    setYears,
    sort: sortState,
    years: yearsState,
  };
};

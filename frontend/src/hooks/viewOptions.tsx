import * as React from 'react';
import { ReleaseSort, ReleaseType, ReleaseView, SetValue } from 'src/types';

import { usePersistentState } from './persistentState';

// TODO: Refactor this mess... I'm thinking that we should ditch all the useEffects here and just
// let the callers create their own useEffects.

export type ViewOptionsT = {
  search: string;
  setSearch: SetValue<string>;
  collectionIds: number[];
  setCollectionIds: SetValue<number[]>;
  artistIds: number[];
  setArtistIds: SetValue<number[]>;
  releaseTypes: ReleaseType[];
  setReleaseTypes: SetValue<ReleaseType[]>;
  years: number[];
  setYears: SetValue<number[]>;
  ratings: number[];
  setRatings: SetValue<number[]>;
  sort: ReleaseSort;
  setSort: SetValue<ReleaseSort>;
  asc: boolean;
  setAsc: SetValue<boolean>;
  releaseView: ReleaseView;
  setReleaseView: SetValue<ReleaseView>;
};

type Params = {
  search?: string;
  collectionIds?: number[];
  artistIds?: number[];
  releaseTypes?: ReleaseType[];
  years?: number[];
  ratings?: number[];
  sort?: ReleaseSort;
  asc?: boolean;
  releaseView?: ReleaseView;
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
}: Params = {}): ViewOptionsT => {
  const [searchState, setSearch] = React.useState<string>(search ?? '');
  const [collectionIdsState, setCollectionIds] = React.useState<number[]>(collectionIds ?? []);
  const [artistIdsState, setArtistIds] = React.useState<number[]>(artistIds ?? []);
  const [releaseTypesState, setReleaseTypes] = React.useState<ReleaseType[]>(releaseTypes ?? []);
  const [yearsState, setYears] = React.useState<number[]>(years ?? []);
  const [ratingsState, setRatings] = React.useState<number[]>(ratings ?? []);
  const [sortState, setSort] = usePersistentState<ReleaseSort>(
    'release-view-options--sort',
    sort ?? ReleaseSort.RECENTLY_ADDED,
  );
  const [ascState, setAsc] = usePersistentState<boolean>('release-view-options--asc', asc ?? false);
  const [releaseViewState, setReleaseView] = usePersistentState<ReleaseView>(
    'release-view-options--view',
    releaseView ?? ReleaseView.ARTWORK,
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

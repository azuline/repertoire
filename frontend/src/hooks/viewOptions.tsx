import * as React from 'react';

import { ReleaseSort, ReleaseType, ReleaseView } from 'src/types';

import { usePersistentState } from './persistentState';

export type ViewOptionsType = {
  search: string;
  setSearch: (arg0: string) => void;
  collectionIds: number[];
  setCollectionIds: (arg0: number[]) => void;
  artistIds: number[];
  setArtistIds: (arg0: number[]) => void;
  releaseTypes: ReleaseType[];
  setReleaseTypes: (arg0: ReleaseType[]) => void;
  sort: ReleaseSort;
  setSort: (arg0: ReleaseSort) => void;
  asc: boolean;
  setAsc: (arg0: boolean) => void;
  releaseView: ReleaseView;
  setReleaseView: (arg0: ReleaseView) => void;
};

type Params = {
  search?: string;
  collectionIds?: number[];
  artistIds?: number[];
  releaseTypes?: ReleaseType[];
  sort?: ReleaseSort;
  asc?: boolean;
  releaseView?: ReleaseView;
};

export const useViewOptions = ({
  search,
  collectionIds,
  artistIds,
  releaseTypes,
  sort,
  asc,
  releaseView,
}: Params = {}): ViewOptionsType => {
  const [searchState, setSearch] = React.useState<string>(search ?? '');
  const [collectionIdsState, setCollectionIds] = React.useState<number[]>(collectionIds ?? []);
  const [artistIdsState, setArtistIds] = React.useState<number[]>(artistIds ?? []);
  const [releaseTypesState, setReleaseTypes] = React.useState<ReleaseType[]>(releaseTypes ?? []);
  const [sortState, setSort] = usePersistentState<ReleaseSort>(
    'release-view-options--sort',
    sort ?? ReleaseSort.RECENTLY_ADDED,
  );
  const [ascState, setAsc] = usePersistentState<boolean>('release-view-options--asc', asc ?? false);
  const [releaseViewState, setReleaseView] = usePersistentState<ReleaseView>(
    'release-view-options--view',
    releaseView ?? ReleaseView.ARTWORK,
  );

  React.useEffect(() => (search !== undefined ? setSearch(search) : undefined), [search]);
  React.useEffect(() => collectionIds && setCollectionIds(collectionIds), [collectionIds]);
  React.useEffect(() => artistIds && setArtistIds(artistIds), [artistIds]);
  React.useEffect(() => releaseTypes && setReleaseTypes(releaseTypes), [releaseTypes]);
  React.useEffect(() => sort && setSort(sort), [sort]);
  React.useEffect(() => (asc !== undefined ? setAsc(asc) : undefined), [asc]);
  React.useEffect(() => releaseView && setReleaseView(releaseView), [releaseView]);

  return {
    search: searchState,
    setSearch,
    collectionIds: collectionIdsState,
    setCollectionIds,
    artistIds: artistIdsState,
    setArtistIds,
    releaseTypes: releaseTypesState,
    setReleaseTypes,
    sort: sortState,
    setSort,
    asc: ascState,
    setAsc,
    releaseView: releaseViewState,
    setReleaseView,
  };
};

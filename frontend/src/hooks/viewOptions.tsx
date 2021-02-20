import * as React from 'react';

import { IReleaseSort, IReleaseType } from '~/graphql';
import { IReleaseView, ISetValue } from '~/types';

import { usePersistentState } from './persistentState';

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
export const useViewOptions = (defaults: IParams = {}): IViewOptions => {
  const [search, setSearch] = React.useState<string>(defaults.search ?? '');
  const [collectionIds, setCollectionIds] = React.useState<number[]>(
    defaults.collectionIds ?? [],
  );
  const [artistIds, setArtistIds] = React.useState<number[]>(defaults.artistIds ?? []);
  const [releaseTypes, setReleaseTypes] = React.useState<IReleaseType[]>(
    defaults.releaseTypes ?? [],
  );
  const [years, setYears] = React.useState<number[]>(defaults.years ?? []);
  const [ratings, setRatings] = React.useState<number[]>(defaults.ratings ?? []);
  const [sort, setSort] = usePersistentState<IReleaseSort>(
    'release-view-options--sort',
    defaults.sort ?? IReleaseSort.RecentlyAdded,
  );
  const [asc, setAsc] = usePersistentState<boolean>(
    'release-view-options--asc',
    defaults.asc ?? false,
  );
  const [releaseView, setReleaseView] = usePersistentState<IReleaseView>(
    'release-view-options--view',
    defaults.releaseView ?? IReleaseView.Artwork,
  );

  return {
    artistIds,
    asc,
    collectionIds,
    ratings,
    releaseTypes,
    releaseView,
    search,
    setArtistIds,
    setAsc,
    setCollectionIds,
    setRatings,
    setReleaseTypes,
    setReleaseView,
    setSearch,
    setSort,
    setYears,
    sort,
    years,
  };
};

import * as React from 'react';

import { ReleaseSort, ReleaseType, ReleaseView } from 'src/types';

export type RVOCType = {
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

export const useViewOptions = (): RVOCType => {
  const [search, setSearch] = React.useState<string>('');
  const [collectionIds, setCollectionIds] = React.useState<number[]>([]);
  const [artistIds, setArtistIds] = React.useState<number[]>([]);
  const [releaseTypes, setReleaseTypes] = React.useState<ReleaseType[]>([]);
  const [sort, setSort] = React.useState<ReleaseSort>(ReleaseSort.RECENTLY_ADDED);
  const [asc, setAsc] = React.useState<boolean>(true);
  const [releaseView, setReleaseView] = React.useState<ReleaseView>(ReleaseView.ARTWORK);

  return {
    search,
    setSearch,
    collectionIds,
    setCollectionIds,
    artistIds,
    setArtistIds,
    releaseTypes,
    setReleaseTypes,
    sort,
    setSort,
    asc,
    setAsc,
    releaseView,
    setReleaseView,
  };
};

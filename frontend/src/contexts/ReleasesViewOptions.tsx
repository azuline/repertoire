import * as React from 'react';
import { ReleaseType, ReleaseSort } from 'src/types';
import { PaginationProvider } from './Pagination';

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
};

export const ReleaseViewOptionsContext = React.createContext<RVOCType>({
  search: '',
  setSearch: () => {},
  collectionIds: [],
  setCollectionIds: () => {},
  artistIds: [],
  setArtistIds: () => {},
  releaseTypes: [],
  setReleaseTypes: () => {},
  sort: 'RECENTLY_ADDED',
  setSort: () => {},
  asc: true,
  setAsc: () => {},
});

export const ReleaseViewOptionsProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [search, setSearch] = React.useState<string>('');
  const [collectionIds, setCollectionIds] = React.useState<number[]>([]);
  const [artistIds, setArtistIds] = React.useState<number[]>([]);
  const [releaseTypes, setReleaseTypes] = React.useState<ReleaseType[]>([]);
  const [sort, setSort] = React.useState<ReleaseSort>('RECENTLY_ADDED');
  const [asc, setAsc] = React.useState<boolean>(true);

  const value = {
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
  };

  return (
    <ReleaseViewOptionsContext.Provider value={value}>
      <PaginationProvider>{children}</PaginationProvider>
    </ReleaseViewOptionsContext.Provider>
  );
};

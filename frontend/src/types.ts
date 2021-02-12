export type IStateValue<T> = T | ((arg0: T) => T);
export type ISetValue<T> = (arg0: IStateValue<T>) => void;
export type ISetPersistentValue<T> = (arg0: IStateValue<T>, arg1?: boolean) => void;

export type IElement = {
  id: number;
  name: string;
};

export enum IReleaseView {
  Artwork = 'ARTWORK',
  Row = 'ROW',
}

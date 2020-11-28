export type StateValue<T> = T | ((arg0: T) => T);
export type SetValue<T> = (arg0: StateValue<T>) => void;
export type SetPersistentValue<T> = (arg0: StateValue<T>, arg1?: boolean) => void;

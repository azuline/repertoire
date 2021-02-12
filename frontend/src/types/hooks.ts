export type StateValue<T> = T | ((arg0: T) => T);
export type SetValue<T> = (arg0: StateValue<T>) => void;
export type SetPersistentValue<T> = (arg0: StateValue<T>, arg1?: boolean) => void;

// https://github.com/snowpackjs/snowpack/discussions/1589
export const SNOWPACK_BUG_HOOKS = true;

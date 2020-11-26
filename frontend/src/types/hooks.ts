export type StateValue<T> = T | ((arg0: T) => T);
export type SetValue<T> = (arg0: StateValue<T>) => void;

export type SetBoolean = SetValue<boolean>;
export type SetNumber = SetValue<number>;

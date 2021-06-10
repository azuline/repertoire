import * as React from 'react';

export type ISetPersistentValue<T> = (
  arg0: React.SetStateAction<T>,
  arg1?: boolean,
) => void;

/**
 * A hook that persists the value of the state in localStorage.
 *
 * @param localStorageKey - The key to use in localStorage.
 * @param defaultValue - The default value for the state. Only used when localStorage
 *                       does not have the key.
 *  @returns A 2-element list, containing the state value and a setter function.
 */
export const usePersistentState = <T>(
  localStorageKey: string,
  defaultValue: T,
): [T, React.Dispatch<React.SetStateAction<T>>] => {
  const [value, setValue] = React.useState<T>(() => {
    const storedValue = localStorage.getItem(localStorageKey);
    if (storedValue !== null) {
      return JSON.parse(storedValue) as T;
    }
    return defaultValue;
  });

  const setPersistentValue: ISetPersistentValue<T> = React.useCallback(
    (newValue, persist = true): void => {
      setValue((innerValue) => {
        const toStore = newValue instanceof Function ? newValue(innerValue) : newValue;
        if (persist) {
          localStorage.setItem(localStorageKey, JSON.stringify(toStore));
        }
        return toStore;
      });
    },
    [setValue], // eslint-disable-line react-hooks/exhaustive-deps
  );

  return [value, setPersistentValue];
};

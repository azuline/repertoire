import * as React from 'react';

type SetParam<T> = T | ((arg0: T) => T);

export const usePersistentState = <T>(
  localStorageKey: string,
  defaultValue: T,
): [T, (arg0: SetParam<T>) => void] => {
  /* A hook that persists the value of the state in localStorage.
   * `defaultValue` is only used when the key is not present in localStorage.
   */
  const [value, setValue] = React.useState<T>(() => {
    const storedValue = localStorage.getItem(localStorageKey);
    return storedValue ? JSON.parse(storedValue) : defaultValue;
  });

  const setPersistentValue = React.useCallback(
    (newValue: SetParam<T>, persist = true) => {
      setValue((innerValue: T) => {
        const toStore = newValue instanceof Function ? newValue(innerValue) : newValue;
        if (persist) {
          localStorage.setItem(localStorageKey, JSON.stringify(toStore));
        }
        return toStore;
      });
    },
    [setValue, localStorageKey],
  );

  return [value, setPersistentValue];
};

import * as React from 'react';

export const usePersistentState = <T>(
  localStorageKey: string,
  defaultValue: T | null = null,
): [T | null, (arg0: T | null) => void] => {
  /* A hook that persists the value of the state in localStorage.
   * `defaultValue` is only used when the key is not present in localStorage.
   */
  const [value, setValue] = React.useState(() => {
    const storedValue = localStorage.getItem(localStorageKey);
    return storedValue ? JSON.parse(storedValue) : defaultValue;
  });

  const setPersistentValue = React.useCallback(
    (newValue: T | null, persist = true) => {
      setValue((value: T | null) => {
        const toStore = newValue instanceof Function ? newValue(value) : newValue;
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

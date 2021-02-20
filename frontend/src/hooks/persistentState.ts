import * as React from 'react';

import { IStateValue } from '~/types';

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
): [T, (arg0: IStateValue<T>) => void] => {
  const [value, setValue] = React.useState<T>(() => {
    const storedValue = localStorage.getItem(localStorageKey);
    return storedValue ? JSON.parse(storedValue) : defaultValue;
  });

  const setPersistentValue = (newValue: IStateValue<T>, persist = true): void => {
    setValue((innerValue: T) => {
      const toStore = newValue instanceof Function ? newValue(innerValue) : newValue;
      if (persist) {
        localStorage.setItem(localStorageKey, JSON.stringify(toStore));
      }
      return toStore;
    });
  };

  return [value, setPersistentValue];
};

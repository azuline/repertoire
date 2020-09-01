import { useCallback, useState } from 'react';

export const usePersistentState = (localStorageKey, defaultValue) => {
  const [value, setValue] = useState(() => {
    const storedValue = localStorage.getItem(localStorageKey);
    return storedValue ? JSON.parse(storedValue) : defaultValue;
  });

  const setPersistentValue = useCallback(
    (newValue, persist = true) => {
      setValue((value) => {
        const toStore = newValue instanceof Function ? newValue(value) : newValue;
        if (persist) {
          localStorage.setItem(localStorageKey, JSON.stringify(toStore));
        }
        return toStore;
      });
    },
    [setValue, localStorageKey]
  );

  return [value, setPersistentValue];
};

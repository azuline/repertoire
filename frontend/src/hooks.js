import { useState } from 'react';

export const usePersistentState = (localStorageKey, defaultValue) => {
  const [value, setValue] = useState(() => {
    const storedValue = localStorage.getItem(localStorageKey);
    return storedValue ? JSON.parse(storedValue) : defaultValue;
  });

  const setPersistentValue = (newValue, persist = true) => {
    const toStore = newValue instanceof Function ? newValue(value) : newValue;
    setValue(toStore);
    if (persist) {
      localStorage.setItem(localStorageKey, JSON.stringify(toStore));
    }
  };

  return [value, setPersistentValue];
};

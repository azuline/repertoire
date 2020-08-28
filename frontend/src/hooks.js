import { useState } from 'react';

export const usePersistentState = (localStorageKey, defaultValue) => {
  const [value, setValue] = useState(() => {
    const storedValue = localStorage.getItem(localStorageKey);
    return storedValue ? JSON.parse(storedValue) : defaultValue;
  });

  const setPersistentValue = (value, persist = true) => {
    setValue(value);
    if (persist) {
      localStorage.setItem(localStorageKey, JSON.stringify(value));
    }
  };

  return [value, setPersistentValue];
};

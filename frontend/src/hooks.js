import { useState } from 'react';

export const usePersistentState = (localStorageKey, defaultValue, transformValue) => {
  const [value, setValue] = useState(() => {
    let storedValue = localStorage.getItem(localStorageKey);
    storedValue = storedValue ? JSON.parse(storedValue) : defaultValue;

    // transformValue is an optional function parameter that modifies the discovered value.
    if (transformValue) {
      storedValue = transformValue(storedValue);
    }

    return storedValue;
  });

  const setPersistentValue = (value) => {
    setValue(value);
    localStorage.setItem(localStorageKey, JSON.stringify(value));
  };

  return [value, setPersistentValue];
};

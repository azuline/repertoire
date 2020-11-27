import clsx from 'clsx';
import * as React from 'react';

import { ElementT } from './Element';

type IndexMap = { [k in string]?: () => void };

const jumpLetters = [
  'A',
  'B',
  'C',
  'D',
  'E',
  'F',
  'G',
  'H',
  'I',
  'J',
  'K',
  'L',
  'M',
  'N',
  'O',
  'P',
  'Q',
  'R',
  'S',
  'T',
  'U',
  'V',
  'W',
  'X',
  'Y',
  'Z',
  '#',
  '?',
];

const getJumpLetter = (string: string): string => {
  const firstChar = string.charAt(0).toUpperCase();
  if (/[A-Z]/.test(firstChar)) {
    return firstChar;
  }
  if (/\d/.test(firstChar)) {
    return '#';
  }
  return '?';
};

export const JumpToLetter: React.FC<{
  className?: string;
  active: number | null;
  results: ElementT[];
  setJumpTo: (arg0: number | null) => void;
}> = ({ className, active, results, setJumpTo }) => {
  const letterToIndexMap = React.useMemo(() => {
    const initialMap = jumpLetters.reduce<IndexMap>((map, jumpLetter) => {
      map[jumpLetter] = undefined; // eslint-disable-line no-param-reassign
      return map;
    }, {});

    return results.reduce<IndexMap>((map, elem, index) => {
      if (elem.starred) return map; // Exclude starred elements from jumper.

      const key = getJumpLetter(elem.name);

      if (!map[key]) {
        map[key] = (): void => setJumpTo(index); // eslint-disable-line no-param-reassign
      }

      return map;
    }, initialMap);
  }, [results]);

  return (
    <div
      className={clsx(
        className,
        'absolute top-0 right-0 z-20 overflow-y-hidden text-right',
        active ? 'mr-5' : 'mr-8',
      )}
      style={{ height: 'calc(100vh - 9rem)' }}
    >
      {Object.entries(letterToIndexMap).map(([letter, jumpFn]) => (
        <div
          className={clsx(
            'px-2',
            jumpFn
              ? 'cursor-pointer hover:font-bold text-primary'
              : 'text-gold-200 dark:text-gold-800',
          )}
          key={letter}
          onClick={jumpFn}
        >
          {letter}
        </div>
      ))}
    </div>
  );
};

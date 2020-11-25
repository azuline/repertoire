import * as React from 'react';
import { ElementT } from './Element';
import clsx from 'clsx';

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
  } else if (/\d/.test(firstChar)) {
    return '#';
  } else {
    return '?';
  }
};

export const JumpToLetter: React.FC<{
  className?: string;
  active: number | null;
  results: ElementT[];
  setJumpTo: (arg0: number | null) => void;
}> = ({ className, active, results, setJumpTo }) => {
  const letterToIndexMap = React.useMemo(() => {
    const initialMap = jumpLetters.reduce<IndexMap>((map, jumpLetter) => {
      map[jumpLetter] = undefined;
      return map;
    }, {});

    return results.reduce<IndexMap>((map, elem, index) => {
      if (elem.starred) return map; // Exclude starred elements from jumper.

      const key = getJumpLetter(elem.name);

      if (!map[key]) {
        map[key] = (): void => setJumpTo(index);
      }

      return map;
    }, initialMap);
  }, [results]);

  return (
    <div
      className={clsx(
        className,
        'text-right z-20 absolute top-0 right-0 overflow-y-hidden',
        active ? 'mr-5' : 'mr-8',
      )}
      style={{ height: 'calc(100vh - 9rem)' }}
    >
      {Object.entries(letterToIndexMap).map(([letter, jumpFn]) => (
        <div
          className={clsx(
            'px-2',
            jumpFn
              ? 'hover:font-bold cursor-pointer text-primary'
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

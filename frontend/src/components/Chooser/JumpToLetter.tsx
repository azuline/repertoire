import clsx from 'clsx';
import * as React from 'react';

import { ISetValue } from '~/types';

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

export const JumpToLetter: React.FC<{
  active: number | null;
  results: ElementT[];
  setJumpTo: ISetValue<number | null>;
}> = ({ active, results, setJumpTo }) => {
  // prettier-ignore
  const letterToIndexMap = React.useMemo(
    () => mapLettersToIndex(results, setJumpTo),
    [results, setJumpTo],
  );

  return (
    <div
      className={clsx(
        'absolute top-0 right-0 z-10 overflow-y-hidden text-right',
        active ? 'mt-9 mr-5' : 'mr-8 pt-1',
      )}
      style={{ height: 'calc(100vh - 9.5rem)' }}
    >
      {Object.entries(letterToIndexMap).map(([letter, jumpFn]) => (
        <div
          key={letter}
          className={clsx(
            'px-2',
            jumpFn ? 'cursor-pointer hover:font-bold text-primary-500' : 'text-primary-700',
          )}
          onClick={jumpFn}
        >
          {letter}
        </div>
      ))}
    </div>
  );
};

const mapLettersToIndex = (results: ElementT[], setJumpTo: ISetValue<number | null>): IndexMap => {
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
};

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

import clsx from 'clsx';
import * as React from 'react';
import { SetValue } from 'src/types/hooks';

import { ElementT } from './Element';

type IndexMap = { [k in string]?: () => void };

const jumpStyle = { height: 'calc(100vh - 9rem)' };

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
  setJumpTo: SetValue<number | null>;
}> = ({ active, results, setJumpTo }) => {
  // prettier-ignore
  const letterToIndexMap = React.useMemo(
    () => mapLettersToIndex(results, setJumpTo),
    [results, setJumpTo],
  );

  return (
    <div
      className={clsx(
        'absolute top-0 right-0 z-20 overflow-y-hidden text-right',
        active ? 'mt-10 mr-5' : 'mr-8',
      )}
      style={jumpStyle}
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

const mapLettersToIndex = (results: ElementT[], setJumpTo: SetValue<number | null>): IndexMap => {
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

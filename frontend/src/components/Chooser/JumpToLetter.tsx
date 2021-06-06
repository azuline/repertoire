import * as React from 'react';
import tw from 'twin.macro';

import { IElement } from './types';

type IIndexMap = { [k in string]?: () => void };

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

type IJumpToLetter = React.FC<{
  results: IElement[];
  setJumpTo: React.Dispatch<React.SetStateAction<number | null>>;
}>;

export const JumpToLetter: IJumpToLetter = ({ results, setJumpTo }) => {
  const letterToIndexMap = React.useMemo(
    () => mapLettersToIndex(results, setJumpTo),
    [results, setJumpTo],
  );

  return (
    <div
      css={[
        tw`absolute top-0 right-0 z-10 height[calc(100vh - 9.5rem)]`,
        tw`overflow-y-hidden text-right mt-9 mr-5`,
      ]}
    >
      {Object.entries(letterToIndexMap).map(([letter, jumpFn]) => (
        <div
          key={letter}
          css={[
            tw`px-2`,
            jumpFn
              ? tw`cursor-pointer hover:font-bold text-primary-500`
              : tw`text-primary-700`,
          ]}
          onClick={jumpFn}
        >
          {letter}
        </div>
      ))}
    </div>
  );
};

const mapLettersToIndex = (
  results: IElement[],
  setJumpTo: React.Dispatch<React.SetStateAction<number | null>>,
): IIndexMap => {
  const initialMap = jumpLetters.reduce<IIndexMap>((map, jumpLetter) => {
    map[jumpLetter] = undefined; // eslint-disable-line no-param-reassign
    return map;
  }, {});

  return results.reduce<IIndexMap>((map, elem, index) => {
    if (elem.starred === true) return map; // Exclude starred elements from jumper.

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

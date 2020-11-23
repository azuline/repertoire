import * as React from 'react';
import { ElementT } from './Element';

type LetterToIndexMapT = { [k in string]: () => void };

const matchLetter = /[A-Z]/;
const matchNumber = /\d/;

const getJumpLetter = (string: string): string => {
  const firstChar = string.charAt(0).toUpperCase();
  if (matchLetter.test(firstChar)) {
    return firstChar;
  } else if (matchNumber.test(firstChar)) {
    return '#';
  } else {
    return '?';
  }
};

export const JumpToLetter: React.FC<{
  results: ElementT[];
  setJumpTo: (arg0: number | null) => void;
}> = ({ results, setJumpTo }) => {
  const letterToIndexMap = React.useMemo(
    () =>
      results.reduce<LetterToIndexMapT>((map, elem, index) => {
        const key = getJumpLetter(elem.name);
        return key in map ? map : { ...map, [key]: (): void => setJumpTo(index) };
      }, {}),
    [results],
  );

  return (
    <div className="text-primary z-20 absolute top-0 right-0 pr-5 pt-4">
      {Object.entries(letterToIndexMap).map(([letter, jumpFn]) => (
        <div className="cursor-pointer px-2 py-0.5 hover:font-bold" key={letter} onClick={jumpFn}>
          {letter}
        </div>
      ))}
    </div>
  );
};
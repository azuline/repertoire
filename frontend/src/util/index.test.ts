import { filterNulls, secondsToLength, stringNumberCompare } from './index';

it('filter nulls', () => {
  const xs = [1, 2, null, 4, 5, null];
  const expected = [1, 2, 4, 5];
  expect(filterNulls(xs)).toStrictEqual(expected);
});

it('string number compare normal case less than', () => {
  expect(stringNumberCompare('10', '19')).toBe(-1);
});

it('string number compare greater than non-alphabetical', () => {
  expect(stringNumberCompare('10', '2')).toBe(1);
});

it('string number compare equal', () => {
  expect(stringNumberCompare('30', '30')).toBe(0);
});

it('seconds to length over 1 minute', () => {
  expect(secondsToLength(99)).toBe('1:39');
});

it('seconds to length less than 1 minute', () => {
  expect(secondsToLength(30)).toBe('0:30');
});

it('seconds to length pad seconds', () => {
  expect(secondsToLength(62)).toBe('1:02');
});

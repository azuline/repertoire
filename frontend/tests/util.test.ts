import { filterNulls } from '~/util';

it('filter nulls', () => {
  const xs = [1, 2, null, 4, 5, null];
  const expected = [1, 2, 4, 5];
  expect(filterNulls(xs)).toStrictEqual(expected);
});

import * as React from 'react';
import { useHistory, useParams } from 'react-router-dom';
import { useToasts } from 'react-toast-notifications';

/**
 * Verify that a given string is a non-negative integer.
 *
 * @param id - The string to check.
 * @returns If the string is a non-negative integer.
 */
const checkIsValid = (id: string): boolean => /^\d+$/.test(id);

/**
 * Fetch the ID from the current route (from react-router-dom). If the ID exists but is not a
 * non-negative integer, redirect the client to `/404`.
 *
 * @returns The active ID.
 */
export const useId = (): number | null => {
  const history = useHistory();
  const { addToast } = useToasts();
  const { id: rawId } = useParams<{ id: string }>();

  // Check if ID is valid; if not, redirect to /404.
  const parsedId = React.useMemo(() => {
    if (!rawId) {
      return null;
    }

    if (checkIsValid(rawId)) {
      return parseInt(rawId, 10);
    }

    addToast('Invalid ID.', { appearance: 'error' });
    history.push('/404');
    return null;
  }, [rawId, addToast, history]);

  return parsedId;
};

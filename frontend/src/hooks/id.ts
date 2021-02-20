import { useHistory, useParams } from 'react-router-dom';
import { useToasts } from 'react-toast-notifications';

/**
 * Fetch the ID from the current route (from react-router-dom). If the ID exists but is
 * not a non-negative integer, redirect the client to `/404`.
 *
 * @returns The active ID.
 */
export const useId = (): number | null => {
  const history = useHistory();
  const { addToast } = useToasts();
  const { id: rawId } = useParams<{ id: string }>();

  if (!rawId) {
    return null;
  }

  if (/^\d+$/.test(rawId)) {
    return parseInt(rawId, 10);
  }

  addToast('Invalid ID.', { appearance: 'error' });
  history.push('/404');
  return null;
};

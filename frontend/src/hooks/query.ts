import { useLocation } from 'react-router-dom';

/**
 * A hook to return the current query string.
 *
 * @returns The current query string.
 */
export const useQuery = (): URLSearchParams => new URLSearchParams(useLocation().search);

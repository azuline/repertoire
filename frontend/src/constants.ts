export const API_URL = process.env.NODE_ENV === 'development' ? 'http://localhost:5000' : '';

export const fuseOptions = {
  threshold: 0.4,
  isCaseSensitive: false,
  useExtendedSearch: true,
};

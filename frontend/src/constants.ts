export const API_URL =
  process.env.NODE_ENV === 'development' ? 'http://localhost:5000' : '';

export enum CacheKeys {
  User = 'user',
}

/* An enum to provide the string literals used as localStorage keys. */
export enum LocalKeys {
  AuthToken = 'auth--token',
  AuthUser = 'auth--user',
}

// Makes requests over the network against the backend.

export const apiUrl =
  process.env.NODE_ENV === 'development' ? 'http://localhost:5000' : '';

// Queries for a list of releases.
export const queryReleases = async (
  search,
  collections,
  artists,
  page,
  perPage,
  sort,
  asc
) => {
  const response = await fetch(
    `${apiUrl}/api/releases?` +
      new URLSearchParams({
        search: search ?? '',
        collections: collections ?? '',
        artists: artists ?? '',
        page: page ?? '',
        perPage: perPage ?? '',
        sort: sort ?? '',
        asc: asc ?? '',
      })
  );
  return await response.json();
};

// Returns a list of queries.
export const fetchQueries = async () => {
  const response = await fetch(`${apiUrl}/api/queries`);
  return await response.json();
};

// Submits a query and returns a newly-created query object.
export const submitQuery = async (query, name) => {
  const response = await fetch(`${apiUrl}/api/queries`, {
    method: 'POST',
    body: JSON.stringify({ query, name }),
  });
  return await response.json();
};

// Returns a list of collections.
export const fetchCollections = async () => {
  const response = await fetch(`${apiUrl}/api/collections`);
  return await response.json();
};

// Returns a list of artists.
export const fetchArtists = async () => {
  const response = await fetch(`${apiUrl}/api/artists`);
  return await response.json();
};

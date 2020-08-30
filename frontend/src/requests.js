// Makes requests over the network against the backend.

export const apiUrl =
  process.env.NODE_ENV === 'development' ? 'http://localhost:5000' : '';

// Queries for a list of releases.
export const queryReleases = async (
  token,
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
        collections: JSON.stringify(collections ?? []),
        artists: JSON.stringify(artists ?? []),
        page: page ?? '',
        perPage: perPage ?? '',
        sort: sort ?? '',
        asc: asc ?? '',
      }),
    {
      headers: new Headers({ Authorization: `Token ${token}` }),
    }
  );
  return await response.json();
};

// Returns a list of queries.
export const fetchQueries = async (token) => {
  const response = await fetch(`${apiUrl}/api/queries`, {
    headers: new Headers({ Authorization: `Token ${token}` }),
  });
  return await response.json();
};

// Submits a query and returns a newly-created query object.
export const submitQuery = async (token, query, name) => {
  const response = await fetch(`${apiUrl}/api/queries`, {
    method: 'POST',
    headers: new Headers({ Authorization: `Token ${token}` }),
    body: JSON.stringify({ query, name }),
  });
  return await response.json();
};

// Returns a list of collections.
export const fetchCollections = async (token) => {
  const response = await fetch(`${apiUrl}/api/collections`, {
    headers: new Headers({ Authorization: `Token ${token}` }),
  });
  return await response.json();
};

// Returns a list of artists.
export const fetchArtists = async (token) => {
  const response = await fetch(`${apiUrl}/api/artists`, {
    headers: new Headers({ Authorization: `Token ${token}` }),
  });
  return await response.json();
};

export type IRoute = { path: string; exact: boolean; label: string };

export const routeSections = [
  {
    name: null,
    routes: [{ exact: true, label: 'Explore', path: '/' }],
  },
  {
    name: 'Library',
    routes: [
      { exact: false, label: 'Releases', path: '/releases' },
      { exact: false, label: 'Artists', path: '/artists' },
      { exact: false, label: 'Genres', path: '/genres' },
      { exact: false, label: 'Labels', path: '/labels' },
      { exact: false, label: 'Years', path: '/years' },
    ],
  },
  {
    name: 'Collections',
    routes: [
      { exact: false, label: 'Collages', path: '/collages' },
      { exact: false, label: 'Playlists', path: '/playlists' },
    ],
  },
  {
    name: 'Manage',
    routes: [
      { exact: false, label: 'Settings', path: '/settings' },
      { exact: false, label: 'Invites', path: '/invites' },
    ],
  },
] as const;

/** @type {import("snowpack").SnowpackUserConfig } */
const httpProxy = require('http-proxy');
const proxy = httpProxy.createServer({ target: 'http://localhost:5000' });

module.exports = {
  mount: {
    public: { url: '/', static: true },
    src: { url: '/dist' },
  },
  plugins: [
    '@snowpack/plugin-react-refresh',
    '@snowpack/plugin-typescript',
    [
      '@snowpack/plugin-run-script',
      {
        cmd: 'postcss src/index.tailwind.css -o src/index.css',
        watch: 'postcss -w src/index.tailwind.css -o src/index.css',
      },
    ],
  ],
  alias: {
    '~': './src',
  },
  routes: [
    /* Enable an SPA Fallback in development: */
    { match: 'routes', src: '.*', dest: '/index.html' },
    /* Proxy API calls. */
    { src: '/api/.*', dest: (req, res) => proxy.web(req, res) },
  ],
  optimize: {
    /* Example: Bundle your final build: */
    // "bundle": true,
  },
  packageOptions: {
    /* ... */
  },
  devOptions: {
    port: 3000,
  },
  buildOptions: {
    /* ... */
  },
};

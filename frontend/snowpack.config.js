/** @type {import("snowpack").SnowpackUserConfig } */
const httpProxy = require('http-proxy');
const proxy = httpProxy.createServer({ target: 'http://localhost:5000' });

module.exports = {
  extends: '@snowpack/app-scripts-react',
  plugins: [
    '@snowpack/plugin-webpack',
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
    /* Proxy API calls. */
    { src: '/api/.*', dest: (req, res) => proxy.web(req, res) },
    { src: '/graphql', dest: (req, res) => proxy.web(req, res) },
    /* Enable an SPA Fallback in development: */
    { match: 'routes', src: '.*', dest: '/index.html' },
  ],
  optimize: {
    bundle: true,
  },
  packageOptions: {
    knownEntrypoints: ['@emotion/react', '@emotion/styled'],
  },
  devOptions: {
    port: 3000,
  },
  buildOptions: {},
};

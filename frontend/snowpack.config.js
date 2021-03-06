/** @type {import("snowpack").SnowpackUserConfig } */
const httpProxy = require('http-proxy');

const backendHost = process.env.BACKEND_HOST ?? 'localhost';
const proxy = httpProxy.createServer({ target: `http://${backendHost}:5000` });

proxy.on('err', (err, req, res) => {
  res.writeHead(500, {
    'Content-Type': 'text/plain',
  });

  res.end('An error occurred with the request.');

  console.log(`Error ${err} on request ${req}.`);
});

module.exports = {
  extends: '@snowpack/app-scripts-react',
  alias: {
    '~': './src',
    '~stories': './tests',
    '~tests': './tests',
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
    minify: true,
    target: 'es2018',
  },
  packageOptions: {
    knownEntrypoints: ['@emotion/react', '@emotion/styled'],
  },
  devOptions: {
    port: 3000,
    output: 'stream',
  },
  buildOptions: {},
};

import { defineConfig } from 'vite';
import reactRefresh from '@vitejs/plugin-react-refresh';
import macrosPlugin from 'vite-plugin-babel-macros';

const backendHost = process.env.BACKEND_HOST ?? 'localhost';
const proxyHost = `http://${backendHost}:5000`;

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    minify: 'esbuild',
    target: 'es2020',
  },
  clearScreen: false,
  plugins: [reactRefresh(), macrosPlugin()],
  resolve: {
    alias: {
      '~': './src',
    },
  },
  server: {
    proxy: {
      '/api': proxyHost,
      '/graphql': proxyHost,
    },
  },
});

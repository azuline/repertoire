import { defineConfig } from 'vite';
import reactRefresh from '@vitejs/plugin-react-refresh';
import macrosPlugin from 'vite-plugin-babel-macros';
import path from 'path';

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
      '~': path.resolve(__dirname, './src'),
    },
  },
  server: {
    proxy: {
      '/api': proxyHost,
      '/graphql': proxyHost,
    },
  },
});

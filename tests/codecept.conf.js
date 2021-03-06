require('ts-node/register');

const fetch = require('node-fetch');
const { setHeadlessWhen } = require('@codeceptjs/configure');

// turn on headless mode when running with HEADLESS=true environment variable
// export HEADLESS=true && npx codeceptjs run
setHeadlessWhen(process.env.HEADLESS);

exports.config = {
  tests: 'src/*.ts',
  output: './output',
  helpers: {
    Playwright: {
      url: 'http://localhost:3000',
      show: true,
      browser: 'chromium',
    },
  },
  include: {
    I: './steps_file.js',
  },
  bootstrap: null,
  mocha: {},
  name: 'tests',
  plugins: {
    pauseOnFail: {},
    retryFailedStep: {
      enabled: true,
    },
    tryTo: {
      enabled: true,
    },
    screenshotOnFail: {
      enabled: true,
    },
  },
  bootstrap: async () => {
    try {
      const res1 = await fetch('http://localhost:3000/api/dev/testuser', {
        method: 'POST',
      });
      if (res1.status !== 200) {
        console.log('Failed to create test user.');
        throw new Error('Failed to create test user.');
      }

      const res2 = await fetch('http://localhost:3000/api/dev/indexlib', {
        method: 'POST',
      });
      if (res2.status !== 200) {
        console.log('Failed to index library.');
        throw new Error('Failed to index library.');
      }
    } catch (e) {
      console.log(e);
      throw e;
    }
  },
};

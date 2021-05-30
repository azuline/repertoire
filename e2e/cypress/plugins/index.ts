// ***********************************************************
// This example plugins/index.ts can be used to load plugins
//
// You can change the location of this file or turn off loading
// the plugins file with the 'pluginsFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/plugins-guide
// ***********************************************************

import fetch from 'node-fetch';

const config: Cypress.PluginConfig = (on, config) => {
  on('before:run', async () => {
    const APP_URL = config.env.APP_URL;

    console.log('Creating test user and library.');

    try {
      const res1 = await fetch(`${APP_URL}/api/dev/testuser`, {
        method: 'POST',
      });
      if (res1.status !== 200) {
        console.log('Failed to create test user.');
        throw new Error('Failed to create test user.');
      }

      const res2 = await fetch(`${APP_URL}/api/dev/indexlib`, {
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
  });
};

export default config;

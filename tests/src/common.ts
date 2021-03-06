import { Page } from 'playwright';
import fetch from 'node-fetch';

export const SERVER_URL = 'http://localhost:3000';

// prepareBackend makes two API calls to repertoire to create a test
// user and index the testing library. The backend must be running in
// debug mode.
export const prepareBackend = async () => {
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
};

const successfulToastClassName = '.react-toast-notifications__toast--success';

export const login = async (page: Page) => {
  await page.goto(`${SERVER_URL}/`);
  // Verify that we are on the correct site...
  expect(await page.title()).toBe('repertoire');

  await page.fill('text=Authorization token', '00'.repeat(32));
  await page.click('text=Login');
  await page.isVisible(successfulToastClassName);
  await expect(page).toHaveText(successfulToastClassName, 'Success');
};

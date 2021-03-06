import { chromium, Browser, Page } from 'playwright';
import { login, prepareBackend, SERVER_URL } from '~/common';

// Set up a per-session browser.
let browser: Browser;

beforeAll(async () => {
  await prepareBackend();
  browser = await chromium.launch();
});

afterAll(async () => {
  await browser.close();
});

// Set up a per-test page.
let page: Page;

beforeEach(async () => {
  page = await browser.newPage();
});

afterEach(async () => {
  await page.close();
});

it('successful login', async () => {
  await login(page);
});

const errorToastClassName = '.react-toast-notifications__toast--error';

it('failed login', async () => {
  await page.goto(`${SERVER_URL}/`);
  // Verify that we are on the correct site...
  expect(await page.title()).toBe('repertoire');

  await page.fill('#auth-token', '44'.repeat(23));
  await page.click('text=Login');
  await page.waitForSelector(errorToastClassName);
  await expect(page).toHaveText(errorToastClassName, 'failed');
});

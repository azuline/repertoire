Feature('login');

Scenario('login step', ({ I }) => {
  I.login();
});

Scenario('login failed', ({ I }) => {
  I.amOnPage('/');
  I.fillField('.login--input', '0101010101');
  I.click('.login--submit');
  I.waitForElement('.react-toast-notifications__toast');
  I.see('Login failed.', { css: '.react-toast-notifications__toast' });
});

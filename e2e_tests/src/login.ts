Feature('login');

Scenario('login step', ({ I }) => {
  I.login();
});

Scenario('login failed', ({ I }) => {
  I.amOnPage('/');
  I.waitForElement('input');
  I.fillField('Authorization token', '0101010101');
  I.click('Login');
  I.waitForElement('.react-toast-notifications__toast', 5);
  I.see('Login failed.', { css: '.react-toast-notifications__toast' });
});

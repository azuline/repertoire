Feature('login');

Scenario('test something', ({ I }) => {
  I.login();
  I.seeElement('.header--username');
});

// in this file you can append custom step methods to 'I' object

module.exports = function () {
  return actor({
    login: function () {
      this.amOnPage('/login');
      this.waitForElement('input.token');
      this.fillField('Authorization token', '00'.repeat(32));
      this.click('Login');
      this.waitForElement('.react-toast-notifications__toast', 5);
      this.see('Successfully logged in.', { css: '.react-toast-notifications__toast' });
    },
  });
};

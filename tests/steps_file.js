// in this file you can append custom step methods to 'I' object

module.exports = function () {
  return actor({
    login: function () {
      this.amOnPage('/');
      this.fillField('.login--input', '00'.repeat(32));
      this.click('.login--submit');
      this.waitForElement('.react-toast-notifications__toast');
      this.see('Successfully logged in.', { css: '.react-toast-notifications__toast' });
    },
  });
};
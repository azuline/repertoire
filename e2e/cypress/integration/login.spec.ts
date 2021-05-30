context('Login', () => {
  it('login', () => {
    const APP_URL = Cypress.env('APP_URL');

    // Login.
    cy.visit(`${APP_URL}/login`);
    cy.get('#login-token').type('00'.repeat(32));
    cy.get('#login-btn').click();
    // View our username.
    cy.contains('tester');
  });
});

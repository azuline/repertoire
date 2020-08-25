module.exports = {
  extends: ['react-app', 'prettier'],
  plugins: ['prettier', 'sort-keys-fix'],
  rules: {
    'prettier/prettier': 'warn',
    'sort-keys-fix/sort-keys-fix': 'warn',
  },
};

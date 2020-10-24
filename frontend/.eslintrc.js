module.exports = {
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
    ecmaFeatures: {
      jsx: true,
    },
  },
  extends: [
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier',
    'prettier/@typescript-eslint',
    'prettier/react',
    'plugin:react/recommended',
    'plugin:prettier/recommended',
  ],
  plugins: ['@typescript-eslint'],
  env: {
    es6: true,
    browser: true,
    jest: true,
  },
  rules: {
    'prettier/prettier': 'warn',
    indent: ['error', 2],
    'linebreak-style': ['error', 'unix'],
    quotes: ['error', 'single'],
    'no-console': 'warn',
    'no-unused-vars': 'off',
    '@typescript-eslint/no-unused-vars': [
      'error',
      { vars: 'all', args: 'after-used', ignoreRestSiblings: false },
    ],
    '@typescript-eslint/explicit-function-return-type': 'warn',
    'no-empty': 'warn',
    'react/prop-types': 'off', // Using React.FC, but this still goes off...?
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
};

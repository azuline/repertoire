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
  plugins: ['@typescript-eslint', 'simple-import-sort'],
  env: {
    es6: true,
    browser: true,
    jest: true,
  },
  rules: {
    'simple-import-sort/imports': 'warn',
    'simple-import-sort/exports': 'warn',
    'no-duplicate-imports': 'warn',
    'sort-imports': 'off',
    'import/order': 'off',
    'prettier/prettier': 'warn',
    indent: ['error', 2, { SwitchCase: 1 }],
    'linebreak-style': ['error', 'unix'],
    quotes: ['error', 'single', 'avoid-escape'],
    'no-console': 'warn',
    'no-unused-vars': 'off',
    '@typescript-eslint/no-unused-vars': [
      'warn',
      { vars: 'all', args: 'after-used', ignoreRestSiblings: false },
    ],
    '@typescript-eslint/explicit-function-return-type': 'warn',
    'no-empty': 'warn',
    'react/prop-types': 'off', // Using React.FC, but this still goes off...?
    '@typescript-eslint/no-empty-function': 'off', // Screw you >:(
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
};

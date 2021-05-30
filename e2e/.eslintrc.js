module.exports = {
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
    project: './tsconfig.json',
  },
  extends: [
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier',
    'plugin:prettier/recommended',
  ],
  plugins: ['@typescript-eslint'],
  env: {
    es6: true,
    browser: true,
    jest: true,
  },
  rules: {
    'consistent-return': 'off',
    indent: ['error', 2, { SwitchCase: 1 }],
    'linebreak-style': ['error', 'unix'],
    'max-len': ['warn', { code: 88, tabWidth: 2 }],
    'no-console': 'off',
    'no-unused-vars': 'warn',
    'no-duplicate-imports': 'warn',
    'no-empty': 'warn',
    'no-plusplus': 'off',
    'prettier/prettier': 'warn',
    quotes: ['error', 'single', 'avoid-escape'],
    '@typescript-eslint/explicit-function-return-type': 'warn',
    '@typescript-eslint/strict-boolean-expressions': 'error',
    '@typescript-eslint/no-empty-function': 'off',
    '@typescript-eslint/no-unused-vars': [
      'warn',
      { vars: 'all', args: 'after-used', ignoreRestSiblings: false },
    ],
    '@typescript-eslint/no-use-before-define': 'off',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
};

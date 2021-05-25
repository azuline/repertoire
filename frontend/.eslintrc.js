module.exports = {
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
    ecmaFeatures: {
      jsx: true,
    },
    project: './tsconfig.json',
  },
  ignorePatterns: ['src/graphql/index.ts'],
  extends: [
    'airbnb-typescript',
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier',
    'prettier/@typescript-eslint',
    'prettier/react',
    'plugin:react/recommended',
    'plugin:prettier/recommended',
    'plugin:import/recommended',
    'plugin:react-hooks/recommended',
  ],
  plugins: ['@typescript-eslint', 'simple-import-sort', 'sort-keys-fix'],
  env: {
    es6: true,
    browser: true,
    jest: true,
  },
  rules: {
    'consistent-return': 'off',
    'import/order': 'off',
    'import/extensions': 'off',
    'import/no-unresolved': 'off',
    'import/prefer-default-export': 'off',
    'import/no-relative-parent-imports': 'error',
    indent: ['error', 2, { SwitchCase: 1 }],
    // Not dealing with a11y at the moment.
    'jsx-a11y/alt-text': 'off',
    'jsx-a11y/no-static-element-interactions': 'off',
    'jsx-a11y/click-events-have-key-events': 'off',
    'jsx-a11y/label-has-associated-control': 'off',
    'jsx-a11y/no-autofocus': 'off',
    'linebreak-style': ['error', 'unix'],
    'max-len': ['warn', { code: 88, tabWidth: 2 }],
    'no-console': 'warn',
    'no-unused-vars': 'warn',
    'no-duplicate-imports': 'warn',
    'no-empty': 'warn',
    'no-plusplus': 'off',
    'prettier/prettier': 'warn',
    quotes: ['error', 'single', 'avoid-escape'],
    'react/no-array-index-key': 'off', // Sometimes there's nothing else -_-
    'react/jsx-props-no-spreading': 'off', // ...
    'react/prop-types': 'off', // Goes off even though components are typed.
    'react/jsx-sort-props': [
      'warn',
      {
        callbacksLast: true,
        shorthandFirst: true,
        reservedFirst: true,
      },
    ],
    'simple-import-sort/imports': 'warn',
    'simple-import-sort/exports': 'warn',
    'sort-imports': 'off',
    'sort-keys-fix/sort-keys-fix': 'warn',
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

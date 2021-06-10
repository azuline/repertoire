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
    'eslint:recommended',
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:import/recommended',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    // Prettier must be the last extension listed.
    'prettier/react',
    'prettier/@typescript-eslint',
    'plugin:prettier/recommended',
  ],
  plugins: [
    '@typescript-eslint',
    'simple-import-sort',
    'sort-keys-fix',
    'unused-imports',
  ],
  env: {
    es6: true,
    browser: true,
    jest: true,
  },
  rules: {
    // Style
    'prettier/prettier': 'warn',
    'max-len': ['warn', { code: 88, tabWidth: 2 }],
    indent: ['error', 2, { SwitchCase: 1 }],
    quotes: ['error', 'single', 'avoid-escape'],
    'linebreak-style': ['error', 'unix'],
    'no-console': 'warn',
    'no-unused-vars': 'warn',
    'no-empty': 'warn',
    'no-plusplus': 'off',
    'consistent-return': 'off',
    // This interferes with GraphQL __typename usage.
    'no-underscore-dangle': 'off',

    // Prop/key sorting.
    'react/jsx-sort-props': [
      'warn',
      {
        callbacksLast: true,
        shorthandFirst: true,
        reservedFirst: true,
      },
    ],
    'sort-keys-fix/sort-keys-fix': 'warn',

    // Unused imports and variables.
    'no-unused-vars': 'off',
    'unused-imports/no-unused-imports': 'error',
    'unused-imports/no-unused-vars': [
      'warn',
      {
        vars: 'all',
        varsIgnorePattern: '^_',
        args: 'after-used',
        argsIgnorePattern: '^_',
      },
    ],

    // Imports
    'no-duplicate-imports': 'warn',
    'import/order': 'off',
    'import/extensions': 'off',
    'import/no-unresolved': 'off',
    'import/prefer-default-export': 'off',
    'import/no-relative-parent-imports': 'error',
    'sort-imports': 'off',
    'simple-import-sort/imports': 'warn',
    'simple-import-sort/exports': 'warn',

    // Overrides for React.
    'react/no-array-index-key': 'off', // Sometimes there's nothing else -_-
    'react/jsx-props-no-spreading': 'off', // ...
    'react/prop-types': 'off', // Goes off even though components are typed.

    // Overrides for @typescript-eslint.
    '@typescript-eslint/explicit-function-return-type': 'warn',
    '@typescript-eslint/strict-boolean-expressions': 'error',
    '@typescript-eslint/no-empty-function': 'off',
    '@typescript-eslint/no-use-before-define': 'off',
    '@typescript-eslint/no-unused-vars': 'off',
    '@typescript-eslint/restrict-template-expressions': [
      'error',
      {
        allowBoolean: true,
      },
    ],
    '@typescript-eslint/no-floating-promises': [
      'error',
      {
        ignoreIIFE: true,
      },
    ],
    // This is for the above no-floating-promises rule.
    'no-void': ['error', { allowAsStatement: true }],

    // Overrides for jsx-a11y--not dealing with a11y right now.
    'jsx-a11y/alt-text': 'off',
    'jsx-a11y/no-static-element-interactions': 'off',
    'jsx-a11y/click-events-have-key-events': 'off',
    'jsx-a11y/label-has-associated-control': 'off',
    'jsx-a11y/no-autofocus': 'off',

    // Disabling this because there are too many false positives.
    'react-hooks/exhaustive-deps': 'off',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
};

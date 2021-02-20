module.exports = {
  printWidth: 88,
  singleQuote: true,
  trailingComma: 'all',
  overrides: [
    {
      files: ['*.ts', '*.tsx'],
      options: {
        parser: 'typescript',
      },
    },
  ],
};

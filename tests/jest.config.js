module.exports = {
  preset: 'jest-playwright-preset',
  testMatch: ['**/*.test.{ts,js}'],
  moduleNameMapper: {
    '^~/(.*)$': '<rootDir>/src/$1',
  },
  setupFilesAfterEnv: ['expect-playwright'],
  transform: {
    '^.+\\.(ts)$': 'ts-jest',
  },
};

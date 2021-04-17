module.exports = {
  ...require('@snowpack/app-scripts-react/jest.config.js')(),
  setupFilesAfterEnv: [],
  testMatch: ['<rootDir>/src/**/*.test.{js,jsx,ts,tsx}'],
  moduleNameMapper: {
    '^~/(.*)$': '<rootDir>/src/$1',
  },
  collectCoverageFrom: ['src/**/*.{ts,tsx}'],
};

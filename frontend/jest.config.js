module.exports = {
  ...require('@snowpack/app-scripts-react/jest.config.js')(),
  setupFilesAfterEnv: [],
  testMatch: ['<rootDir>/tests/**/*.{js,jsx,ts,tsx}'],
  moduleNameMapper: {
    '^~/(.*)$': '<rootDir>/src/$1',
    '^~stories/(.*)$': '<rootDir>/stories/$1',
    '^~tests/(.*)$': '<rootDir>/tests/$1',
  },
  collectCoverageFrom: ['src/**/*.{ts,tsx}', 'tests/**/*.{ts,tsx}'],
};

const path = require('path');
const snowpackConfig = require('../snowpack.config');

module.exports = {
  stories: ['../stories/**/*.stories.mdx', '../stories/**/*.stories.@(ts|tsx)'],
  addons: ['@storybook/addon-links', '@storybook/addon-essentials'],
  webpackFinal: async (config) => {
    config.resolve.alias = {
      ...config.resolve.alias,
      ...Object.fromEntries(
        Object.entries(snowpackConfig.alias).map(([key, value]) => [
          key,
          path.resolve(__dirname, '../', value),
        ]),
      ),
    };

    return config;
  },
};

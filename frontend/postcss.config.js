const tailwind = require('tailwindcss');
const cssnano = require('cssnano');

const isProd = process.env.NODE_ENV === 'production';

module.exports = {
  plugins: [
    tailwind('./tailwind.config.js'),
    require('autoprefixer'),
    isProd ? cssnano({ preset: 'default' }) : null,
  ],
};

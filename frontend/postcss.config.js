tailwind = require('tailwindcss');
cssnano = require('cssnano');

module.exports = {
  plugins: [
    tailwind('./tailwind.config.js'),
    require('autoprefixer'),
    cssnano({ preset: 'default' }),
  ],
};

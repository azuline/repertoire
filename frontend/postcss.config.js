tailwind = require('tailwindcss');

module.exports = {
  plugins: [tailwind('./tailwind.config.js'), require('autoprefixer')],
};

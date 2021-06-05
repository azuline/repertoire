const plugin = require('tailwindcss/plugin');

module.exports = {
  darkMode: 'class',
  theme: {
    screens: {
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
      '2xl': '1440px',
    },
    extend: {
      colors: {
        'foreground-50': 'var(--color-foreground-50)',
        'foreground-100': 'var(--color-foreground-100)',
        'foreground-200': 'var(--color-foreground-200)',
        'foreground-300': 'var(--color-foreground-300)',
        'foreground-400': 'var(--color-foreground-400)',
        'foreground-500': 'var(--color-foreground-500)',
        'background-700': 'var(--color-background-700)',
        'background-800': 'var(--color-background-800)',
        'background-900': 'var(--color-background-900)',
        'background-950': 'var(--color-background-950)',
        'primary-400': 'var(--color-primary-400)',
        'primary-500': 'var(--color-primary-500)',
        'primary-600': 'var(--color-primary-600)',
        'primary-700': 'var(--color-primary-700)',
        'primary-800': 'var(--color-primary-800)',
      },
      backgroundOpacity: {
        7: '0.07',
      },
      spacing: {
        full: '100%',
        '1/24': '4.166666%',
      },
      width: {
        7.5: '1.875rem',
        18: '4.5rem',
        88: '22rem',
      },
      maxWidth: {
        '3/5': '60%',
      },
      minHeight: {
        48: '12rem',
        52: '13rem',
      },
      inset: {
        '1/2': '50%',
      },
      borderWidth: {
        10: '10px',
      },
      fill: {
        transparent: 'rgba(0, 0, 0, 0)',
      },
    },
  },
  plugins: [
    plugin(({ addComponents }) => {
      addComponents({
        '.full': {
          width: '100%',
          height: '100%',
        },
        '.truncate-2': {
          display: '-webkit-box',
          overflow: 'hidden',
          '-webkit-line-clamp': '2',
          '-webkit-box-orient': 'vertical',
        },
        '.rtl': {
          direction: 'rtl',
        },
        '.hover-bg': {
          '&:hover': {
            '--tw-bg-opacity': '5%',
            'background-color': 'rgba(255, 255, 255, var(--tw-bg-opacity))',
            '.light &': {
              'background-color': 'rgba(0, 0, 0, var(--tw-bg-opacity))',
            },
          },
        },
        '.pad-page': {
          'padding-left': '1.5rem',
          'padding-right': '1.5rem',
          '@screen xl': {
            'padding-left': '4rem',
            'padding-right': '4rem',
          },
          '@screen lg': {
            'padding-left': '3rem',
            'padding-right': '3rem',
          },
          '@screen md': {
            'padding-left': '2rem',
            'padding-right': '2rem',
          },
        },
      });
    }),
  ],
};

module.exports = {
  darkMode: 'class',
  purge: ['./src/**/*.tsx', './src/**/*.html'],
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
        foreground: 'var(--color-foreground)',
        'foreground-alt': 'var(--color-foreground-alt)',
        background: 'var(--color-background)',
        'background-alt': 'var(--color-background-alt)',
        'background-alt2': 'var(--color-background-alt2)',
        primary: 'var(--color-primary)',
        'primary-alt': 'var(--color-primary-alt)',
        'primary-alt2': 'var(--color-primary-alt2)',
        'primary-alt3': 'var(--color-primary-alt3)',
        gold: {
          400: '#daa520',
          500: '#b78846',
          600: '#a57a3f',
          700: '#6e522a',
          800: '#523d20',
          900: '#372915',
        },
      },
      spacing: {
        full: '100%',
        '1/24': '4.166666%',
      },
      width: {
        88: '22rem',
      },
      inset: {
        '1/2': '50%',
      },
      borderWidth: {
        10: '10px',
      },
    },
  },
  variants: {
    backgroundOpacity: ['dark', 'hover'],
    fontWeight: ['hover'],
    display: ['responsive'],
    maxWidth: ['responsive', 'focus'],
  },
};

module.exports = {
  darkMode: 'class',
  theme: {
    screens: {
      xs: '480px',
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
        gold: {
          50: '#FBF9F6',
          100: '#F8F3ED',
          200: '#EDE1D1',
          300: '#E2CFB5',
          400: '#CDAC7E',
          500: '#B78846',
          600: '#A57A3F',
          700: '#6E522A',
          800: '#523D20',
          900: '#372915',
        },
      },
      spacing: {
        full: '100%',
        '1/24': '4.166666%',
      },
      width: {
        84: '21rem',
      },
      inset: {
        '1/2': '50%',
      },
      borderWidth: {
        10: '10px',
        12: '12px',
        14: '14px',
      },
      maxWidth: {
        xxs: '16rem',
      },
    },
  },
  variants: {
    backgroundOpacity: ['dark', 'hover'],
    borderWidth: ['responsive', 'hover', 'focus'],
    display: ['responsive', 'hover'],
    maxWidth: ['responsive', 'focus'],
  },
};

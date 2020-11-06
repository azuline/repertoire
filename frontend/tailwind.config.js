module.exports = {
  theme: {
    screens: {
      xsm: '480px',
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
      '2xl': '1440px',
    },
    extend: {
      colors: {
        fg: 'var(--color-fg)',
        'fg-alt': 'var(--color-fg-alt)',
        bg: 'var(--color-bg)',
        'bg-alt': 'var(--color-bg-alt)',
        'bg-alt2': 'var(--color-bg-alt2)',
        'bg-embellish': 'var(--color-bg-embellish)',
        highlight: 'var(--color-highlight)',
        bold: 'var(--color-bold)',
        success: 'var(--color-success)',
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
        7: '1.75rem',
        full: '100%',
        '1/24': '4.166666%',
      },
      height: {
        '1/2': '50%',
      },
      width: {
        14: '3.5rem',
        28: '7rem',
        36: '9rem',
        44: '11rem',
        52: '13rem',
        60: '15rem',
      },
      opacity: {
        2: '.02',
        3: '.03',
        4: '.04',
        5: '.05',
        10: '.1',
        20: '.2',
        30: '.3',
        40: '.4',
        50: '.5',
        60: '.6',
        70: '.7',
        80: '.8',
        90: '.9',
      },
      inset: {
        '1/2': '50%',
      },
      transitionProperty: {
        width: 'width',
        height: 'height',
      },
    },
  },
  variants: {
    borderWidth: ['responsive', 'hover', 'focus'],
    display: ['responsive', 'hover'],
    opacity: ['hover'],
    width: ['responsive', 'focus'],
  },
};

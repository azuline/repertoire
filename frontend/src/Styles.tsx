import { styled } from 'twin.macro';

import { colors } from '~/colors';

export const AppStyles = styled.div`
  --lh: 1.4rem;
  line-height: var(--lh);
  font-family: 'Montserrat', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';

  /* Set theme colors. */

  --color-gray-500: #6b7280; /* coolGray-500 */

  --color-foreground-50: ${colors.foreground[50]};
  --color-foreground-100: ${colors.foreground[100]};
  --color-foreground-200: ${colors.foreground[200]};
  --color-foreground-300: ${colors.foreground[300]};
  --color-foreground-400: ${colors.foreground[400]};
  --color-foreground-500: ${colors.foreground[500]};
  --color-background-700: ${colors.background[700]};
  --color-background-800: ${colors.background[800]};
  --color-background-900: ${colors.background[900]};
  --color-background-950: ${colors.background[950]};
  --color-primary-400: ${colors.primary[400]};
  --color-primary-500: ${colors.primary[500]};
  --color-primary-600: ${colors.primary[600]};
  --color-primary-700: ${colors.primary[700]};
  --color-primary-800: ${colors.primary[800]};

  /* Style scrollbars. */

  * {
    scrollbar-color: var(--color-gray-500) transparent;
    scrollbar-width: thin;
  }
  *::-webkit-scrollbar {
    background-color: transparent;
    width: 0.375rem;
    height: 0.375rem;
  }
  *::-webkit-scrollbar-thumb {
    background-color: var(--color-gray-500);
  }
`;

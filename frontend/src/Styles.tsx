import { styled } from 'twin.macro';

export const AppStyles = styled.div`
  --lh: 1.4rem;
  line-height: var(--lh);
  font-family: 'Montserrat', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol', 'Noto Color Emoji';

  /* Set theme colors. */

  --color-foreground: #f9fafb;
  --color-foreground-100: #f3f4f6;
  --color-foreground-200: #e5e7eb;
  --color-foreground-300: #d1d5db;
  --color-foreground-400: #9ca3af;
  --color-background-700: #101013;
  --color-background-800: #18181d;
  --color-background-900: #1b1b21;
  --color-primary-400: #daa520;
  --color-primary-500: #a47b40;
  --color-primary-600: #96703a;
  --color-primary-700: #6e522a;
  --color-primary-800: #523d20;
  --color-gray-500: #6b7280; /* coolGray-500 */

  /* Style scrollbars. */

  * {
    scrollbar-color: var(--color-gray-500) transparent;
    scrollbar-width: thin;
  }
  ::-webkit-scrollbar {
    background-color: transparent;
    width: 0;
    height: 0.375rem;
  }
  ::-webkit-scrollbar-thumb {
    background-color: var(--color-gray-500);
  }
`;

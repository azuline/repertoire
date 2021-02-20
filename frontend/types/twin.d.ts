import { css as cssImport } from '@emotion/react';
// The css prop: https://emotion.sh/docs/typescript#css-prop
import {} from '@emotion/react/types/css-prop';
import styledImport from '@emotion/styled';

declare module 'twin.macro' {
  const styled: typeof styledImport;
  const css: typeof cssImport;
}

declare global {
  namespace JSX {
    interface IntrinsicAttributes<T> extends DOMAttributes<T> {
      as?: string;
    }
  }
}

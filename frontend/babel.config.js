module.exports = {
  extends: '@snowpack/app-scripts-react/babel.config.json',
  plugins: [
    'babel-plugin-twin',
    'babel-plugin-macros',
    [
      '@emotion/babel-plugin-jsx-pragmatic',
      {
        export: 'jsx',
        import: '__cssprop',
        module: '@emotion/react',
      },
    ],
    [
      '@babel/plugin-transform-react-jsx',
      {
        pragma: '__cssprop',
        pragmaFrag: 'React.Fragment',
      },
    ],
  ],
};

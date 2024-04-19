import babel from '@rollup/plugin-babel';

const config = {
  input: 'src/static/js/main.js',
  output: {
    file: 'src/static/dist/bundle.js',
    format: 'es'
  },
  plugins: [babel({ babelHelpers: 'bundled' })]
};

export default config;
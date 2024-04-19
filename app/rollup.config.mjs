import babel from "@rollup/plugin-babel";
import { nodeResolve } from "@rollup/plugin-node-resolve";
import terser from '@rollup/plugin-terser';

const config = {
  input: "src/static/js/main.js",
  output: {
    file: "src/static/dist/bundle.js",
    format: "es",
  },
  plugins: [babel({ babelHelpers: "bundled" }), nodeResolve(), terser()],
};

export default config;

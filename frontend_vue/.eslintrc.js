module.exports = {
    root: true,
    env: {
      node: true,
    },
    extends: [
      'plugin:vue/essential',
      'eslint:recommended',
      '@vue/prettier',
    ],
    parserOptions: {
      parser: 'babel-eslint',
    },
    rules: {
      'prettier/prettier': ['error', {
        endOfLine: 'auto',
      }],
      // other rules
    },
  };
  
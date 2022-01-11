module.exports = {
  lintOnSave: false,
  rules: {
    '@typescript-eslint/no-var-requires': 0,
  },
};

const path = require('path');

module.exports = {
  assetsDir: process.env.NODE_ENV === 'production'? '../static' : 'static',
  publicPath: process.env.NODE_ENV === 'production'? './' : '/',
  outputDir: path.resolve(__dirname, '../templates'),
}
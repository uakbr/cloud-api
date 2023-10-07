const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  // 1. Define entry point
  entry: './src/index.js',

  // 2. Define output point
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },

  // 3. Specify loaders and rules
  module: {
    rules: [
      // Handling JS and JSX files
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader'],
      },
      // Handling CSS files
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      // Handling image files
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
    ],
  },

  // 4. Configure plugins
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
  ],

  // 5. Set up development server settings
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 9000,
    hot: true,
  },
};
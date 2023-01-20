const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const each = require('lodash/fp/each')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

class RelativeBundleTrackerPlugin extends BundleTracker {
  convertPathChunks(chunks){
    each(each(chunk => {
      chunk.path = path.relative(this.options.path, chunk.path)
    }))(chunks)
  }
  writeOutput(compiler, contents) {
    if (contents.status === 'done')  {
      this.convertPathChunks(contents.chunks)
    }

    super.writeOutput(compiler, contents)
  }
}
module.exports = {
  context: __dirname,
  //  mode: 'production',
  entry: ['./assets/js/app.js', './assets/scss/app.scss'],
  output: {
    path: path.resolve('./static/bundles/'),
    filename: "[name]-[hash].js",
    chunkFilename: "[name]-[hash].js"
  },

  plugins: [
    new CleanWebpackPlugin(),
    new RelativeBundleTrackerPlugin({filename: './webpack-stats.json', path: '.'}),
    new ExtractTextPlugin({
      filename: "[name]-[hash].css",
      allChunks: true,
    }),
    new VueLoaderPlugin(),
  ],

  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ],
      },
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          //resolve-url-loader may be chained before sass-loader if necessary
          use: ['css-loader', 'sass-loader']
        })
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
            // Since sass-loader (weirdly) has SCSS as its default parse mode, we map
            // the "scss" and "sass" values for the lang attribute to the right configs here.
            // other preprocessors should work out of the box, no loader config like this necessary.
            'scss': [
              'vue-style-loader',
              'css-loader',
              'sass-loader'
            ],
            'sass': [
              'vue-style-loader',
              'css-loader',
              'sass-loader?indentedSyntax'
            ]
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.(woff2?|ttf|otf|eot)$/,
        exclude: /node_modules/,
        loader: 'file-loader',
        options: {
          name: '[path][name].[ext]'
        }
      }
    ],
  },
  
  resolve: {
    modules: ['node_modules'],
    extensions: ['.js'],
    alias: {
      'vue$': 'vue/dist/vue.common.js'
    }
  },
  performance: {
    maxEntrypointSize: 51200000,
    maxAssetSize: 51200000
  },
}


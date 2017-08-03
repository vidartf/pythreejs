module.exports = function (config) {
  config.set({
    basePath: '..',
    frameworks: ['mocha'],
    reporters: ['mocha'],
    client: {
      mocha: {
        timeout : 20000, // 20 seconds - upped from 2 seconds
        //retries: 3 // Allow for slow server on CI.
      }
    },
    browserNoActivityTimeout: 21000, // 21 seconds - upped from 10 seconds
    files: [
      'test/injector.js',
      'test/src/index.js'
    ],
    preprocessors: {
      'test/src/index.js': ['webpack']
    },
    webpack: {
      module: {
        loaders: [
          { test: /\.json$/, loader: "json-loader" }
        ],
      }
    },
    port: 9876,
    colors: true,
    singleRun: true,
    logLevel: config.LOG_INFO
  });
};

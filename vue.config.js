module.exports = {
  filenameHashing: false,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:80'
      }
    }
  },
}
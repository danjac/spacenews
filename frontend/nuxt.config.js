module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'spacenews',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Nuxt.js project' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        type: 'text/css',
        crossorigin: 'anonymous',
        href: 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
        integrity:'sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm'
      }
    ]
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/toast',
    ['bootstrap-vue/nuxt', { css: false }]
  ],
  serverMiddleware: [
    '~/server/session',
    '~/server/csrf',
    '~/server/auth',
    '~/server/api'
  ],
  toast: {
    position: 'center',
    theme: 'bubble'
  },
  /* Plugins */
  plugins: [
    // '~/plugins/bootstrap',
    '~/plugins/validate',
    '~/plugins/axios'
  ],
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}

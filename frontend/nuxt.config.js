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
    '@nuxtjs/auth',
    '@nuxtjs/toast',
    'bootstrap-vue/nuxt'
  ],
  axios: {
    proxy: true
  },
  proxy: {
    '/api': 'http://django:8000'
  },
  toast: {
    position: 'center',
    theme: 'bubble'
  },
  auth: {
    fetchUserOnLogin: true,
    endpoints: {
      login: { url: '/api/auth/token/create/', method: 'post', propertyName: 'auth_token' },
      logout: { url: '/api/auth/token/destroy/', method: 'post' },
      user: { url: '/api/auth/me/', propertyName: false },
    },
    token: {
      type: 'Token',
      name: 'token'
    },
    redirect: {
      login: '/login',
      home: '/'
    }
  },
  /* Plugins */
  plugins: [
    // '~/plugins/bootstrap',
    '~/plugins/validate'
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

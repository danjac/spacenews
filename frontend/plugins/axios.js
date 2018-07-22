export default function ({ $axios, redirect }) {
  $axios.onRequest(config => {
    config.xsrfHeaderName = 'x-csrf-token'
    config.xsrfCookieName = 'csrf-token'
  })
}

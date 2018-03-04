export default function({ $axios }) {
  $axios.onRequest(config => {
    config.xsrfCookieName = 'csrftoken'
    config.xsrfHeaderName = 'X-CSRFToken'
  })
}

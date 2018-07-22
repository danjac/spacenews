export default {
  state: () => ({
    loggedIn: false,
    user: null
  }),
  actions: {
    async nuxtServerInit ({ commit }, { req, app }) {
      console.log('nuxtServerInit', req.session.authToken)
      if (req.session.authToken) {
        const data = await app.$axios.$get('/api/auth/me/')
        commit('SET_USER', data)
      } else {
        commit('SET_USER', null)
      }
    },
    async login ({ commit }, creds) {
      await this.$axios.$post('/auth/login/', creds)
      const data = await this.$axios.$get('/api/auth/me/')
      commit('SET_USER', data)
    },
    logout ({ commit }) {
      this.$axios.$post('/auth/logout/')
      commit('SET_USER', null)
    }
  },
  mutations: {
    SET_USER (state, user) {
      if (user) {
        state.loggedIn = true
        state.user = user
      } else {
        state.loggedIn = false
        state.user = null
      }
    }
  }
}

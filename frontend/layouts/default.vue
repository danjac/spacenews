<template>
  <b-container class="mt-4">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-navbar-brand to="/">Space News</b-navbar-brand>
      <b-collapse is-nav id="nav-collapse">

        <b-navbar-nav>
          <b-nav-item to="/" exact>New</b-nav-item>
          <b-nav-item to="/comments">Comments</b-nav-item>
          <b-nav-item to="/submit">Submit</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto" v-if="$store.state.loggedIn">
          <b-nav-text>{{ $store.state.user.username }}</b-nav-text>
          <b-nav-item @click.prevent="logout()">Logout</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto" v-if="!$store.state.loggedIn">
          <b-nav-item to="/login">Login</b-nav-item>
          <b-nav-item to="/signup">Signup</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <b-container class="mt-2">
      <nuxt/>
    </b-container>

  </b-container>
</template>

<script>
export default {
  methods: {
    logout () {
    }
  }
}
</script>

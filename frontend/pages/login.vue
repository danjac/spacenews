<template>
  <div>
    <b-form @submit.prevent="submit" novalidate>
      <b-form-group label="Username" :invalid-feedback="errors.first('username')" :state="!errors.has('username')">
        <b-form-input type="text" name="username" v-model="form.username" v-validate="'required'"></b-form-input>
      </b-form-group>
      <b-form-group label="Password" :invalid-feedback="errors.first('password')" :state="!errors.has('password')">
        <b-form-input type="password" name="password" v-model="form.password" v-validate="'required'"></b-form-input>
      </b-form-group>
      <b-button variant="primary" size="lg" type="submit">Login</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      form: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async submit () {
      try {
        await this.$store.dispatch('login', this.form)
        let nextUrl = '/'
        if (this.$route.query.next) {
          nextUrl = decodeURIComponent(this.$route.query.next)
        }
        if (!nextUrl.startsWith('/')) {
          nextUrl = '/'
        }
        this.$router.push(nextUrl)
        this.$toast.success('Logged in')
      } catch(e) {
        this.$toast.error('Bad credentials')
      }
    }
  }
}
</script>

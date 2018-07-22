<template>
  <div>
    <b-form @submit.prevent="submit" novalidate>
      <b-form-group label="Username" :invalid-feedback="errors.first('username')" :state="!errors.has('username')">
        <b-form-input type="text" name="username" v-model="form.username" v-validate="'required'"></b-form-input>
      </b-form-group>
      <b-form-group label="Email address" :invalid-feedback="errors.first('email')" :state="!errors.has('email')">
        <b-form-input type="text" name="email" v-model="form.email" v-validate="'required|email'"></b-form-input>
      </b-form-group>
      <b-form-group label="Password" :invalid-feedback="errors.first('password')" :state="!errors.has('password')">
        <b-form-input type="password" data-vv-value-path="innerValue" name="password" v-model="form.password" v-validate="'required'"></b-form-input>
      </b-form-group>
      <b-form-group
          label="Repeat Password"
          :invalid-feedback="errors.first('password_rpt')"
          :state="!errors.has('password_rpt')">
        <b-form-input
          type="password"
          data-vv-as="password"
          data-vv-value-path="innerValue"
          name="password_rpt"
          v-model="form.password_rpt"></b-form-input>
      </b-form-group>
      <b-button variant="primary" size="lg" type="submit">Signup</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      form: {
        username: '',
        email: '',
        password: '',
        password_rpt: ''
      }
    }
  },
  methods: {
    async submit () {
      await this.$validator.validateAll()
      if (this.errors.any()) {
        return
      }
      try {
        await this.$axios.post('/api/auth/users/create/', this.form)
        this.$toast.success('Congrats! Please log in with your new credentials.')
        this.$router.push('/login/?redirect=/')
      } catch(e) {
        // tbd: handle form errors
        if (e.response.data && e.response.data) {
           for (var field of Object.keys(e.response.data)) {
             this.$validator.errors.add(field, e.response.data[field][0])
           }
        }
        this.$toast.error('invalid signup')
      }
    }
  }
}
</script>

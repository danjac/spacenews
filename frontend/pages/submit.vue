<template>
  <div>
    <b-form @submit.prevent="submit" novalidate>
      <b-form-group label="Title" :invalid-feedback="errors.first('title')" :state="!errors.has('title')">
        <b-form-input type="text" name="title" v-model="form.title" v-validate="'required'"></b-form-input>
      </b-form-group>
      <b-form-group label="URL" :invalid-feedback="errors.first('url')" :state="!errors.has('url')">
        <b-form-input type="text" name="url" v-model="form.url" v-validate="'url'"></b-form-input>
      </b-form-group>
      <b-form-group label="Description">
        <b-form-textarea name="description" v-model="form.description"></b-form-textarea>
      </b-form-group>
      <b-button variant="primary" size="lg" type="submit">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  middleware: ['auth'],
  data () {
    return {
      form: {
        title: '',
        url: '',
        description: ''
      }
    }
  },
  methods: {
    async submit () {
      await this.$validator.validateAll()
      if (this.errors.any()) {
        return
      }
      // check valid etc....
      await this.$axios.post('/api/posts/', this.form)
      this.$router.push('/')
    }
  }

}
</script>

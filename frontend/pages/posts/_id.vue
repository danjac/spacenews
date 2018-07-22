<template>
  <div>
    <post :post="post"></post>
    <b-form v-if="$store.state.loggedIn" @submit.prevent="submitComment" novalidate class="mt-4">
      <b-form-group
        :invalid-feedback="errors.first('content')"
        :state="!errors.has('content')">
        <b-form-textarea
          name="content"
          v-model="form.content"
          placeholder="Add your comment"
          rows="8"
          class="mb-3"
          v-validate="'required'"></b-form-textarea>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit comment</b-button>
    </b-form>
    <comment v-for="comment in topComments" :comment="comment" :key="comment.id" :depth="1"></comment>
  </div>
</template>

<script>

import Post from '~/components/Post'
import Comment from '~/components/Comment'

export default {
  components: {
    Post,
    Comment
  },
  async asyncData ({ app, params }) {

    let response = await app.$axios.get(`/api/posts/${params.id}/`)
    const post = response.data

    response = await app.$axios.get(`/api/posts/${params.id}/comments/`)

    const comments = response.data
    const topComments = comments.filter(comment => !comment.parent)

    const appendChildren = parent => {
      parent.comments = comments.filter(comment => comment.parent === parent.id)
      parent.comments.forEach(comment => appendChildren(comment))
    }

    topComments.forEach(parent => appendChildren(parent))

    return {
      post,
      topComments
    }

  },
  data() {
    return {
      form: {
      }
    }
  },
  methods: {
    async submitComment () {

      await this.$validator.validateAll()

      if (this.errors.any()) {
        return
      }

      // handle 400 etc...
      const response = await this.$axios.post(`/api/posts/${this.post.id}/add_comment/`, this.form)

      this.topComments.splice(0, 0, response.data)
      this.form = {}
      this.$nextTick(() => {
        this.$validator.reset()
      })
    }
  }
}
</script>

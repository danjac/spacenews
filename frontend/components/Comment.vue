<template>
  <b-card class="mt-4">
    <p>{{ comment.content }}</p>
    <p>
      Posted by [ <nuxt-link to="/">{{ comment.author.username }}</nuxt-link> ] {{ ago }}
    </p>
    <p v-if="$store.state.loggedIn">
      [ <a href="#" @click.prevent="toggleReplyForm">Reply</a> ]
    </p>
    <b-form v-show="showReplyForm" novalidate class="my-4" @submit.prevent="reply">
      <b-form-group
        :invalid-feedback="errors.first('content')"
        :state="!errors.has('content')">
        <b-form-textarea
          name="content"
          v-model="replyForm.content"
          placeholder="Add your comment"
          rows="8"
          class="mb-3"
          v-validate="'required'"></b-form-textarea>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit comment</b-button>
      <b-button type="reset" variant="secondary" @click.prevent="toggleReplyForm">Cancel</b-button>
     </b-form>

    <comment v-for="comment in comment.comments"
             :comment="comment"
             :key="comment.id"
             :style="style"
             :depth="depth + 10">
    </comment>
  </b-card>
</template>

<script>
import moment from 'moment'

export default {
  name: 'comment',
  props: ['comment', 'depth'],
  data () {
    return {
      style: {
        paddingLeft: this.depth * 10
      },
      showReplyForm: false,
      replyForm: {
        content: ''
      },
      ago: moment(this.comment.created).fromNow()
    }
  },
  methods: {
    clearReplyForm () {
      this.replyForm.content = ''

      this.$nextTick(() => {
        this.$validator.reset()
      })
    },
    toggleReplyForm () {
      this.showReplyForm = !this.showReplyForm
      this.clearReplyForm()
    },
    async reply () {
      await this.$validator.validateAll()
      if (this.errors.any()) {
        return
      }
      const response = await this.$axios.post(`/api/comments/${this.comment.id}/reply/`, this.replyForm)
      if (!this.comment.comments) {
        this.comment.comments = []
      }
      this.comment.comments.push(response.data)
      this.toggleReplyForm()
    }
  }
}
</script>

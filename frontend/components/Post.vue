<template>
  <div v-show="!deleted">
  <b-card>
    <h6 v-if="post.url"><a :href="post.url">{{ post.title }}</a></h6>
    <h6 v-if="!post.url"><nuxt-link to="/">{{ post.title }}</nuxt-link></h6>
    <p>
      Posted by [ <nuxt-link to="/">{{ post.author.username }}</nuxt-link> ] {{ ago }}
    </p>
    <p v-if="$store.state.loggedIn">
      [ <nuxt-link :to="`/posts/${post.id}`">Discuss</nuxt-link> ]
      <span v-if="post.is_owner">
      [ <nuxt-link to="/">Edit</nuxt-link> ]
      [ <b-btn variant="link" class="p-0" v-b-modal="modalId">Delete</b-btn> ]
     </span>
    </p>
    <p v-if="!$store.state.loggedIn">
      [ <nuxt-link :to="`/posts/${post.id}`">Details</nuxt-link> ]
      [ <nuxt-link :to="{path: '/login', query: {redirect: $route.path}}">Login to comment</nuxt-link> ]
    </p>
  </b-card>
  <b-modal :id="modalId" title="Delete Post" @ok="deletePost">
    <p>Are you sure you want to delete this post? All comments will be deleted too!</p>
  </b-modal>
</div>
</template>


<script>
import moment from 'moment'

export default {
  props: ['post'],
  data () {
    return {
      deleted: false,
      ago: moment(this.post.created).fromNow(),
      modalId: `deleteConfirm-${this.post.id}`
    }
  },
  methods: {
    deletePost () {
      // TBD: add a post-delete action to props
      this.$axios.delete(`/api/posts/${this.post.id}/`)
      this.deleted = true
      this.$toast.success('Post deleted')
    }
  }
}
</script>

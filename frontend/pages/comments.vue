<template>
  <div>
  <b-card class="mt-4" v-for="comment in comments" :key="comment.id">
      <p><nuxt-link :to="`/posts/${comment.post}/`">{{ comment.content }}</nuxt-link></p>
    <p>
      Posted by [ <nuxt-link to="/">{{ comment.author.username }}</nuxt-link> ]
    </p>
   </b-card>
  </div>
</template>

<script>

export default {
  async asyncData ({ app }) {
    try {
      const response = await app.$axios.get('/api/comments/')
      return {
        comments: response.data.results,
        error: false
      }
    } catch (e) {
      console.log('error', e)
      return {
        comments: [],
        error: true
      }
    }
  }
}

</script>

<style>

</style>

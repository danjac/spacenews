import test from 'ava'
import { mount } from '@vue/test-utils'
import Vue from 'vue'
import Post from '../../components/Post'

let wrapper

test.beforeEach(() => {
  wrapper = mount(Post, {
    propsData: {
      post: {
        id: 1,
        title: "test",
        author: {
          username: 'tester'
        },
        created: new Date()
      },
      loggedIn: false
    },
    mocks: {
      $route: {
        path: '/'
      },
      $auth: {
        state: {
          loggedIn: false
        }
      }
    }
  })
})

test('it should run', (t) => {
  // checking test setup
  t.truthy(true)
})

test('it should render the component', (t) => {
  // check we have the props content...
  t.regex(wrapper.text(), /test/)
})
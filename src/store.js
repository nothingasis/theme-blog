import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articles: require('@/data/articles.json'),
    // articles: [],
    drawer: false,
    items: [
      {
        text: 'Home',
        to: '/'
      },
      {
        text: 'About',
        to: '/about'
      },
      {
        text: 'Contact',
        to: '/contact'
      },
      {
        text: 'After Care',
        to: '/aftercare'
      },
      {
        text: 'Book Appointment',
        target: "_blank",
        href: 'https://square.site/book/FH4JMT69VE5JE/roah-cosmetics-lashes-sacramento-ca'
      }
    ]
  },
  getters: {
    categories: state => {
      const categories = []

      for (const article of state.articles) {
        if (
          !article.category ||
          categories.includes(article.category)
        ) continue

        const text = article.category

        categories.push({
          text,
          to: `/category/${text}`
        })
      }

      return categories.sort().slice(0, 4)
    },
    links: (state, getters) => {
      return state.items
      // .concat(getters.categories)
    }
  },
  mutations: {
    setDrawer: (state, payload) => (state.drawer = payload),
    toggleDrawer: state => (state.drawer = !state.drawer),
    filterArticles: (state, searchinput) => {
      state.articles = require('@/data/articles.json').filter(art => {
        return art.title.toLowerCase().includes(searchinput.toLowerCase())
      })
    }
  },
  actions: {
    filterArticles ({ commit }, data) {
      console.log('filterArticles: ', data)
      commit('filterArticles', data)
    }
  }
})

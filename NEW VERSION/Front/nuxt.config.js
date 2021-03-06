export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'MoneyItStep',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
		'aos/dist/aos.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
		{ src: '~plugins/vue-radial-progress', ssr: false },
		{ src: '~plugins/aos.js', ssr: false },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,
	moment: {
		defaultLocale: 'ru',
		locales: ['ru']
	},

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
		'@nuxtjs/moment',
		['nuxt-fontawesome', {
				component: 'fa',
				imports: [
					{
						set: '@fortawesome/free-solid-svg-icons',
						icons: ['fas']
					},
					{
						set:'@fortawesome/free-brands-svg-icons',
						icons: ['fab']
					}
				]
		}],
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}

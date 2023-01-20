import Vue from 'vue'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import Datepicker from 'vuejs-datepicker';
import {en, es} from 'vuejs-datepicker/dist/locale'
import { CountUp } from 'countup.js';
// require styles
import 'swiper/dist/css/swiper.css'
//Components
import SolicitarCita from './components/SolicitarCita.vue'
import SolicitarCitaYa from './components/SolicitarCitaYa.vue'

window.CountUp = CountUp
Vue.use(VueAwesomeSwiper, /* { default global options } */)

Vue.component('datepicker', Datepicker)
Vue.component('solicitar-cita', SolicitarCita)
Vue.component('solicitar-citaya', SolicitarCitaYa)
new Vue({
  el: '#app',
  data: {
    menu: false,
    es,
    swiperOptions: {
      loop: true,
      autoplay: {
        delay: 3500,
        disableOnInteraction: true
      },
    },
    disabledDates: {
      to: new Date()
    }
  }
})


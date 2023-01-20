<template>
  <div>
    <h1 class="title is-gothampro">Agenda tu cita ya!</h1>
    <div class="columns">
      <div class="column">
        <form action="#" class="columns is-multiline"
          @submit.prevent="submitForm">

          <div class="column is-6">
            <datepicker :disabled-dates="disabledDates" :language="es"
              input-class="input date" placeholder="Selecciona la fecha"
              v-model="fecha"></datepicker>
          </div>
          <div class="column is-6">
            <div class="select yellow">
              <select v-model="sede" required>
                <option selected disabled value="">Escoge tu sede
                </option>
              <option>Modelia</option>
              <option>Chicó</option>
              <option>Restrepo</option>
              </select>
            </div>
          </div>
          <div class="column is-6">
            <input class="input" type="text" placeholder="Nombre y apellido"
            v-model="name" required>
          </div>
          <div class="column is-6">
            <button type="submit" class="button has-bg-lightblue">
              <span>Pedir cita</span>
              <span class="icon">
                <i class="fab fa-whatsapp"></i>
              </span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
  
  
</template>

<script>
import {en, es} from 'vuejs-datepicker/dist/locale'
export default {
  data: () => ({
    es,
    name: '',
    fecha: '',
    sede: '',
    disabledDates: {
      to: new Date()
    }
  }),
  methods: {
    submitForm() {
      let el = document.querySelector('div.column.content > h1')
      let articulo = el.innerHTML
      let message = `Hola, mi nombre es ${this.name}, y deseo realizarme un
      ${articulo} en la sede de ${this.sede} el dia ${this.fecha.toLocaleDateString()}`

      let phone = ''
      if(this.sede == 'Modelia') {
        phone = '573502350616'
      } else {
        phone = '573505610150'
      }
      window.location.assign(`https://wa.me/${phone}?text=` + encodeURIComponent(message));
    }
  }
};
</script>

<style>
.input.date {
  background-color: #ffb4d9;
  color: #343434;
}

.input.date::placeholder {
  color: #343434;
}

.select.yellow select {
    background-color: #d9d1a8;
}
</style>

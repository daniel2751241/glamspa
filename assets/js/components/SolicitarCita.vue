<template>
  <div class="">
    <div class="">
      <form action="#" class="columns is-multiline is-variable is-1" @submit.prevent="submitForm">
        <div class="column is-2">
          <div class="select">
            <select v-model="procedimiento" required>
              <option selected disabled value="">Selecciona un
              Procedimiento</option>
              <option value="Cejas">Cejas</option>
              <option value="Pestañas">Pestañas</option>
              <option value="Manicure">Manicure</option>
              <option value="Pedicure">Pedicure</option>
              <option value="Depilacion Facial">Depilacion Facial</option>
              <option value="Depilacion Corporal">Depilacion Corporal</option>
            </select>
          </div>
        </div>
        <div class="column is-2">
          <div class="select">
            <select v-model="tipo" required>
              <option selected disabled value="">Tipo de procedimiento
              </option>
              <option v-for="option in options[procedimiento]"
                      :value="option">{{option}}</option>
            </select>
          </div>
        </div>
        <div class="column is-2">
          <div class="select" style="width: 100%;">
            <select v-model="sede" style="width: 100%;" required>
              <option selected disabled value="">Escoge tu sede
              </option>
              <option>Modelia</option>
              <option>Chicó</option>
              <option>Restrepo</option>
            </select>
          </div>
        </div>
        <div class="column">
          <datepicker :disabled-dates="disabledDates" :language="es"
            input-class="input" placeholder="Selecciona la fecha"
            v-model="fecha" required></datepicker>
        </div>
        <div class="column">
          <input required v-model="nombre" class="input" type="text" placeholder="Nombre y apellido">
        </div>
        <div class="column">
          <button type="submit" class="button">
            <span>Pedir cita</span>
            <span class="icon">
              <i class="fab fa-whatsapp"></i>
            </span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {en, es} from 'vuejs-datepicker/dist/locale'
export default {
  data: () => ({
    procedimiento: '',
    tipo: '',
    fecha: '',
    nombre: '',
    sede: '',
    options: {
      'Cejas': ['Diseño de cejas con cera', 'Diseño de cejas con hilo', 'Mapa de cejas',
        'Maquillaje de cejas ', 'Micropigmentación', 'Valoración micropigmentación',
        'Microblading', 'Microshading', 'Cejas compactas', 'Corrección tatuajes en cejas',
        'Borrado de tatuajes en cejas', 'Laminado de cejas',
      ],
      'Pestañas': ['Lifting de pestañas', 'Extensión de pestañas', 
        'Extensión clásica efecto pestañina', 'Extensión tipo seda', 'Volumen ruso',
        'Retoque de pestañas', 'Retoque extensión pestañas clásicas', 'Retoque tipo seda',
        'Retoque volumen ruso', 'Retiro de extensión de pestañas'
      ],
      'Depilacion Facial': ['Rostro completo cera', 'Frente', 'Pómulos',
        'Patillas', 'Nariz interna ', 'Bozo', 'Nariz externa', 'Orejas', 'Rostro completo hilo',
        'Frente', 'Pómulos', 'Patillas', 'Barbilla', 'Bozo', 'Nariz externa'
      ],
      'Depilacion Corporal': ['Depilación completa', 'Pecho', 'Espalda',
        'Axila', 'Media Pierna', 'Pierna Completa', 'Bikini completo',
        'Brazos'],
      'Manicure': ['Manicure tradicional', 'Manicure semipermanente o color gel', 'Manicure ruso (en seco)',
        'Uñas acrílicas esculpidas', 'Esmaltado tradicional', 'Esmaltado semipermanente', 'Puntas y estructuras',
        'Uñas tips', 'Recubrimiento acrílico', 'Mantenimientos uñas acrílicas',
        'Retirado semipermanente', 'Retirado uñas acrílicas', 'Spa de manos',
        'Chocolaterapia', 'Vitamina E', 'Parafina', 'Aromaterapia', 'Veloterapia'
      ],
      'Pedicure': ['Pedicure tradicional', 'Pedicure semipermanente', 'Spa de pies',
        'Chocolaterapia', 'Vitamina E', 'Parafina', 'Aromaterapia',
        'Veloterapia', 'Desintoxicacion ionica detox', 'Pediluvio de gel', 'Bomba sales minerales naturales'
      ]
    },
    es,
    disabledDates: {
      to: new Date()
    }
  }),
  methods: {
    submitForm() {
      let message = `Hola, mi nombre es ${this.nombre}, y deseo realizarme un
      ${this.tipo} en la sede de ${this.sede} el dia ${this.fecha.toLocaleDateString()}`
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

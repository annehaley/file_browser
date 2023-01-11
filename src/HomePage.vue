<script lang="ts">
import { defineComponent } from "vue";
import SaveDialog from "./components/SaveDialog.vue";

export default defineComponent({
  name: "HomePage",
  components: { SaveDialog },
  setup() {
    return {};
  },
});
</script>

<template>
  <div id="app">
    <v-app>
      <div class="d-flex">
        <save-dialog />
      </div>
    </v-app>
  </div>
</template>

<style scoped>
.container-1 {
  margin: 10px;
  padding: 10px;
  width: 400px;
  background-color: black;
}
.container-2 {
  margin: 10px;
  padding: 10px;
  border: 1px dashed black;
  width: 700px;
}
</style>

<script lang="ts">
import { defineComponent } from "vue";
import FileBrowser from "./components/FileBrowser.vue";

export default defineComponent({
  name: "HomePage",
  components: { FileBrowser },
  setup() {
    return {};
  },
});
</script>

<template>
  <div id="app">
    <v-app>
      <div class="d-flex">
        <file-browser />
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

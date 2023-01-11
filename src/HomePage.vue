<script lang="ts">
import { defineComponent, ref } from "vue";
import SaveDialog from "./components/SaveDialog.vue";

export default defineComponent({
  name: "HomePage",
  components: { SaveDialog },
  setup() {
    const currentLocalDir = ref(undefined);
    const currentRemoteDir = ref(undefined);

    return {
      localDirectories: [
        "/home/localUser/Documents",
        "/home/localUser/Downloads",
        "/home/localUser/Data",
        "/home/localUser/Data/One",
        "/home/localUser/Data/Two",
        "/home/localUser/Data/Three",
      ],
      remoteDirectories: [
        "remote_host:/root/data",
        "remote_host:/root/data/one",
        "remote_host:/root/data/two",
        "remote_host:/root/data/three",
      ],
      currentLocalDir,
      currentRemoteDir,
    };
  },
});
</script>

<template>
  <div id="app">
    <v-app>
      <div class="d-flex">
        <save-dialog
          :currentLocalDir="currentLocalDir"
          :currentRemoteDir="currentRemoteDir"
          :remoteDirectories="remoteDirectories"
          :localDirectories="localDirectories"
          @setLocalDir="(dir) => (currentLocalDir = dir)"
          @setRemoteDir="(dir) => (currentRemoteDir = dir)"
        />
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

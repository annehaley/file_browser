<script lang="ts">
import SaveDialog from "./components/SaveDialog.vue";

export default {
  name: "HomePage",
  components: { SaveDialog },
  methods: {
    getDirContents(dir: string) {
      console.log("getting random contents for", dir);
      const possibleFiles = [
        {
          name: "example1",
          type: "file",
          size: "10KB",
          modified: "10/30/22 12:23pm",
          owner: "root",
        },
        {
          name: "example2",
          type: "file",
          size: "20KB",
          modified: "10/30/22 2:00pm",
          owner: "root",
        },
        {
          name: "example3",
          type: "file",
          size: "30KB",
          modified: "10/30/22 3:00pm",
          owner: "root",
        },
        {
          name: "a big file",
          type: "file",
          size: "10MB",
          modified: "10/31/22 10:00pm",
          owner: "root",
        },
        {
          name: "foo",
          type: "file",
          size: "1MB",
          modified: "10/29/22 4:00pm",
          owner: "root",
        },
        {
          name: "bar",
          type: "file",
          size: "1MB",
          modified: "10/29/22 4:00pm",
          owner: "root",
        },
        {
          name: "Folder A",
          type: "folder",
          size: "--",
          modified: "10/29/22 4:00pm",
          owner: "root",
        },
        {
          name: "Folder B",
          type: "folder",
          size: "--",
          modified: "10/29/22 4:00pm",
          owner: "root",
        },
      ];
      return possibleFiles.filter(() => Math.random() < 0.5);
    }
  },
  data() {
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
      currentLocalDir: "/home/localUser/Data/One",
      currentRemoteDir: "remote_host:/root/data/one",
    };
  },
};
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
          :currentLocalDirContents="getDirContents(currentLocalDir)"
          :currentRemoteDirContents="getDirContents(currentRemoteDir)"
          @setLocalDir="(dir) => (currentLocalDir = dir)"
          @setRemoteDir="(dir) => (currentRemoteDir = dir)"
        />
      </div>
    </v-app>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    localDirectories: {
      type: Array,
      required: true,
    },
    remoteDirectories: {
      type: Array,
      required: true,
    },
    currentLocalDir: {
      type: String,
      default: undefined,
    },
    currentRemoteDir: {
      type: String,
      default: undefined,
    },
  },
  data() {
    return {
      dialogOpen: false,
      syncCurrentLocalAndRemote: false,
      unsyncedCurrentTab: "local",
      keywordFilter: undefined,
      categoryFilter: undefined,
    };
  },
  computed: {},
  methods: {},
  mounted() {
    console.log("mounted");
  },
  updated() {
    console.log("updated");
  },
};
</script>

<template>
  <div class="container">
    <v-btn color="primary" @click="dialogOpen = true"> Save </v-btn>
    <v-dialog
      v-model="dialogOpen"
      transition="dialog-bottom-transition"
      max-width="600"
    >
      <v-card>
        <v-card-text class="text-h6 grey lighten-2">
          Save
          <v-icon
            @click="dialogOpen = false"
            style="float: right; height: 30px"
          >
            mdi-close
          </v-icon>
        </v-card-text>
        <v-divider></v-divider>
      </v-card>
    </v-dialog>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  width: 100%;
  justify-content: space-around;
}
.v-dialog > .v-card > .v-card__text {
  padding: 5px 20px;
}
</style>

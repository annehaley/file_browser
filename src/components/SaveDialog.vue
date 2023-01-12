<script lang="ts">
import FileBrowser from "./FileBrowser.vue";
export default {
  components: { FileBrowser },
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
      dialogOpen: true,
      syncCurrentLocalAndRemote: false,
      unsyncedCurrentTab: "local",
      keywordFilter: undefined,
      categoryFilter: undefined,
    };
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

        <v-btn
          fab
          small
          class="sync-button"
          :color="syncCurrentLocalAndRemote ? 'primary' : ''"
          @click="syncCurrentLocalAndRemote = !syncCurrentLocalAndRemote"
        >
          <v-icon>mdi-folder-sync-outline</v-icon>
        </v-btn>
        <div v-if="!syncCurrentLocalAndRemote">
          <v-tabs
            fixed-tabs
            v-model="unsyncedCurrentTab"
            active-class="highlighted-tab"
          >
            <v-tab>Local</v-tab>
            <v-tab>Remote</v-tab>
          </v-tabs>
          <v-tabs-items v-model="unsyncedCurrentTab">
            <v-tab-item>
              <file-browser
                locationType="Local"
                :small="syncCurrentLocalAndRemote"
                :allDirectories="localDirectories"
                :currentDir="currentLocalDir"
                @setCurrentDir="(dir) => this.$emit('setLocalDir', dir)"
              />
            </v-tab-item>
            <v-tab-item>
              <file-browser
                locationType="Remote"
                :small="syncCurrentLocalAndRemote"
                :allDirectories="remoteDirectories"
                :currentDir="currentRemoteDir"
                @setCurrentDir="(dir) => this.$emit('setRemoteDir', dir)"
              />
            </v-tab-item>
          </v-tabs-items>
        </div>
        <div v-else class="sync-display">
          <div>
            <v-tabs fixed-tabs>
              <v-tab class="highlighted-tab">Local</v-tab>
            </v-tabs>
            <file-browser
              locationType="Local"
              :small="syncCurrentLocalAndRemote"
              :allDirectories="localDirectories"
              :currentDir="currentLocalDir"
              @setCurrentDir="(dir) => this.$emit('setLocalDir', dir)"
            />
          </div>
          <div>
            <v-tabs fixed-tabs>
              <v-tab class="highlighted-tab">Remote</v-tab>
            </v-tabs>
            <file-browser
              locationType="Remote"
              :small="syncCurrentLocalAndRemote"
              :allDirectories="remoteDirectories"
              :currentDir="currentRemoteDir"
              @setCurrentDir="(dir) => this.$emit('setRemoteDir', dir)"
            />
          </div>
        </div>
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
.sync-button {
  position: absolute;
  right: calc(50% - 20px);
  z-index: 1;
}
.sync-display {
  display: flex;
  width: 100%;
}
.sync-display > div {
  width: 50%;
}
.highlighted-tab {
  background-color: lightblue !important;
}
.v-dialog > .v-card > .v-card__text {
  padding: 5px 20px;
}
</style>

<script lang="ts">
export default {
  props: {
    locationType: {
      type: String,
      required: true,
    },
    allDirectories: {
      type: Array,
      required: true,
    },
    currentDir: {
      type: String,
      default: undefined,
    },
  },
  data() {
    return {};
  },
};
</script>

<template>
  <v-card>
    <div class="dir-select-box">
      <v-select
        :items="allDirectories"
        :value="currentDir"
        :label="locationType + ' Directory'"
        class="dir-select"
        solo
        hide-details=""
        @change="(dir) => this.$emit('setCurrentDir', dir)"
      />
      <v-btn x-small style="height: 45px">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-btn x-small style="height: 45px">
        <v-icon>mdi-arrow-right</v-icon>
      </v-btn>
      <v-btn x-small style="height: 45px">
        <v-icon>mdi-folder-arrow-up-outline</v-icon>
      </v-btn>

      <v-btn x-small style="height: 45px; margin-left: 10px">
        <v-icon>mdi-folder-plus-outline</v-icon>
      </v-btn>
    </div>
  </v-card>
</template>

<style scoped>
.dir-select-box {
  padding: 10px 15px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  row-gap: 10px;
  background-color: lightgrey;
}
.dir-select {
  margin-right: 10px;
  min-width: 200px;
  background-color: white;
}
</style>

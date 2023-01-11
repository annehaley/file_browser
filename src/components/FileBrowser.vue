<script lang="ts">
export default {
  props: {
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
  <v-card class="pa-3">hello world</v-card>
</template>

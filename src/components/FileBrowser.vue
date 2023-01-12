<script lang="ts">
export default {
  props: {
    locationType: {
      type: String,
      required: true,
    },
    small: {
      type: Boolean,
      default: true,
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
    return {
      filterString: undefined,
    };
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

    <div class="filter-box">
      <v-chip
        color="rgb(70, 70, 70)"
        small
        class="filter-button"
        text-color="white"
      >
        <v-avatar>
          <v-icon :small="small">mdi-history</v-icon>
        </v-avatar>
        <div v-if="!small" class="pl-1">Recents</div>
      </v-chip>
      <v-chip
        color="rgb(70, 70, 70)"
        small
        class="filter-button"
        text-color="white"
      >
        <v-avatar>
          <v-icon :small="small">mdi-heart</v-icon>
        </v-avatar>
        <div v-if="!small" class="pl-1">Favorites</div>
      </v-chip>
      <v-chip
        color="rgb(70, 70, 70)"
        small
        class="filter-button"
        text-color="white"
      >
        <v-avatar>
          <v-icon :small="small">mdi-folder-marker</v-icon>
        </v-avatar>
        <div v-if="!small" class="pl-1">Locations</div>
      </v-chip>
      <v-text-field
        v-model="filterString"
        prepend-icon="mdi-magnify"
        hide-details
        autofocus
        placeholder="Filter by keyword"
        class="filter-input"
      />
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
.filter-box {
  background-color: rgb(70, 70, 70);
  color: white;
  padding: 10px 15px;
  display: flex;
  align-items: center;
}
.filter-button {
  outline: 1px solid white;
  color: white;
  padding: 0px 5px;
  margin: 0px 3px;
  min-width: 32px;
}
.filter-input {
  background-color: white;
  height: 30px;
  border-radius: 20px;
  padding: 0px 10px;
  min-width: 20px;
  margin-top: 0;
  margin-left: 5px;
}
</style>

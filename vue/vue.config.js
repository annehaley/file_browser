const { defineConfig } = require("@vue/cli-service");

const path = require("path");
const DST_PATH = "../filebrowser/build";

module.exports = defineConfig({
  transpileDependencies: ["vuetify"],
  outputDir: path.resolve(__dirname, DST_PATH),
});

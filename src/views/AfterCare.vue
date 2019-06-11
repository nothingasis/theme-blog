<template>
  <v-container
    id="aftercare"
    tag="section"
  >
    <base-subheading>After Care</base-subheading>
    <under-construction/>
    <!-- <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
    <p v-html="editorData"></p> -->
  </v-container>
</template>

<script>
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';

export default {
  name: "AfterCare",
  components: {
    UnderConstruction: () => import('@/components/core/UnderConstruction.vue'),
  },
  data () {
    return {
      editor: ClassicEditor,
              editorData: '<p>Content of the editor.</p>',
              editorConfig: {
                  // The configuration of the editor.
              }
    }
  }
}
</script>


<template>
  <v-container
    id="aftercare"
    tag="section"
  >
    <!-- <base-subheading>After Care</base-subheading> -->
    <!-- <under-construction/> -->
    <!-- <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
    <p v-html="editorData"></p> -->
    <p class="text-xs-center font-weight-light display-2">After Care Services</p>
    <hr>
    <p class="my-4 text-xs-center font-weight-regular subheading">Reminder that after the application of lash extensions there may be unfavorable results which can include but not limited to: allergic reaction, irritation, burning, redness and soreness.</p>

    <p class="headline">TO KEEP YOUR EYES SAFE</p>

    <p>
      <ul>
        <li class="my-1">Try to keep lashes dry up to 48 hours after application.</li>
        <li class="my-1">Try to avoid getting water in your eyes during showers or any water activity during time frame.</li>
        <li class="my-1">Avoid workouts, steam room, or hot yoga which may cause adhesive to reactivate and cause lashes to stick together.</li>
        <li class="my-1">Resist the urge to pull, pick, and/or touch your lashes which can damage your natural lashes and can help avoid bacteria.</li>
        <li class="my-1">Do not use rich moisturizing products around your lashes. Shampoo, conditioners, or oil-based product can eventually loosen the adhesive bond.Tilting you head back when washing your hair will help avoid getting the lashes wet or expose to the products.</li>
        <li class="my-1">Do not apply mascara on top of lash extension; may cause irritation and redness.</li>
        <li class="my-1">If in any case redness occurs apply eyedrops to lessen redness and use every hour until redness is gone.</li>
        <li class="my-1">After application, lashes may fall out a little faster than normal due to: seasons/allergies, medication intake, feeling under the weather and/or oily skin.</li>
      </ul>
    </p>
  </v-container>
</template>

<script>
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

export default {
  name: "AfterCare",
  components: {
    UnderConstruction: () => import("@/components/core/UnderConstruction.vue")
  },
  data() {
    return {
      editor: ClassicEditor,
      editorData: "<p>Content of the editor.</p>",
      editorConfig: {
        // The configuration of the editor.
      }
    };
  }
};
</script>


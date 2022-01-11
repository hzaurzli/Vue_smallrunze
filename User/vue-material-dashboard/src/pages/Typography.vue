<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item">
        <md-card>
          <md-card-header data-background-color="green">
            <h4 class="title">Material Dashboard Heading</h4>
            <p class="category">Created using Roboto Font Family</p>
          </md-card-header>
          <md-card-content>
            <div id="typography">
              <div class="title">
                <h2>SYNVISIO</h2>
              </div>
              <div>
                <iframe :src=url style="width: 100%; height: 1500px;"></iframe>
              </div>
            </div>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      url:"http://synvisio.insect-genome.com/#/mc-bv"
    }
  },
  props: {
    dataBackgroundColor: {
      type: String,
      default: "",
    },
  },
};
</script>

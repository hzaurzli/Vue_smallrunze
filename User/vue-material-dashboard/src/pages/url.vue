<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item">
        <md-card class="md-card-plain">
          <md-card-header data-background-color="green">
            <h4 class="title">Material Design Icons</h4>
            <p class="category">
              Handcrafted by our friends from
              <a target="_blank" href="https://design.google.com/icons/"
                >Google</a
              >
            </p>
          </md-card-header>
          <md-card-content>
            <iframe :src=src style="width: 100%; height: 1500px;"></iframe>
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
          src:""
        }
      },
      mounted() {
        this.src = this.$route.query.id;
        console.log(this.$route.query)
      }
    };
</script>
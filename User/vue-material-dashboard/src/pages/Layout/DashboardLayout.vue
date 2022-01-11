<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <notifications></notifications>

    <side-bar
      :sidebar-item-color="sidebarBackground"
      :sidebar-background-image="sidebarBackgroundImage"
    >
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/dashboard">
        <md-icon></md-icon>
        <p style="font-size: 25px">Dashboard</p>
      </sidebar-link>
      <sidebar-link to="/user">
        <md-icon></md-icon>
        <p style="font-size: 25px">User Profile</p>
      </sidebar-link>
      <sidebar-link to="/table">
        <md-icon></md-icon>
        <p style="font-size: 25px">Table list</p>
      </sidebar-link>
      <sidebar-link to="/typography">
        <md-icon></md-icon>
        <p style="font-size: 25px">Synvisio</p>
      </sidebar-link>
      <sidebar-link to="/icons">
        <md-icon></md-icon>
        <p style="font-size: 25px">Icons</p>
      </sidebar-link>
      <sidebar-link to="/maps">
        <md-icon></md-icon>
        <p style="font-size: 25px">Maps</p>
      </sidebar-link>
      <sidebar-link to="/notifications">
        <md-icon></md-icon>
        <p style="font-size: 25px">Data table</p>
      </sidebar-link>
      <sidebar-link to="/upgrade" class="active-pro">
        <md-icon></md-icon>
        <p>Upgrade to PRO</p>
      </sidebar-link>
    </side-bar>

    <div class="main-panel">
      <top-navbar></top-navbar>

      <fixed-plugin
        :color.sync="sidebarBackground"
        :image.sync="sidebarBackgroundImage"
      >
      </fixed-plugin>

      <dashboard-content> </dashboard-content>

      <content-footer v-if="!$route.meta.hideFooter"></content-footer>
    </div>
  </div>
</template>

<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "@/pages/Layout/MobileMenu.vue";
import FixedPlugin from "./Extra/FixedPlugin.vue";

export default {
  components: {
    TopNavbar,
    DashboardContent,
    ContentFooter,
    MobileMenu,
    FixedPlugin,
  },
  data() {
    return {
      sidebarBackground: "green",
      sidebarBackgroundImage: require("@/assets/img/sidebar-2.jpg"),
    };
  },
};
</script>

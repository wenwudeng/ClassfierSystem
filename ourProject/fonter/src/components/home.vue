<template>
  <!-- <router-link to="/test">路由测试</router-link> -->
  <el-container>
    <!-- 左侧导航栏 -->
    <!-- <el-container style="background-color: rgb(244, 245, 245);"> -->
    <el-aside>
      <el-menu
        :default-active="active"
        class="el-menu-vertical-demo siderbar-style"
        @select="handleSelect"
        :collapse="isCollapse"
        background-color="white"
        text-color="#000"
        active-text-color="rgb(18,175,227)"
        style="height:794px"
      >
        <el-menu-item index="0">
          <i class="el-icon-s-home"></i>
          <span slot="title">主页</span>
        </el-menu-item>
        <el-menu-item index="1" v-if="this.role=='admin' || this.role=='reptile'">
          <i class="el-icon-s-marketing"></i>
          <span slot="title">爬虫功能</span>
        </el-menu-item>
        <el-menu-item index="2" v-if="this.role=='admin' || this.role=='data'">
          <i class="el-icon-s-data"></i>
          <span slot="title">数据标注</span>
        </el-menu-item>
        <el-menu-item index="3" v-if="this.role=='admin' || this.role=='classify'">
          <i class="el-icon-document"></i>
          <span slot="title">分类功能</span>
        </el-menu-item>
        <el-menu-item index="4" v-if="this.role=='admin' || this.role=='algorithm'">
          <i class="el-icon-cpu"></i>
          <span slot="title">算法展示</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <!-- </el-container> -->

    <el-container :class="mainstyle">
      <!-- 顶部导航栏 -->
      <el-header style="background-color: rgb(244, 245, 245); height:56px">
        <el-menu
          class="el-menu-demo navbar-style"
          mode="horizontal"
          background-color="rgb(18,175,227)"
          text-color="#fff"
          active-text-color="#ffd04b"
          style="margin: 0px -20px 0px -20px !important;height:56px;"
        >
          <el-menu-item @click="collapse" style="height:56px;">
            <div style="width:24px;height:56px;">
              <img src="@/assets/collapse.png" style="width:20px;height:20px;margin-top:-5px;" />
              <!-- <i class="el-icon-s-operation" ></i> -->
            </div>
          </el-menu-item>
          <el-dropdown class="avatar-container" @command="handleCommand" trigger="click">
            <div class="user-container" style="margin-top:5px;">
              <img class="user-avatar" src="@/assets/logo.png" />
              <i class="el-icon-arrow-down user-icon"></i>
            </div>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="0">主页</el-dropdown-item>
              <el-dropdown-item command="-1">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-menu>
      </el-header>
      <el-main>
        <Main v-if="this.active == 0"></Main>
        <Reptile v-if="this.active == 1"></Reptile>
        <DataAnnotation v-if="this.active == 2"></DataAnnotation>
        <Classify v-if="this.active == 3"></Classify>
        <Algorithm v-if="this.active == 4"></Algorithm>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Main from "@/components/page/Main";
import Reptile from "@/components/page/Reptile";
import DataAnnotation from "@/components/page/DataAnnotation";
import Classify from "@/components/page/Classify";
import Algorithm from "@/components/page/Algorithm";

export default {
  components: {
    Main,
    Reptile,
    DataAnnotation,
    Classify,
    Algorithm
  },
  data() {
    return {
      isCollapse: false,
      mainstyle: "mainstyle1",
      active: "0",
      role: ""
    };
  },
  created() {
    this.role = this.$route.query.role;
  },
  methods: {
    collapse() {
      this.isCollapse = !this.isCollapse;
      if (this.isCollapse == true) {
        this.mainstyle = "mainstyle2";
      } else {
        this.mainstyle = "mainstyle1";
      }
    },
    handleSelect(key, keyPath) {
      this.active = key;
      console.log(key);
      console.log(keyPath);
    },
    handleCommand(command) {
      if (command == 0) {
        this.active = command;
      } else {
        // 退出登录
        this.$router.push({
          path: "/login"
        });
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.avatar-container {
  cursor: pointer;
  float: right;
}
.user-container {
  margin: 9px 15px 0px 0px;
}
.user-icon {
  color: #cccccc;
}
.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 10px;
}
.mainstyle1 {
  margin-left: -100px;
  transition-property: margin-left;
  transition-duration: 0.3s;
  transition-timing-function: linear;
  background-color: rgb(236, 240, 245);
}
.mainstyle2 {
  margin-left: -236px;
  transition-property: margin-left;
  transition-duration: 0.3s;
  transition-timing-function: linear;
  background-color: rgb(236, 240, 245);
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.el-menu-item:hover {
  background-color: rgb(236, 245, 255) !important;
}
</style>

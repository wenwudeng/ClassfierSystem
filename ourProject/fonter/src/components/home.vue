<template>
  <!-- <router-link to="/test">路由测试</router-link> -->
  <el-container>
    <!-- 顶部导航栏 -->
    <el-header>
      <el-menu
        class="el-menu-demo navbar-style"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        style="margin: 0px -20px 0px -20px !important"
      >
        <el-menu-item @click="collapse">
          <div style="width:24px">
            <i class="el-icon-s-operation"></i>
          </div>
        </el-menu-item>
        <!-- <el-menu-item index="1">选项1</el-menu-item>
      <el-menu-item index="2">选项2</el-menu-item>
      <el-menu-item index="3">选项3</el-menu-item>
        <el-menu-item index="4">选项4</el-menu-item>-->

        <div>
          <img class="user-avatar" src="@/assets/user.png" />
        </div>
      </el-menu>
    </el-header>

    <!-- 左侧导航栏 -->
    <el-container>
      <el-aside>
        <el-menu
          :default-active="active"
          class="el-menu-vertical-demo siderbar-style"
          @select="handleSelect"
          :collapse="isCollapse"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          style="height:734px"
        >
          <el-menu-item index="0">
            <i class="el-icon-menu"></i>
            <span slot="title">主页</span>
          </el-menu-item>
          <el-menu-item index="1">
            <i class="el-icon-menu"></i>
            <span slot="title">爬虫功能</span>
          </el-menu-item>
          <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span slot="title">数据标注</span>
          </el-menu-item>
          <el-menu-item index="3">
            <i class="el-icon-document"></i>
            <span slot="title">分类功能</span>
          </el-menu-item>
          <el-menu-item index="4">
            <i class="el-icon-setting"></i>
            <span slot="title">算法展示</span>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <el-main :class="mainstyle">
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
      active: "0"
    };
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
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.mainstyle1 {
  margin-left: -95px;
  transition: margin-left 0.5s;
}
.mainstyle2 {
  margin-left: -230px;
  transition: margin-left 0.5s;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  float: right;
  margin: 9px 20px 0px 0px;
}
</style>

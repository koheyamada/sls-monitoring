import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import cognito from '@/cognito'
import MemoList from '@/components/MemoList'
import UserList from '@/components/UserList'
import Registration from '@/components/Registration'
import CheckResults from '@/components/CheckResults'
import Codes from '@/components/Codes'
import Graph from '@/components/Graph'
import Login from '@/components/Login'
import Signup from '@/components/Signup'
import Confirm from '@/components/Confirm'
import Sandbox from '@/components/sandbox'

Vue.use(Router)

const requireAuth = (to, from, next) => {
  cognito.isAuthenticated()
    .then(session => {
      next()
    })
    .catch(session => {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    })
}

const logout = (to, from, next) => {
  cognito.logout()
  next('/login')
}

export default new Router({
  routes: [
    {
      path: '/',
      redirect: 'home'
    },
    {
      path: '/home',
      name: 'HelloWorld',
      component: HelloWorld,
      beforeEnter: requireAuth
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {
        title: 'Login'
      }
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup,
      meta: {
        title: 'Signup'
      }
    },
    {
      path: '/confirm',
      name: 'Confirm',
      component: Confirm,
      meta: {
        title: 'Confirm'
      }
    },
    {
      path: '/confirm',
      beforeEnter: logout
    },
    {
      path: '/memo',
      name: 'MemoList',
      component: MemoList,
      meta: {
        title: 'memo list'
      }
    },
    {
      path: '/user',
      name: 'UserList',
      component: UserList,
      meta: {
        title: 'user list'
      }
    },
    {
      path: '/registration',
      name: 'UserRegist',
      component: Registration,
      meta: {
        title: 'user regist'
      }
    },
    {
      path: '/checkresults',
      name: 'CheckResults',
      component: CheckResults,
      meta: {
        title: 'Check Results'
      }
    },
    {
      path: '/codes',
      name: 'Codes',
      component: Codes,
      meta: {
        title: 'Codes'
      }
    },
    {
      path: '/graph',
      name: 'Graph',
      component: Graph,
      meta: {
        title: 'Graph'
      }
    },
    {
      path: '/sandbox',
      name: 'Sandbox',
      component: Sandbox,
      meta: {
        title: 'Sandbox'
      }
    }
  ]
})

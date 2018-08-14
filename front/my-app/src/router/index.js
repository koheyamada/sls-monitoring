import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import MemoList from '@/components/MemoList'
import UserList from '@/components/UserList'
import Registration from '@/components/Registration'
import CheckResults from '@/components/CheckResults'
import Codes from '@/components/Codes'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld,
      meta: {
        title: 'hello world'
      }
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
    }
  ]
})

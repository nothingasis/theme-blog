(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d22d207"],{f5bd:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",{attrs:{"grid-list-xl":""}},[a("v-layout",{attrs:{wrap:""}},[a("v-flex",{attrs:{xs12:""}},[t._t("default")],2),t._l(t.paginatedArticles,function(e,n){return a("feed-card",{key:e.title+n,attrs:{size:t.layout[n],value:e}})})],2),a("v-layout",{attrs:{"align-center":""}},[a("v-flex",{attrs:{xs3:""}},[1!==t.page?a("base-btn",{staticClass:"ml-0",attrs:{title:"Previous page",square:""},on:{click:function(e){t.page--}}},[a("v-icon",[t._v("mdi-chevron-left")])],1):t._e()],1),a("v-flex",{attrs:{xs6:"","text-xs-center":"",subheading:""}},[t._v("\n      PAGE "+t._s(t.page)+" OF "+t._s(t.pages)+"\n    ")]),a("v-flex",{attrs:{xs3:"","text-xs-right":""}},[t.pages>1&&t.page<t.pages?a("base-btn",{staticClass:"mr-0",attrs:{title:"Next page",square:""},on:{click:function(e){t.page++}}},[a("v-icon",[t._v("mdi-chevron-right")])],1):t._e()],1)],1)],1)},s=[],r=a("cebc"),i=a("2f62"),c={name:"Feed",components:{FeedCard:function(){return a.e("chunk-0a78824a").then(a.bind(null,"eb3a"))}},data:function(){return{layout:[2,2,1,2,2,3,3,3,3,3,3],page:1}},computed:Object(r["a"])({},Object(i["e"])(["articles"]),{pages:function(){return Math.ceil(this.articles.length/11)},paginatedArticles:function(){var t=11*(this.page-1),e=11*this.page;return this.articles.slice(t,e)}}),watch:{page:function(){window.scrollTo(0,0)}}},l=c,u=a("2877"),o=a("6544"),p=a.n(o),d=a("a523"),g=a("0e8f"),f=a("132d"),v=a("a722"),h=Object(u["a"])(l,n,s,!1,null,null,null);e["default"]=h.exports;p()(h,{VContainer:d["a"],VFlex:g["a"],VIcon:f["a"],VLayout:v["a"]})}}]);
//# sourceMappingURL=chunk-2d22d207.7d16890f.js.map
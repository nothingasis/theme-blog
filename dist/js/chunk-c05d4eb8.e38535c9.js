(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-c05d4eb8"],{"132d":function(t,e,n){"use strict";n("44dc");var a,s=n("b64a"),r=n("2b0e"),i=r["a"].extend({name:"sizeable",props:{large:Boolean,medium:Boolean,size:{type:[Number,String]},small:Boolean,xLarge:Boolean}}),o=n("6a18"),l=n("80d2"),c=n("58df"),d=Object.assign||function(t){for(var e=1;e<arguments.length;e++){var n=arguments[e];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(t[a]=n[a])}return t};function u(t){return["fas","far","fal","fab"].some(function(e){return t.includes(e)})}(function(t){t["small"]="16px",t["default"]="24px",t["medium"]="28px",t["large"]="36px",t["xLarge"]="40px"})(a||(a={}));var h=Object(c["a"])(s["a"],i,o["a"]).extend({name:"v-icon",props:{disabled:Boolean,left:Boolean,right:Boolean},methods:{getIcon:function(){var t="";return this.$slots.default&&(t=this.$slots.default[0].text.trim()),Object(l["k"])(this,t)},getSize:function(){var t={small:this.small,medium:this.medium,large:this.large,xLarge:this.xLarge},e=Object(l["j"])(t).find(function(e){return t[e]});return e&&a[e]||Object(l["a"])(this.size)},getDefaultData:function(){var t={staticClass:"v-icon",class:{"v-icon--disabled":this.disabled,"v-icon--left":this.left,"v-icon--link":this.$listeners.click||this.$listeners["!click"],"v-icon--right":this.right},attrs:d({"aria-hidden":!0},this.$attrs),on:this.$listeners};return t},applyColors:function(t){t.class=d({},t.class,this.themeClasses),this.setTextColor(this.color,t)},renderFontIcon:function(t,e){var n=[],a=this.getDefaultData(),s="material-icons",r=t.indexOf("-"),i=r<=-1;i?n.push(t):(s=t.slice(0,r),u(s)&&(s="")),a.class[s]=!0,a.class[t]=!i;var o=this.getSize();return o&&(a.style={fontSize:o}),this.applyColors(a),e("i",a,n)},renderSvgIcon:function(t,e){var n=this.getDefaultData();n.class["v-icon--is-component"]=!0;var a=this.getSize();a&&(n.style={fontSize:a,height:a}),this.applyColors(n);var s=t.component;return n.props=t.props,n.nativeOn=n.on,e(s,n)}},render:function(t){var e=this.getIcon();return"string"===typeof e?this.renderFontIcon(e,t):this.renderSvgIcon(e,t)}});e["a"]=r["a"].extend({name:"v-icon",$_wrapperFor:h,functional:!0,render:function(t,e){var n=e.data,a=e.children,s="";return n.domProps&&(s=n.domProps.textContent||n.domProps.innerHTML||s,delete n.domProps.textContent,delete n.domProps.innerHTML),t(h,n,s?[s]:a)}})},"40cf":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("base-card",{attrs:{dark:""}},[a("v-img",{staticClass:"grey lighten-2",attrs:{height:"400",width:"100%",src:n("4c4a")}},[a("v-layout",{attrs:{"fill-height":"","align-center":"","pa-3":""}},[a("v-flex",{attrs:{xs12:"",md7:"","offset-md5":""}},[a("h1",{staticClass:"display-3 font-weight-light"},[t._v("\n          Roah Cosmetics & Lashes\n        ")]),a("div",{staticClass:"subheading text-uppercase pl-2 mb-4"},[a("v-icon",{attrs:{dark:""}},[t._v("\n            mdi-map-marker\n          ")]),t._v("\n          4562 MACK ROAD, SACRAMENTO CA 95823\n        ")],1),a("v-btn",{attrs:{color:"primary",depressed:"",round:""},on:{click:function(e){return t.$vuetify.goTo("#subscribe")}}},[t._v("\n          Subscribe\n        ")])],1)],1)],1)],1)},s=[],r=n("2877"),i=n("6544"),o=n.n(i),l=n("8336"),c=n("0e8f"),d=n("132d"),u=n("adda"),h=n("a722"),f={},p=Object(r["a"])(f,a,s,!1,null,null,null);e["default"]=p.exports;o()(p,{VBtn:l["a"],VFlex:c["a"],VIcon:d["a"],VImg:u["a"],VLayout:h["a"]})},"44dc":function(t,e,n){},"4c4a":function(t,e,n){t.exports=n.p+"img/banner.4fdefabe.jpg"}}]);
//# sourceMappingURL=chunk-c05d4eb8.e38535c9.js.map
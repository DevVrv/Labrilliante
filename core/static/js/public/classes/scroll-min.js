"use strict";class ScrollFix{constructor(o){this.container=this.getElement(o.container),this.extensionBottom=o.extensionBottom,this.extensionTop=o.extensionTop,this.debug=o.debug,this.create()}create(){!0===this.debug&&this.debuger(),this.scroll()}debuger(o=this){}getElement(o,t=document){let e=t.querySelectorAll(o);return 1===e.length&&(e=e[0]),e}scroll(){this.container.scrollTo(0,4),this.container.addEventListener("scroll",(()=>{this.scrollHeight=this.container.scrollHeight,this.scrollTop=this.container.scrollTop,this.scrollBottom=this.container.scrollHeight-this.container.scrollTop-this.container.clientHeight,this.scrollBottom<4&&(this.container.scrollTo({top:this.scrollTop-5,behavior:"smooth"}),void 0!==this.extensionBottom&&this.extensionBottom()),this.scrollTop<4&&(this.container.scrollTo({top:5,behavior:"smooth"}),void 0!==this.extensionTop&&this.extensionTop())}))}}function windowScrollFix(){window.scrollTo({top:5,behavior:"smooth"}),window.addEventListener("scroll",(()=>{let o=document.documentElement.scrollTop;document.documentElement.scrollHeight-document.documentElement.scrollTop-document.documentElement.clientHeight<4&&window.scrollTo({top:o-5,behavior:"smooth"}),o<4&&window.scrollTo({top:5,behavior:"smooth"})}))}windowScrollFix();
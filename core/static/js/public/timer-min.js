"use strict";function timer(e,t,n,r=60){const o=`\n        <div class="login__info w-100 d-flex align-items-center justify-content-between py-3">\n            <span>Didn't get the code ?</span>\n            <a href="${n}" class="btn btn-secondary" id="resend_mail_code">Send the code again</a>\n        </div>\n    `,a=document.querySelector(e);let l=null;void 0!==a&&(l=a.querySelector(t));const i=Number(Date.now());if(null===localStorage.getItem("timer")&&localStorage.setItem("timer",i),null!==l){setInterval((function(){const e=Number(Date.now()),t=Number(localStorage.getItem("timer"));let n=Math.floor(e/1e3-t/1e3);n>=r?(localStorage.clear(),l.parentElement.remove(),a.innerHTML=o):l.textContent=r-n}),1e3)}}timer("#resend_timer_container","#resend_timer","/user/confirm/again/");
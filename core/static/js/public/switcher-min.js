"use strict";function switcher(e){const t=[...document.querySelectorAll(e)];t[0].checked=!0,t[0].parentElement.classList.add("active"),t.map(((e,c)=>{e.addEventListener("input",(()=>{t.map((e=>{e.checked=!1,e.parentElement.classList.remove("active")})),e.checked=!0,e.parentElement.classList.add("active")}))}))}switcher(".switcher > div > label > input");
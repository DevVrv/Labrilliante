"use strict";function inDev(e,t){let c="active";const i=document.querySelectorAll(e),n=document.querySelector(t);i.forEach((e=>{e.addEventListener("click",(e=>{e.preventDefault,n.classList.add(c);setTimeout((()=>{n.classList.remove(c)}),2e3)}))}))}inDev(".in-dev-toggler","#in-dev");
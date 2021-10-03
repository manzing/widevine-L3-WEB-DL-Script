/* eslint-env browser */

// ==UserScript==
// @name         Amazon EAC3 Enabler
// @namespace    nobody@nowhere.com
// @version      0.1
// @description  Enable EAC3 streams for Amazon Video
// @author       nobody
// @match        https://www.amazon.com/*
// @match        https://www.amazon.co.uk/*
// @match        https://www.amazon.de/*
// @match        https://www.amazon.co.jp/*
// @match        https://www.primevideo.com/*
// @grant        none
// ==/UserScript==

(function () {
  'use strict';
  (function (open) {
    XMLHttpRequest.prototype.open = function () {
      arguments[1] = arguments[1].replace('~', '')
      open.apply(this, arguments)
    }
  })(XMLHttpRequest.prototype.open)
})()
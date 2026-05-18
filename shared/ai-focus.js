/* ai-focus.js — 「この章の焦点」を cover の data-label から動的に注入する。
   章の内容が変われば data-label が変わり、焦点表示も自動で追従する。 */
(function () {
  var cover = document.querySelector('section[data-label]');
  if (!cover) return;
  var label = cover.getAttribute('data-label') || '';
  var dash = label.indexOf('—');
  var focus = (dash >= 0 ? label.slice(dash + 1) : label).trim();
  if (!focus) return;
  document.querySelectorAll('.ai-focus-value').forEach(function (el) {
    el.textContent = focus;
  });
})();

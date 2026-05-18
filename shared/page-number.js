/* page-number.js — meta-line のページ番号を section 数から自動採番する。
   ベタ書きの "NN / MM" は fallback。スライドを増減しても番号が drift しない。 */
(function () {
  var sections = document.querySelectorAll('section');
  var total = sections.length;
  var pad = function (n) { return String(n).padStart(2, '0'); };
  sections.forEach(function (section, i) {
    var span = section.querySelector('.meta-line > span:last-child');
    if (span && /^\s*\d+\s*\/\s*\d+\s*$/.test(span.textContent)) {
      span.textContent = pad(i + 1) + ' / ' + pad(total);
    }
  });
})();

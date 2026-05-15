/* ============================================================
 * progress-strip.js
 * 各 <section> に「全スライド中の現在位置」を示す横長インジケータを注入する。
 * 仕様：
 *   - 各 section 末尾に <div class="progress-strip"> を追加
 *   - 全スライド分の dot + 短縮ラベルを並べる
 *   - 自スライドに `.active` を付与
 *   - data-label の "—" や "－" の前を短縮ラベルとして使う
 *
 * theme.css の `.progress-strip` / `.ps-step` / `.ps-dot` / `.ps-label` で装飾。
 * deck-stage.js の後に読み込むこと。
 * ============================================================ */
(function () {
  function shorten(label) {
    if (!label) return '';
    // "Cover — なぜ今、Claude Code を学ぶのか" → "Cover"
    // 「—」「-」「ー」などの区切りで前を取る
    var first = label.split(/[—\-－]+/)[0].trim();
    if (first.length > 12) first = first.slice(0, 11) + '…';
    return first;
  }

  function inject() {
    var sections = document.querySelectorAll('deck-stage > section');
    if (!sections.length) return;

    sections.forEach(function (section, idx) {
      // 既に注入済みならスキップ（再呼び出し対策）
      if (section.querySelector(':scope > .progress-strip')) return;

      var strip = document.createElement('div');
      strip.className = 'progress-strip';

      sections.forEach(function (s, i) {
        var step = document.createElement('div');
        // data-kind="main" のスライド（各章本題）はクレイ色で強調する
        step.className = 'ps-step'
          + (i === idx ? ' active' : '')
          + (s.dataset.kind === 'main' ? ' main' : '');

        var dot = document.createElement('div');
        dot.className = 'ps-dot';
        step.appendChild(dot);

        var labelEl = document.createElement('div');
        labelEl.className = 'ps-label';
        var num = String(i + 1).padStart(2, '0');
        labelEl.textContent = num + ' ' + shorten(s.dataset.label || '');
        step.appendChild(labelEl);

        strip.appendChild(step);
      });

      section.appendChild(strip);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inject);
  } else {
    inject();
  }
})();

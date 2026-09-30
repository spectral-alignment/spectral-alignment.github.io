'use strict';
const progress = document.querySelector('.progress');
const sections = [...document.querySelectorAll('article section[id]')];
const links = [...document.querySelectorAll('.toc a[href^="#"]')];
let scheduled = false;
function updateReading() {
  const max = document.documentElement.scrollHeight - innerHeight;
  progress.style.width = (max > 0 ? Math.min(100, scrollY / max * 100) : 0) + '%';
  let active = 'overview';
  for (const section of sections) if (section.getBoundingClientRect().top < innerHeight * .32) active = section.id;
  links.forEach(link => { const selected = link.hash === '#' + active; link.classList.toggle('active', selected); if (selected) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); });
  scheduled = false;
}
addEventListener('scroll', () => { if (!scheduled) { scheduled = true; requestAnimationFrame(updateReading); } }, {passive:true});
addEventListener('resize', updateReading);
updateReading();
const slider = document.getElementById('bandwidth');
const canvas = document.getElementById('kernel-canvas');
function drawKernel() {
  if (!canvas || !slider) return;
  const ctx = canvas.getContext('2d');
  const sigma = Number(slider.value), n = 23, cell = 18, start = 33;
  ctx.clearRect(0,0,460,460);
  for (let i=0;i<n;i++) for (let j=0;j<n;j++) {
    const v=Math.exp(-Math.abs(i-j)/sigma);
    ctx.fillStyle=`rgb(${Math.round(242-205*v)},${Math.round(246-173*v)},${Math.round(251-133*v)})`;
    ctx.fillRect(start+j*cell,start+i*cell,cell+.2,cell+.2);
  }
  ctx.fillStyle='#626b76';ctx.font='14px -apple-system, sans-serif';ctx.textAlign='center';
  [0,11,22].forEach(i=>{ctx.fillText(String(i),start+i*cell+cell/2,22);ctx.fillText(String(i),16,start+i*cell+cell/2+5);});
  document.getElementById('sigma-value').textContent=String(sigma);
  document.getElementById('kernel-description').textContent=`At 7 frames apart, similarity is ${Math.exp(-7/sigma).toFixed(2)}. ${sigma<5?'A narrow band emphasizes nearby observations.':sigma>12?'A wide band keeps distant observations more similar.':'A wider band preserves similarity across longer separations.'}`;
  canvas.setAttribute('aria-label',`Temporal similarity matrix for 23 observations with bandwidth ${sigma}. Similarity at a separation of 7 frames is ${Math.exp(-7/sigma).toFixed(2)}.`);
}
slider?.addEventListener('input',drawKernel);drawKernel();
// Shuffle the equal-contribution pair only; keep the other authors in paper order.
const equalAuthors = document.getElementById('equal-author-names');
if (equalAuthors && Math.random() < .5) equalAuthors.prepend(equalAuthors.lastElementChild);
for (const element of document.querySelectorAll('.math-tex')) {
  katex.render(element.textContent, element, {displayMode:element.dataset.display==='true',throwOnError:true,trust:false,output:'htmlAndMathml'});
}
const dialog = document.getElementById('figure-dialog');
const expanded = document.getElementById('expanded-figure');
let previousOverflow = '';
for (const link of document.querySelectorAll('[data-zoom]')) {
  link.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || !dialog.showModal) return;
    event.preventDefault();
    expanded.alt = link.querySelector('img').alt;
    expanded.src = link.dataset.zoom;
    dialog.setAttribute('aria-label', link.dataset.title + '. Press Escape or click to close.');
    previousOverflow = document.documentElement.style.overflow;
    document.documentElement.style.overflow = 'hidden';
    dialog.showModal();
  });
}
dialog.addEventListener('click', () => dialog.close());
dialog.addEventListener('close', () => {
  document.documentElement.style.overflow = previousOverflow;
});

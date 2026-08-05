function hdr() { return {"X-User": document.getElementById("user").value || "labuser", "Content-Type": "application/json"}; }
function env() { return document.getElementById("env").value; }
async function getJson(url) { const r = await fetch(url, {headers: hdr()}); if (!r.ok) throw new Error(await r.text()); return r.json(); }
async function postJson(url, body) { const r = await fetch(url, {method: "POST", headers: hdr(), body: JSON.stringify(body)}); if (!r.ok) throw new Error(await r.text()); return r.json(); }
function table(items) {
  if (!items || !items.length) return "<em>Nenhum item encontrado</em>";
  const keys = Object.keys(items[0]);
  return `<table><thead><tr>${keys.map(k=>`<th>${k}</th>`).join("")}</tr></thead><tbody>` + items.map(row=>`<tr>${keys.map(k=>`<td>${row[k]??""}</td>`).join("")}</tr>`).join("") + "</tbody></table>";
}
function setRaw(id, data) { document.getElementById(id).innerHTML = data.items ? table(data.items) : `<pre>${data.raw}</pre>`; }
async function loadEnvs() {
  const data = await getJson('/api/environments');
  const sel = document.getElementById('env');
  sel.innerHTML = data.environments.map(e=>`<option>${e}</option>`).join('');
}
async function refreshAll() {
  try {
    const [mon, subs, dss] = await Promise.all([getJson(`/api/${env()}/monitor`), getJson(`/api/${env()}/subscriptions`), getJson(`/api/${env()}/datastores`)]);
    setRaw('monitor', mon); setRaw('subscriptions', subs); setRaw('datastores', dss);
    const running = (mon.items || []).filter(x => (x.state || '').toLowerCase().includes('mirror')).length;
    const inactive = (mon.items || []).filter(x => (x.state || '').toLowerCase().includes('inactive')).length;
    document.getElementById('cards').innerHTML = `<div class="card"><div>Subscriptions</div><div class="value">${(mon.items || []).length}</div></div><div class="card"><div>Running</div><div class="value ok">${running}</div></div><div class="card"><div>Inactive</div><div class="value warn">${inactive}</div></div><div class="card"><div>Datastores</div><div class="value">${(dss.items || []).length}</div></div>`;
  } catch (e) { alert(e.message); }
}
async function loadDetails() {
  const sub = document.getElementById('subname').value;
  const data = await getJson(`/api/${env()}/subscription/${encodeURIComponent(sub)}`);
  document.getElementById('details').textContent = data.raw;
}
async function loadEvents(side) {
  const sub = document.getElementById('subname').value;
  const data = await getJson(`/api/${env()}/subscription/${encodeURIComponent(sub)}/events/${side}?count=100`);
  document.getElementById('details').innerHTML = table(data.items) + `
<pre>${data.raw}</pre>`;
}
async function startMirroring() {
  const sub = document.getElementById('opsub').value;
  if (!confirm(`Iniciar mirroring para ${sub}?`)) return;
  const data = await postJson('/api/actions/start', {environment: env(), subscription: sub});
  document.getElementById('operation').textContent = data.raw;
  await refreshAll();
}
async function stopMirroring() {
  const sub = document.getElementById('opsub').value;
  if (!confirm(`Encerrar replication para ${sub}?`)) return;
  const data = await postJson('/api/actions/stop', {environment: env(), subscription: sub, method: 'normal'});
  document.getElementById('operation').textContent = data.raw;
  await refreshAll();
}
loadEnvs().then(refreshAll).catch(e => alert(e.message));

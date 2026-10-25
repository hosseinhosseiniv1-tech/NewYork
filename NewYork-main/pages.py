# pages.py - Lumen Gate v11
# Contains: LOGIN_HTML, DASHBOARD_HTML, NOT_FOUND_HTML and get_public_page_html().
# The UI is a self-contained design system (CSS custom properties, dark + light themes).
# Markup IDs, inline handlers and API calls are unchanged from the previous version.

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="dark light">
<title>Sign in · Lumen Gate</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%2032%2032%22%3E%3Cdefs%3E%3ClinearGradient%20id%3D%22g%22%20x1%3D%220%22%20y1%3D%220%22%20x2%3D%221%22%20y2%3D%221%22%3E%3Cstop%20offset%3D%220%22%20stop-color%3D%22%232dd4bf%22/%3E%3Cstop%20offset%3D%221%22%20stop-color%3D%22%232563c9%22/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect%20width%3D%2232%22%20height%3D%2232%22%20rx%3D%229%22%20fill%3D%22url%28%23g%29%22/%3E%3Cpath%20d%3D%22M6%2017h5l3-8%204%2014%203-6h5%22%20fill%3D%22none%22%20stroke%3D%22%2304201c%22%20stroke-width%3D%222.6%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22/%3E%3C/svg%3E">
<script>try{document.documentElement.setAttribute('data-theme',localStorage.getItem('gateway-theme')==='light'?'light':'dark')}catch(e){}</script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{color-scheme:dark;--bg:#080f17;--card:#0f1923;--bg3:#15212d;--bd:#233443;--t1:#e8eff5;--t2:#9db0c0;--t3:#6b8093;--accent:#2dd4bf;--accent2:#5eead4;--accent-d:rgba(45,212,191,.12);--on-accent:#04201c;--purple:#7aa7f5;--red:#f87171;--red-bg:rgba(248,113,113,.12);--field:rgba(0,0,0,.22);--ring:0 0 0 3px rgba(45,212,191,.32);--shadow:0 28px 70px -14px rgba(0,0,0,.8);--font:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace}
[data-theme="light"]{color-scheme:light;--bg:#f2f5f7;--card:#ffffff;--bg3:#e9eef2;--bd:#dbe2e9;--t1:#0b1620;--t2:#4b5b6a;--t3:#7a8896;--accent:#0b8f84;--accent2:#097a71;--accent-d:#dcf3f0;--on-accent:#ffffff;--purple:#2563c9;--red:#b92f2f;--red-bg:#fbe3e3;--field:#f6f8fa;--ring:0 0 0 3px rgba(11,143,132,.3);--shadow:0 28px 70px -14px rgba(11,22,32,.3)}
html,body{min-height:100%}
body{font-family:var(--font);background:radial-gradient(60% 45% at 50% -5%,var(--accent-d),transparent 70%),var(--bg);color:var(--t1);display:grid;place-items:center;padding:calc(20px + env(safe-area-inset-top,0px)) 20px calc(20px + env(safe-area-inset-bottom,0px));font-size:14px;line-height:1.5;-webkit-font-smoothing:antialiased}
button,input{font:inherit;color:inherit}
:focus-visible{outline:none;box-shadow:var(--ring)}
.wrap{width:100%;max-width:400px}
.card{background:var(--card);border:1px solid var(--bd);border-radius:22px;padding:34px 30px 30px;box-shadow:var(--shadow);animation:rise .4s cubic-bezier(.2,.8,.2,1)}
@keyframes rise{from{opacity:0;transform:translateY(10px)}}
.brand{display:flex;align-items:center;gap:12px;margin-bottom:26px}
.brand-img svg{width:40px;height:40px;display:block}
.brand-name{font-size:16px;font-weight:650;letter-spacing:-.01em}
.brand-sub{font-size:12px;color:var(--t3)}
h1{font-size:26px;font-weight:700;letter-spacing:-.03em;line-height:1.15}
.sub{color:var(--t2);margin:8px 0 22px}
.err{display:none;align-items:center;gap:8px;padding:10px 12px;margin-bottom:14px;border-radius:12px;background:var(--red-bg);color:var(--red);font-size:13px}
.err.show{display:flex}
.hint{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:10px 12px;margin-bottom:18px;border:1px dashed var(--bd);border-radius:12px;font-size:12.5px;color:var(--t3)}
.hint-val{font-family:var(--mono);color:var(--accent2);background:var(--accent-d);padding:2px 10px;border-radius:99px;cursor:pointer}
.field{display:flex;flex-direction:column;gap:6px;margin-bottom:16px}
.field label{font-size:13px;font-weight:600;color:var(--t2)}
.inp-wrap{position:relative}
.inp-wrap input{width:100%;height:44px;padding:0 44px;border-radius:12px;border:1px solid var(--bd);background:var(--field);font-size:15px;outline:none;transition:border-color .15s,box-shadow .15s}
.inp-wrap input:focus{border-color:var(--accent);box-shadow:var(--ring)}
.inp-wrap .ic{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:17px;pointer-events:none}
.eye{position:absolute;right:8px;top:50%;transform:translateY(-50%);width:32px;height:32px;display:flex;align-items:center;justify-content:center;background:none;border:0;border-radius:8px;color:var(--t3);font-size:17px;cursor:pointer}
.eye:hover{color:var(--t1);background:var(--bg3)}
.btn{width:100%;height:46px;display:flex;align-items:center;justify-content:center;gap:8px;border:0;border-radius:12px;background:var(--accent);color:var(--on-accent);font-size:15px;font-weight:650;cursor:pointer;transition:filter .15s,transform .12s}
.btn:hover{filter:brightness(1.1)}.btn:active{transform:scale(.98)}.btn:disabled{opacity:.6;cursor:wait}
@keyframes spin{to{transform:rotate(360deg)}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
</head>
<body>
<main class="wrap">
  <div class="card">
    <div class="brand">
      <div class="brand-img"><svg viewBox="0 0 32 32" role="img" aria-label="Lumen Gate"><defs><linearGradient id="lgL" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--accent)"/><stop offset="1" style="stop-color:var(--purple)"/></linearGradient></defs><rect width="32" height="32" rx="9" fill="url(#lgL)"/><path d="M6 17h5l3-8 4 14 3-6h5" fill="none" stroke="var(--on-accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div><div class="brand-name">Lumen Gate</div><div class="brand-sub">v11</div></div>
    </div>
    <h1>Sign in</h1>
    <p class="sub">Enter your password to access the dashboard.</p>
    <div class="err" id="err" role="alert"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint">
      <span class="hint-label">Default password</span>
      <span class="hint-val" role="button" tabindex="0" onclick="document.getElementById('pw').value='admin';document.getElementById('pw').focus()">admin</span>
    </div>
    <form id="form">
      <div class="field">
        <label for="pw">Password</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="Enter your password" autocomplete="current-password" autofocus required>
          <i class="ti ti-lock ic" aria-hidden="true"></i>
          <button type="button" class="eye" id="pw-eye" aria-label="Show password"><i class="ti ti-eye"></i></button>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> Open dashboard</button>
    </form>
    <div class="footer"></div>
  </div>
</main>
<script>
document.getElementById('pw-eye').addEventListener('click',()=>{
  const i=document.getElementById('pw'),b=document.getElementById('pw-eye'),show=i.type==='password';
  i.type=show?'text':'password';
  b.setAttribute('aria-label',show?'Hide password':'Show password');
  b.firstElementChild.className='ti '+(show?'ti-eye-off':'ti-eye');
});
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> Signing in...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'Error');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> Open dashboard';
  }
});
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="dark light">
<title>Dashboard · Lumen Gate</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%2032%2032%22%3E%3Cdefs%3E%3ClinearGradient%20id%3D%22g%22%20x1%3D%220%22%20y1%3D%220%22%20x2%3D%221%22%20y2%3D%221%22%3E%3Cstop%20offset%3D%220%22%20stop-color%3D%22%232dd4bf%22/%3E%3Cstop%20offset%3D%221%22%20stop-color%3D%22%232563c9%22/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect%20width%3D%2232%22%20height%3D%2232%22%20rx%3D%229%22%20fill%3D%22url%28%23g%29%22/%3E%3Cpath%20d%3D%22M6%2017h5l3-8%204%2014%203-6h5%22%20fill%3D%22none%22%20stroke%3D%22%2304201c%22%20stroke-width%3D%222.6%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22/%3E%3C/svg%3E">
<script>try{document.documentElement.setAttribute('data-theme',localStorage.getItem('gateway-theme')==='light'?'light':'dark')}catch(e){}</script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
/* ==========================================================================
   Lumen Gate — dashboard design system
   1. Tokens  2. Base  3. Shell  4. Primitives  5. Pages  6. Overlays  7. Responsive
   ========================================================================== */

/* 1. Tokens ---------------------------------------------------------------- */
:root{
  color-scheme:dark;
  --bg:#080f17;--bg2:#0c1520;--bg3:#15212d;
  --card:#0f1923;--card-b:#233443;--card-bh:#35506a;
  --t1:#e8eff5;--t2:#9db0c0;--t3:#6b8093;
  --accent:#2dd4bf;--accent2:#5eead4;--accent-d:rgba(45,212,191,.12);--on-accent:#04201c;
  --green:#4ade80;--green-t:#4ade80;--green-bg:rgba(74,222,128,.12);
  --red:#f87171;--red-t:#f87171;--red-bg:rgba(248,113,113,.12);
  --amber:#fbbf24;--amber-t:#fbbf24;--amber-bg:rgba(251,191,36,.12);
  --purple:#7aa7f5;--purple-bg:rgba(122,167,245,.13);
  --shadow:0 8px 28px -10px rgba(0,0,0,.65);--shadow-lg:0 28px 70px -14px rgba(0,0,0,.8);
  --ring:0 0 0 3px rgba(45,212,191,.32);--scrim:rgba(3,8,13,.66);--field:rgba(0,0,0,.22);
  --font:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --sp-1:4px;--sp-2:8px;--sp-3:12px;--sp-4:16px;--sp-5:24px;--sp-6:32px;
  --r-sm:8px;--r-md:12px;--r-lg:18px;--radius:16px;--sidebar-w:244px;
  --ease:cubic-bezier(.2,.8,.2,1);
}
[data-theme="light"]{
  color-scheme:light;
  --bg:#f2f5f7;--bg2:#ffffff;--bg3:#e9eef2;
  --card:#ffffff;--card-b:#dbe2e9;--card-bh:#b7c4d1;
  --t1:#0b1620;--t2:#4b5b6a;--t3:#7a8896;
  --accent:#0b8f84;--accent2:#097a71;--accent-d:#dcf3f0;--on-accent:#ffffff;
  --green:#138a55;--green-t:#0f7547;--green-bg:#dcf3e6;
  --red:#d43b3b;--red-t:#b92f2f;--red-bg:#fbe3e3;
  --amber:#b36a00;--amber-t:#935700;--amber-bg:#fbefd5;
  --purple:#2563c9;--purple-bg:#e0eafb;
  --shadow:0 8px 24px -10px rgba(11,22,32,.18);--shadow-lg:0 28px 70px -14px rgba(11,22,32,.3);
  --ring:0 0 0 3px rgba(11,143,132,.3);--scrim:rgba(11,22,32,.45);--field:#f6f8fa;
}

/* 2. Base ------------------------------------------------------------------ */
*{margin:0;padding:0;box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{font-family:var(--font);background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;line-height:1.5;-webkit-font-smoothing:antialiased;transition:background .25s,color .25s}
a{color:inherit;text-decoration:none}
button,input,select,textarea{font:inherit;color:inherit}
button{cursor:pointer}
:focus-visible{outline:none;box-shadow:var(--ring)}
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:8px;border:2px solid transparent;background-clip:content-box}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes ring{0%{box-shadow:0 0 0 0 currentColor}70%,100%{box-shadow:0 0 0 7px transparent}}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}
@keyframes spin{to{transform:rotate(360deg)}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}

/* 3. Shell ----------------------------------------------------------------- */
.sidebar{width:var(--sidebar-w);background:var(--bg2);border-right:1px solid var(--card-b);display:flex;flex-direction:column;position:fixed;left:0;top:0;bottom:0;z-index:200;transition:transform .25s var(--ease)}
.logo{display:flex;align-items:center;gap:12px;padding:20px 18px 16px;border-bottom:1px solid var(--card-b)}
.logo-img,.mob-logo{display:flex;flex-shrink:0}
.logo-img svg{width:36px;height:36px}.mob-logo svg{width:28px;height:28px}
.logo-name{font-size:15px;font-weight:650;letter-spacing:-.01em}
.logo-sub{font-size:11px;color:var(--t3)}
.sb-close{display:none;position:absolute;right:12px;top:18px;width:32px;height:32px;border-radius:var(--r-sm);background:var(--accent-d);border:0;color:var(--t2);font-size:16px;align-items:center;justify-content:center}
.nav-wrap{flex:1;overflow-y:auto;padding:8px 10px}
.nav-sec{padding:16px 10px 6px;font-size:11px;font-weight:600;color:var(--t3)}
.nav-it{display:flex;align-items:center;gap:10px;padding:9px 12px;margin:1px 0;border-radius:var(--r-md);color:var(--t2);font-size:13.5px;cursor:pointer;transition:background .15s,color .15s}
.nav-it i{font-size:18px;width:20px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--bg3);color:var(--t1)}
.nav-it.on{background:var(--accent-d);color:var(--accent2);font-weight:600}
.nav-badge{margin-left:auto;background:var(--accent-d);color:var(--accent2);font-size:11px;padding:1px 8px;border-radius:99px;font-weight:600}
.sb-foot{padding:12px;border-top:1px solid var(--card-b);display:flex;flex-direction:column;gap:8px}
.tg-btn,.theme-btn,.logout-btn{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;height:36px;border-radius:var(--r-md);font-size:13px;font-weight:550;border:1px solid var(--card-b);background:transparent;color:var(--t2);transition:background .15s,color .15s,transform .12s}
.tg-btn{background:var(--accent);color:var(--on-accent);border-color:transparent}
.tg-btn:hover{filter:brightness(1.08)}
.theme-btn:hover{background:var(--bg3);color:var(--t1)}
.logout-btn{color:var(--red-t);border-color:transparent;background:var(--red-bg)}
.logout-btn:hover{filter:brightness(1.12)}
.tg-btn:active,.theme-btn:active,.logout-btn:active{transform:scale(.98)}
.mob-top{display:none;position:fixed;top:0;left:0;right:0;height:56px;padding:env(safe-area-inset-top,0) 14px 0;background:color-mix(in srgb,var(--bg2) 88%,transparent);backdrop-filter:blur(12px);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between}
.mob-top .ml{display:flex;align-items:center;gap:10px}
.mob-title{font-size:14px;font-weight:650}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{width:36px;height:36px;border-radius:var(--r-sm);background:var(--bg3);border:0;color:var(--t2);font-size:18px;display:flex;align-items:center;justify-content:center}
.overlay{display:none;position:fixed;inset:0;background:var(--scrim);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-left:var(--sidebar-w);flex:1;padding:32px 32px 64px;min-width:0;max-width:1400px}
.pg{display:none}
.pg.on{display:block;animation:fi .22s var(--ease)}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:24px}
.tb-title{font-size:22px;font-weight:700;letter-spacing:-.02em;display:flex;align-items:center;gap:10px}
.tb-title i{color:var(--accent);font-size:22px}
.tb-sub{font-size:13px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.ml-auto{margin-left:auto}
.mb16{margin-bottom:16px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:16px;margin-bottom:16px}

/* 4. Primitives ------------------------------------------------------------ */
.badge,.exp-chip,.proto-chip,.conn-status-pill{display:inline-flex;align-items:center;gap:6px;font-weight:600;white-space:nowrap;border-radius:99px}
.badge{font-size:12px;padding:3px 10px}
.exp-chip{font-size:11px;padding:2px 9px}
.proto-chip{font-size:11px;padding:2px 9px;border-radius:7px}
.bg-green,.ec-ok,.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.bg-blue,.ec-inf,.pc-ws{background:var(--accent-d);color:var(--accent2)}
.bg-amber,.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.bg-red,.ec-exp{background:var(--red-bg);color:var(--red-t)}
.bg-purple,.pc-xhttp{background:var(--purple-bg);color:var(--purple)}
.dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green);color:var(--green)}.dr{background:var(--red);color:var(--red)}.da{background:var(--amber);color:var(--amber)}.db{background:var(--accent);color:var(--accent)}
.pulse{animation:ring 2s infinite}

.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;height:34px;padding:0 14px;border-radius:var(--r-md);border:1px solid transparent;font-size:13px;font-weight:550;white-space:nowrap;transition:background .15s,border-color .15s,transform .12s,filter .15s}
.btn i{font-size:15px}
.btn:active{transform:scale(.97)}
.btn:disabled{opacity:.45;cursor:not-allowed;transform:none}
.btn-p{background:var(--accent);color:var(--on-accent)}.btn-p:hover{filter:brightness(1.1)}
.btn-o{background:transparent;border-color:var(--card-b);color:var(--t2)}.btn-o:hover{background:var(--bg3);color:var(--t1)}
.btn-g{background:var(--accent-d);color:var(--accent2)}.btn-g:hover{filter:brightness(1.15)}
.btn-d{background:var(--red-bg);color:var(--red-t)}.btn-d:hover{filter:brightness(1.15)}
.btn-pur{background:var(--purple-bg);color:var(--purple)}.btn-pur:hover{filter:brightness(1.15)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t)}.btn-amber:hover{filter:brightness(1.15)}
.btn-sm{height:28px;padding:0 10px;font-size:12px;border-radius:var(--r-sm)}
.btn-icon{width:30px;height:30px;padding:0;border-radius:var(--r-sm)}

.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:20px;transition:border-color .2s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:14px;font-weight:650;margin-bottom:16px;display:flex;align-items:center;gap:8px}
.card-title i{font-size:18px;color:var(--accent)}
.sr{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px solid var(--card-b);font-size:13px}
.sr:last-child{border-bottom:0}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:8px}
.sr-k i{font-size:15px;color:var(--t3)}
.sr-v{font-weight:600;text-align:right}
.ch{position:relative;height:240px}.ch-lg{position:relative;height:330px}.ch-sm{position:relative;height:190px}

.tog{width:38px;height:22px;border-radius:99px;background:var(--bg3);border:1px solid var(--card-b);position:relative;flex-shrink:0;transition:background .2s var(--ease)}
.tog::after{content:'';position:absolute;top:2px;left:2px;width:16px;height:16px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.35);transition:transform .2s var(--ease)}
.tog.on{background:var(--accent);border-color:transparent}
.tog.on::after{transform:translateX(16px)}

.form-row{display:flex;gap:12px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:6px}
.fg label,.pw-field label,.modal-v2-field label,.cp-block-label{font-size:12.5px;font-weight:600;color:var(--t2);display:flex;align-items:center;gap:6px}
.fi,.fs,.cp-input-full,.pw-input,.modal-v2-input,.subs-search input,.lmodal-search input{height:38px;padding:0 12px;border-radius:var(--r-md);border:1px solid var(--card-b);background:var(--field);color:var(--t1);font-size:13.5px;outline:none;transition:border-color .15s,box-shadow .15s;width:100%}
.fi,.fs{min-width:100px;width:auto}
.fi::placeholder,.cp-input-full::placeholder,.pw-input::placeholder,.modal-v2-input::placeholder,.subs-search input::placeholder,.lmodal-search input::placeholder{color:var(--t3)}
.fi:focus,.fs:focus,.cp-input-full:focus,.pw-input:focus,.modal-v2-input:focus,.subs-search input:focus,.lmodal-search input:focus{border-color:var(--accent);box-shadow:var(--ring)}
.fs option{background:var(--card)}
.cl{display:flex;gap:10px;align-items:flex-start;padding:12px 14px;margin-top:12px;border-radius:var(--r-md);background:var(--accent-d);color:var(--t2);font-size:12.5px;line-height:1.6}
.cl i{font-size:16px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);color:var(--amber-t)}.cl.amber i{color:var(--amber)}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.chip{font-size:12px;font-weight:550;padding:5px 12px;border-radius:99px;background:transparent;color:var(--t2);border:1px solid var(--card-b);transition:.15s;white-space:nowrap}
.chip:hover{background:var(--bg3);color:var(--t1)}
.chip.active{background:var(--accent-d);color:var(--accent2);border-color:transparent}
.empty{text-align:center;padding:48px 20px;color:var(--t3)}
.empty i{font-size:38px;opacity:.5;margin-bottom:12px;display:block}
.empty p{font-size:13px;margin-top:4px}
.spbar,.ubar,.conn-duration-track,.pw-strength{height:6px;border-radius:99px;background:var(--bg3);overflow:hidden}
.spbar{margin-top:6px}
.spfill,.ubar-f{height:100%;border-radius:99px;background:var(--accent);transition:width .6s var(--ease)}
.utxt{font-size:12px;color:var(--t3);display:flex;justify-content:space-between}
.m-icon,.traf-mini-icon,.conn-hero-icon,.srv-tile-icon,.conn-stat-icon,.lrow-v2-avatar,.log-ic,.cfg-head-icon,.cp-head-icon,.srv-hero-icon,.pw-hero-icon,.sub-card-icon,.modal-v2-icon,.lmodal-icon,.conn-avatar,.conn-ip-icon,.proto-card-icon,.conn-empty-v2-icon,.subs-empty-v2-icon{display:flex;align-items:center;justify-content:center;flex-shrink:0;background:var(--accent-d);color:var(--accent)}
.m-icon{width:36px;height:36px;border-radius:var(--r-md);margin-bottom:12px;font-size:18px}
.m-icon.suc,.conn-ip-icon{background:var(--green-bg);color:var(--green-t)}
.m-icon.dan{background:var(--red-bg);color:var(--red-t)}
.m-icon.pur,.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}

/* 5. Pages ----------------------------------------------------------------- */
/* Overview metrics */
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:16px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px;transition:border-color .2s,transform .2s var(--ease)}
.metric:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.m-label{font-size:13px;color:var(--t2);margin-bottom:6px;font-weight:550}
.m-val{font-size:28px;font-weight:700;line-height:1.1;letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.m-unit{font-size:13px;font-weight:500;color:var(--t3)}
.m-sub{font-size:12px;color:var(--t3);margin-top:8px;display:flex;align-items:center;gap:4px}
.vless-box{background:var(--card);border:1px solid var(--card-b);border-left:3px solid var(--accent);border-radius:var(--radius);padding:20px;margin-bottom:16px}
.vl-header{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;margin-bottom:14px}
.vl-title{font-size:14px;font-weight:650;display:flex;align-items:center;gap:8px}
.vl-title i{color:var(--accent);font-size:18px}
.vl-code{background:var(--field);border:1px solid var(--card-b);border-radius:var(--r-md);padding:12px 14px;font-size:12px;font-family:var(--mono);color:var(--accent2);word-break:break-all;line-height:1.8}
.vl-actions{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}

/* Traffic */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:16px;margin-bottom:16px}
.traf-main-stat,.traf-mini,.traf-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius)}
.traf-main-stat{padding:22px;border-top:3px solid var(--accent)}
.traf-main-label,.traf-mini-label,.conn-hero-label{font-size:13px;color:var(--t2);font-weight:550;display:flex;align-items:center;gap:6px}
.traf-main-label{margin-bottom:10px}
.traf-main-val{font-size:36px;font-weight:700;line-height:1;letter-spacing:-.03em;display:flex;align-items:baseline;gap:6px;font-variant-numeric:tabular-nums}
.traf-main-val span{font-size:15px;font-weight:500;color:var(--t3)}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:12px;font-weight:600;padding:3px 10px;border-radius:99px;margin-top:12px}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{padding:18px;display:flex;flex-direction:column;justify-content:space-between}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:34px;height:34px;border-radius:var(--r-md);font-size:16px}
.traf-mini-val{font-size:22px;font-weight:700;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.traf-mini-sub{font-size:12px;color:var(--t3);margin-top:3px}
.traf-chart-card{padding:22px;margin-bottom:16px}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-bottom:6px}
.traf-chart-title{font-size:15px;font-weight:650;display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px}
.traf-chart-sub{font-size:12.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--t2)}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-range-tabs{display:inline-flex;gap:2px;background:var(--bg3);padding:3px;border-radius:var(--r-md)}
.traf-range-tab{padding:5px 13px;border-radius:var(--r-sm);font-size:12px;font-weight:550;color:var(--t2);border:0;background:transparent;transition:.15s}
.traf-range-tab.on{background:var(--card);color:var(--t1);box-shadow:var(--shadow)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}

/* Create config panel, server info, password */
.create-panel,.srv-panel,.pw-panel{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);overflow:hidden;margin-bottom:16px}
.cp-head,.srv-hero,.pw-hero{display:flex;align-items:center;gap:14px;padding:20px 24px;border-bottom:1px solid var(--card-b)}
.cp-head-icon,.srv-hero-icon,.pw-hero-icon{width:44px;height:44px;border-radius:var(--r-md);font-size:20px}
.cp-head-text,.srv-hero-text,.pw-hero-text{flex:1;min-width:0}
.cp-head-title,.pw-hero-title{font-size:16px;font-weight:650;letter-spacing:-.01em}
.srv-hero-domain{font-size:16px;font-weight:650;word-break:break-all}
.cp-head-sub,.pw-hero-sub,.srv-hero-sub{font-size:13px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.cp-body,.pw-body{padding:20px 24px 24px}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;margin-bottom:16px}
.cp-block{background:var(--bg2);border:1px solid var(--card-b);border-radius:var(--r-md);padding:16px}
.cp-block-label{margin-bottom:12px}
.cp-block-label i{color:var(--accent);font-size:16px}
.cp-mini-row{display:flex;gap:8px;margin-top:10px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 84px}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.proto-card{border:1.5px solid var(--card-b);border-radius:var(--r-md);padding:14px 12px;text-align:center;position:relative;background:transparent;transition:border-color .15s,background .15s}
.proto-card:hover{border-color:var(--card-bh)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d)}
.proto-card-check{position:absolute;top:8px;right:8px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:var(--on-accent);font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.18s var(--ease)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-icon{width:34px;height:34px;border-radius:var(--r-md);font-size:17px;margin:0 auto 8px}
.proto-card.active .proto-card-icon{background:var(--accent);color:var(--on-accent)}
.proto-card-title{font-size:13px;font-weight:650}
.proto-card-desc{font-size:11.5px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--t3);flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:16px;flex-shrink:0}
.cp-submit-btn,.pw-submit{display:flex;align-items:center;justify-content:center;gap:8px;height:42px;padding:0 24px;border-radius:var(--r-md);border:0;background:var(--accent);color:var(--on-accent);font-size:14px;font-weight:600;transition:filter .15s,transform .12s}
.cp-submit-btn:hover,.pw-submit:hover{filter:brightness(1.1)}
.cp-submit-btn:active,.pw-submit:active{transform:scale(.98)}
.pw-submit{width:100%}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:20px 24px 24px}
.srv-tile{display:flex;align-items:center;gap:12px;background:var(--bg2);border:1px solid var(--card-b);border-radius:var(--r-md);padding:12px 14px}
.srv-tile-icon{width:36px;height:36px;border-radius:var(--r-md);font-size:17px}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:12px;color:var(--t3);margin-bottom:2px}
.srv-tile-val{font-size:13.5px;font-weight:600;word-break:break-word}
.pw-field{position:relative;margin-bottom:14px}
.pw-field label{margin-bottom:6px}
.pw-input{padding-right:42px}
.pw-eye{position:absolute;right:8px;top:30px;width:30px;height:30px;background:none;border:0;border-radius:var(--r-sm);color:var(--t3);font-size:17px;display:flex;align-items:center;justify-content:center}
.pw-eye:hover{color:var(--t1);background:var(--bg3)}
.pw-strength{height:5px;margin-top:8px;display:flex;gap:3px;background:none}
.pw-strength-seg{flex:1;height:100%;border-radius:99px;background:var(--bg3);transition:background .25s}
.pw-strength-label{font-size:12px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:6px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0 18px}
.pw-req{font-size:12px;padding:3px 10px;border-radius:99px;background:var(--bg3);color:var(--t3);font-weight:550;display:flex;align-items:center;gap:5px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}

/* Live connections */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px}
.conn-hero-tile{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px}
.conn-hero-icon{width:34px;height:34px;border-radius:var(--r-md);background:var(--green-bg);color:var(--green-t);font-size:17px;margin-bottom:12px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{margin-bottom:4px}
.conn-hero-val{font-size:24px;font-weight:700;line-height:1.1;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.conn-hero-unit{font-size:13px;color:var(--t3);font-weight:500}
.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.conn-toolbar-title{font-size:15px;font-weight:650;display:flex;align-items:center;gap:8px}
.conn-toolbar-title i{color:var(--green-t);font-size:18px}
.conn-live-badge{display:flex;align-items:center;gap:8px;font-size:12px;font-weight:600;color:var(--green-t);background:var(--green-bg);padding:4px 12px;border-radius:99px}
.conn-live-dot{width:8px;height:8px;border-radius:50%;background:var(--green);color:var(--green);animation:ring 2s infinite}
.conn-grid-v2,.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.conn-card-v2,.conn-card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);overflow:hidden;transition:border-color .2s,transform .2s var(--ease);position:relative}
.conn-card-v2:hover,.conn-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.conn-card-v2-glow{display:none}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 18px 14px}
.conn-avatar{width:42px;height:42px;border-radius:var(--r-md);background:var(--green-bg);color:var(--green-t);font-size:18px;position:relative}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:15px;border:1.5px solid var(--green);animation:ring 2.4s infinite;color:var(--green);opacity:.5}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2,.conn-ip{font-family:var(--mono);font-size:14px;font-weight:700;display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:0;color:var(--t3);font-size:14px;padding:2px;display:flex}.conn-ip-copy:hover{color:var(--accent)}
.conn-label-v2,.conn-label{font-size:12px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:11px;padding:3px 10px;background:var(--green-bg);color:var(--green-t);flex-shrink:0}
.conn-card-v2-divider{height:1px;background:var(--card-b);margin:0 18px}
.conn-card-v2-body{padding:14px 18px 18px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:28px;height:28px;border-radius:var(--r-sm);font-size:14px}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:11px;color:var(--t3)}
.conn-stat-text-val{font-size:13px;font-weight:600;margin-top:1px}
.conn-duration-fill{height:100%;border-radius:99px;background:var(--green);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;width:40%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.3),transparent);animation:shimmer 1.8s linear infinite}
.conn-card{padding:16px 18px;border-left:3px solid var(--green)}
.conn-ip-row{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.conn-ip-icon{width:34px;height:34px;border-radius:var(--r-md);font-size:16px}
.conn-meta{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:var(--t3);padding-top:10px;border-top:1px solid var(--card-b)}
.conn-empty-v2,.subs-empty-v2{text-align:center;padding:64px 20px;background:var(--card);border:1.5px dashed var(--card-b);border-radius:var(--radius)}
.conn-empty-v2-icon,.subs-empty-v2-icon{width:60px;height:60px;border-radius:var(--r-lg);font-size:26px;margin:0 auto 16px;color:var(--t3)}
.subs-empty-v2-icon{color:var(--purple);background:var(--purple-bg)}
.conn-empty-v2-title,.subs-empty-v2-title{font-size:15px;font-weight:650;margin-bottom:6px}
.conn-empty-v2-sub,.subs-empty-v2-sub{font-size:13px;color:var(--t3)}
.subs-empty-v2{grid-column:1/-1}

/* Sub groups */
.sub-box{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:12px;padding:14px 16px;background:var(--purple-bg);border-radius:var(--r-md)}
.sub-url{font-family:var(--mono);font-size:12px;color:var(--purple);word-break:break-all;flex:1}
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:16px}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{padding-left:38px;background:var(--card)}
.subs-search i{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:16px}
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);overflow:hidden;transition:border-color .2s,transform .2s var(--ease),box-shadow .2s}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:var(--shadow)}
.sub-card-top{padding:20px 20px 16px;border-bottom:1px solid var(--card-b)}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:12px}
.sub-card-icon{width:44px;height:44px;border-radius:var(--r-md);font-size:20px;background:var(--purple-bg);color:var(--purple)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:16px;font-weight:650;letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:12.5px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:28px;height:28px;border-radius:var(--r-sm);display:flex;align-items:center;justify-content:center;font-size:14px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}
.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);margin-top:16px;background:var(--bg2);border:1px solid var(--card-b);border-radius:var(--r-md);overflow:hidden}
.sub-card-stat{padding:10px 8px;text-align:center;border-right:1px solid var(--card-b)}
.sub-card-stat:last-child{border-right:0}
.sub-card-stat-val{font-size:16px;font-weight:700;line-height:1.2;font-variant-numeric:tabular-nums}
.sub-card-stat-label{font-size:11.5px;color:var(--t3);margin-top:3px}
.sub-card-url-row{margin:14px 20px 0;background:var(--bg2);border:1px dashed var(--card-b);border-radius:var(--r-md);padding:9px 12px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:var(--mono);font-size:11px;color:var(--t2);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:0;color:var(--t3);font-size:15px;padding:3px;display:flex;flex-shrink:0}.sub-card-url-copy:hover{color:var(--accent)}
.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:8px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;min-width:fit-content}

/* Config list */
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--r-lg);transition:border-color .2s,box-shadow .2s;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:var(--shadow)}
.cfg-card.is-off{opacity:.6}.cfg-card.is-exp{opacity:.8}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:10px;height:10px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 4px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 4px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 4px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:4px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:14.5px;font-weight:650;display:flex;align-items:center;gap:8px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--t3)}
.cfg-uuid-mini{font-family:var(--mono);font-size:11px;color:var(--t2);background:var(--bg3);padding:2px 8px;border-radius:6px;cursor:pointer;transition:.15s}
.cfg-uuid-mini:hover{color:var(--accent2);background:var(--accent-d)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:6px}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:6px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:6px;flex-shrink:0}
.cfg-sub-tag{font-size:12px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:13px}

/* Activity log */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:12px 0;border-bottom:1px solid var(--card-b)}
.log-item:last-child{border-bottom:0}
.log-ic{width:32px;height:32px;border-radius:var(--r-md);font-size:15px}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}.log-ic.err{background:var(--red-bg);color:var(--red-t)}.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:13.5px;line-height:1.6}
.log-time{font-size:12px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.log-kind{font-size:11px;padding:1px 8px;border-radius:99px;background:var(--accent-d);color:var(--accent2);font-weight:600}
.erow{padding:10px 0;border-bottom:1px solid var(--card-b)}.erow:last-child{border-bottom:0}
.etime{color:var(--t3);font-size:12px;margin-bottom:4px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-t);font-family:var(--mono);background:var(--red-bg);padding:7px 10px;border-radius:var(--r-sm);word-break:break-all;font-size:12px}
.dash-footer{border-top:1px solid var(--card-b);margin-top:16px;padding-top:16px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:12px;color:var(--t3)}
.df-link{font-size:13px;color:var(--accent2);display:flex;align-items:center;gap:6px;font-weight:600}

/* 6. Overlays -------------------------------------------------------------- */
.modal-bg{display:none;position:fixed;inset:0;background:var(--scrim);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(5px);padding:16px}
.modal-bg.open{display:flex}
.modal,.modal-v2{background:var(--card);border:1px solid var(--card-b);border-radius:20px;width:100%;max-height:92vh;overflow-y:auto;position:relative;box-shadow:var(--shadow-lg);animation:fi .22s var(--ease)}
.modal{max-width:520px;padding:26px}
.modal-v2{max-width:430px;padding:0}
.modal-close,.modal-v2-close{position:absolute;top:14px;right:14px;width:32px;height:32px;border-radius:var(--r-sm);background:var(--bg3);border:0;color:var(--t2);font-size:16px;display:flex;align-items:center;justify-content:center;z-index:2;transition:.15s}
.modal-close:hover,.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t)}
.modal-title{font-size:17px;font-weight:650;margin-bottom:18px;display:flex;align-items:center;gap:8px;letter-spacing:-.01em}
.modal-title i{color:var(--accent)}
.modal-v2-head{padding:22px 22px 16px}
.modal-v2-icon{width:42px;height:42px;border-radius:var(--r-md);font-size:20px;margin-bottom:12px}
.modal-v2-title{font-size:17px;font-weight:650;letter-spacing:-.01em}
.modal-v2-sub{font-size:13px;color:var(--t3);margin-top:3px;line-height:1.6}
.modal-v2-body{padding:16px 22px 22px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:12px}
.modal-v2-field label{margin-bottom:6px}
.modal-v2-field label i{color:var(--accent);font-size:14px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}
.modal-v2-input-wrap .modal-v2-input{padding-left:38px}
.modal-v2-hint{display:flex;gap:8px;align-items:flex-start;padding:10px 12px;border-radius:var(--r-md);background:var(--accent-d);font-size:12.5px;color:var(--t2);line-height:1.6}
.modal-v2-hint i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:8px;margin-top:16px}
.modal-v2-footer .btn{flex:1;height:38px}
.modal-v2-btn-cancel,.modal-v2-btn-submit{flex:1;display:flex;align-items:center;justify-content:center;gap:6px;height:38px;border-radius:var(--r-md);font-size:13px;font-weight:600;border:1px solid var(--card-b);background:transparent;color:var(--t2)}
.modal-v2-btn-submit{background:var(--accent);color:var(--on-accent);border-color:transparent}
.lmodal-head{padding:22px 24px 16px;border-bottom:1px solid var(--card-b);position:relative}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;padding-right:36px}
.lmodal-icon{width:44px;height:44px;border-radius:var(--r-md);font-size:20px}
.lmodal-title-v2{font-size:16px;font-weight:650}
.lmodal-sub-v2{font-size:12.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{padding-left:38px}
.lmodal-search i{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:12px;align-items:center}
.lmodal-qbtn{font-size:12px;font-weight:550;padding:5px 12px;border-radius:var(--r-sm);background:var(--accent-d);color:var(--accent2);border:0;display:inline-flex;align-items:center;gap:4px;transition:.15s}
.lmodal-qbtn:hover{filter:brightness(1.15)}
.lmodal-count{margin-left:auto;font-size:12px;color:var(--t3)}
.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:var(--r-md);cursor:pointer;margin-bottom:4px;border:1px solid transparent;transition:.15s}
.lrow-v2:hover{background:var(--bg3)}
.lrow-v2.checked{background:var(--accent-d);border-color:var(--accent)}
.lrow-v2-check{width:20px;height:20px;border-radius:6px;border:1.5px solid var(--t3);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s}
.lrow-v2.checked .lrow-v2-check{background:var(--accent);border-color:var(--accent)}
.lrow-v2-check i{font-size:13px;color:var(--on-accent);opacity:0;transform:scale(.5);transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:34px;height:34px;border-radius:var(--r-sm);font-size:15px}
.lrow-v2.checked .lrow-v2-avatar{background:var(--accent);color:var(--on-accent)}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:13.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:12px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:11px;font-weight:600;padding:2px 9px;border-radius:99px;flex-shrink:0}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}
.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.lmodal-footer-info{font-size:12px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}
.lrow{display:flex;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid var(--card-b)}.lrow:last-child{border-bottom:0}
.lrow-check{width:16px;height:16px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:13px}
.lrow-badge{font-size:11px;padding:2px 8px;border-radius:99px;background:var(--green-bg);color:var(--green-t);font-weight:600}
.toast{position:fixed;bottom:calc(22px + env(safe-area-inset-bottom,0px));left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);border-left:3px solid var(--accent);color:var(--t1);border-radius:var(--r-md);padding:11px 18px;font-size:13.5px;opacity:0;transition:opacity .25s,transform .25s var(--ease);z-index:900;box-shadow:var(--shadow-lg);pointer-events:none;max-width:calc(100vw - 32px)}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-left-color:var(--green)}.toast.err{border-left-color:var(--red)}

/* 7. Responsive ------------------------------------------------------------ */
@media(max-width:1100px){
  .traf-hero{grid-template-columns:1fr 1fr}
  .conn-hero{grid-template-columns:1fr 1fr}
}
@media(max-width:1050px){
  .sidebar{transform:translateX(-100%)}
  .sidebar.open{transform:none;box-shadow:var(--shadow-lg)}
  .sb-close{display:flex}
  .main{margin-left:0;padding:76px 20px 56px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:880px){
  .cfg-row{flex-wrap:wrap}.cfg-divider-v{display:none}.cfg-usage-col{min-width:100%;order:5}
}
@media(max-width:768px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:12px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
  .cfg-identity{min-width:0;flex:1}.cfg-usage-col,.cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}
  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;width:100%}
}
@media(max-width:760px){
  .cp-row,.proto-cards{grid-template-columns:1fr}
  .cp-footer{flex-direction:column;align-items:stretch}
  .cp-submit-btn{width:100%}
}
@media(max-width:560px){
  .srv-tiles,.traf-hero,.conn-hero{grid-template-columns:1fr}
  .traf-chart-body{height:260px}
  .conn-grid-v2,.conn-grid,.sub-grid{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:72px 14px 48px}
  .cp-head,.srv-hero,.pw-hero{padding:16px}.cp-body,.pw-body{padding:16px}.srv-tiles{padding:16px}
}
</style>
</head>
<body>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<div class="modal-bg" role="dialog" aria-modal="true" id="modal-links">
  <div class="modal-v2" style="max-width:500px">
    <div class="lmodal-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="lmodal-icon-row">
        <div class="lmodal-icon"><i class="ti ti-link-plus"></i></div>
        <div>
          <div class="lmodal-title-v2">Manage configs in <span id="modal-sub-name" style="color:var(--accent2)">—</span></div>
          <div class="lmodal-sub-v2">Choose the configs to include in this group</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="Search configs..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> Select all</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> Clear all</button>
        <span class="lmodal-count" id="lmodal-count">0 selected</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">Loading...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> Changes apply immediately</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">Close</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> Save</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" role="dialog" aria-modal="true" id="modal-create-sub">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">Create group</div>
      <div class="modal-v2-sub">Create a separate public page to share configs</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> Group name</label>
        <input class="modal-v2-input" id="ns-name" placeholder="e.g. Telegram channel">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> Description (optional)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="Short description of this group">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> Public page password (optional)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="Leave empty = no password">
      </div>
      <div class="cl" style="margin-top:14px"><i class="ti ti-info-circle"></i><span>The public page for this group will be available online at a unique link.</span></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6">Cancel</button>
        <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> Create group</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" role="dialog" aria-modal="true" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> Edit config</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>Title</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Quota (0 = Unlimited)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>Unit</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>Expiry (days from now, 0 = no change / unlimited)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>Note</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Fingerprint (uTLS)</label>
        <select class="fs" id="el-fp" style="width:100%">
          <option value="chrome">chrome</option>
          <option value="firefox">firefox</option>
          <option value="safari">safari</option>
          <option value="ios">ios</option>
          <option value="android">android</option>
          <option value="edge">edge</option>
          <option value="360">360</option>
          <option value="qq">qq</option>
          <option value="random">random</option>
          <option value="randomized">randomized</option>
        </select>
      </div>
      <div class="fg" style="flex:1"><label>ALPN (Empty = Default)</label><input class="fi" id="el-alpn" placeholder="e.g.: h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>Connection port</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label>IP limit (0 = Unlimited)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>Speed limit (0 = Unlimited)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label>Unit</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>To keep the current expiry, leave the expiry field at 0.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">Cancel</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> Save changes</button>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><svg viewBox="0 0 32 32" role="img" aria-label="Lumen Gate"><defs><linearGradient id="lgM" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--accent)"/><stop offset="1" style="stop-color:var(--purple)"/></linearGradient></defs><rect width="32" height="32" rx="9" fill="url(#lgM)"/><path d="M6 17h5l3-8 4 14 3-6h5" fill="none" stroke="var(--on-accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
    <span class="mob-title">Lumen Gate</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-img"><svg viewBox="0 0 32 32" role="img" aria-label="Lumen Gate"><defs><linearGradient id="lgS" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--accent)"/><stop offset="1" style="stop-color:var(--purple)"/></linearGradient></defs><rect width="32" height="32" rx="9" fill="url(#lgS)"/><path d="M6 17h5l3-8 4 14 3-6h5" fill="none" stroke="var(--on-accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
    <div><div class="logo-name">Lumen Gate</div><div class="logo-sub">v11</div></div>
  </div>
  <div class="nav-wrap" role="navigation" aria-label="Primary">
    <div class="nav-sec">Panel</div>
    <div tabindex="0" role="button" class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> Dashboard</div>
    <div tabindex="0" role="button" class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> Configs <span class="nav-badge" id="links-nb">0</span></div>
    <div tabindex="0" role="button" class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> Sub groups <span class="nav-badge" id="subs-nb">0</span></div>
    <div tabindex="0" role="button" class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> Subscription</div>
    <div tabindex="0" role="button" class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> Traffic</div>
    <div tabindex="0" role="button" class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> Connections <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec">System</div>
    <div tabindex="0" role="button" class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> Security</div>
    <div tabindex="0" role="button" class="nav-it" data-pg="logs"><i class="ti ti-history"></i> Activity log</div>
    <div tabindex="0" role="button" class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> Errors</div>
    <div tabindex="0" role="button" class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> WebSocket test</div>
    <div tabindex="0" role="button" class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> Settings</div>
    <div tabindex="0" role="button" class="nav-it" data-pg="support"><i class="ti ti-headset"></i> Support</div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">Light theme</span></button>
    
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> Sign out</button>
  </div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> Dashboard</div><div class="tb-sub" id="last-upd">Loading...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> Active</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh</button>
    </div>
  </div>
  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">Live connections</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> WebSocket / XHTTP Live</div></div>
    <div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">Total traffic</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">since startup</div></div>
    <div class="metric suc"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">Active configs</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">of total</div></div>
    <div class="metric pur"><div class="m-icon pur"><i class="ti ti-folders"></i></div><div class="m-label">Sub groups</div><div class="m-val" id="m-subs">—</div><div class="m-sub">Active</div></div>
  </div>
  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> Default link (no limits)</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">Fetching...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> Copy</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> Limited configs</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> Sub groups</button>
    </div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> Hourly traffic (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> Distribution</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> Service status</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● Active · strict</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS Tunnel</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> Siz10a XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● Active · 3 mode</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-folders"></i> Sub Groups</span><span class="sr-v" style="color:var(--green-t)">● Active v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription API</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> Uptime</span><span class="sr-v" id="uptime-inline">—</span></div>
      <div class="sr" style="flex-direction:column;align-items:flex-start;gap:4px">
        <div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> Relative load</span><span class="sr-v" id="bw-pct">—%</span></div>
        <div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> Config summary <span class="ml-auto badge bg-blue" id="lsummary-badge">0</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">Gateway v11 · Railway</span>
    
    
  </div>
</section>
<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> Configs</div><div class="tb-sub">Create and manage configs with quotas, expiry and groups</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">0 configs</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">Create a new config</div>
        <div class="cp-head-sub">UUID Random · Choose a quota, expiry and protocol</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> Config name</div>
          <input class="cp-input-full" id="nl-label" placeholder="e.g. Ali (phone)">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="Note (optional)">
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> Sub group and expiry</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— No group —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="Expiry (days) · 0 = Unlimited">
          </div>
          <div tabindex="0" role="button" class="chip-row" id="exp-chips">
            <span tabindex="0" role="button" class="chip" onclick="setExpiry(0,this)">Unlimited</span>
            <span tabindex="0" role="button" class="chip" onclick="setExpiry(7,this)">7 days</span>
            <span tabindex="0" role="button" class="chip active" onclick="setExpiry(30,this)">30 days</span>
            <span tabindex="0" role="button" class="chip" onclick="setExpiry(90,this)">90 days</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> Traffic quota</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = Unlimited">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div tabindex="0" role="button" class="chip-row" id="quota-chips">
          <span tabindex="0" role="button" class="chip" onclick="setQuota(0,'GB',this)">Unlimited</span>
          <span tabindex="0" role="button" class="chip" onclick="setQuota(500,'MB',this)">500 MB</span>
          <span tabindex="0" role="button" class="chip active" onclick="setQuota(1,'GB',this)">1 GB</span>
          <span tabindex="0" role="button" class="chip" onclick="setQuota(5,'GB',this)">5 GB</span>
          <span tabindex="0" role="button" class="chip" onclick="setQuota(10,'GB',this)">10 GB</span>
          <span tabindex="0" role="button" class="chip" onclick="setQuota(50,'GB',this)">50 GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> Transport protocol</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp-packet-up">XHTTP Ultra · packet-up</option>
          <option value="xhttp-stream-up">XHTTP Ultra · stream-up</option>
        </select>
        <div class="proto-cards">
          <div tabindex="0" role="button" class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <div tabindex="0" role="button" class="proto-card-check"><i class="ti ti-check"></i></div>
            <div tabindex="0" role="button" class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div tabindex="0" role="button" class="proto-card-title">VLESS / WS</div>
            <div tabindex="0" role="button" class="proto-card-desc">Stable, all-purpose</div>
          </div>
          <div tabindex="0" role="button" class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
            <div tabindex="0" role="button" class="proto-card-check"><i class="ti ti-check"></i></div>
            <div tabindex="0" role="button" class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div tabindex="0" role="button" class="proto-card-title">XHTTP · packet-up</div>
            <div tabindex="0" role="button" class="proto-card-desc">Compatible with CDN</div>
          </div>
          <div tabindex="0" role="button" class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
            <div tabindex="0" role="button" class="proto-card-check"><i class="ti ti-check"></i></div>
            <div tabindex="0" role="button" class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div tabindex="0" role="button" class="proto-card-title">XHTTP · stream-up</div>
            <div tabindex="0" role="button" class="proto-card-desc">Lower latency</div>
          </div>
        </div>
      </div>
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-fingerprint"></i> Fingerprint (uTLS)</div>
          <select class="cp-input-full fs" id="nl-fp">
            <option value="chrome" selected>chrome</option>
            <option value="firefox">firefox</option>
            <option value="safari">safari</option>
            <option value="ios">ios</option>
            <option value="android">android</option>
            <option value="edge">edge</option>
            <option value="360">360</option>
            <option value="qq">qq</option>
            <option value="random">random</option>
            <option value="randomized">randomized</option>
          </select>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-antenna-bars-5"></i> ALPN</div>
          <select class="cp-input-full fs" id="nl-alpn-preset" onchange="onAlpnPresetChange()">
            <option value="">Protocol default</option>
            <option value="h2,http/1.1">h2,http/1.1</option>
            <option value="http/1.1">http/1.1</option>
            <option value="h2">h2</option>
            <option value="__custom__">Custom...</option>
          </select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-alpn" placeholder="Custom value ALPN" style="display:none">
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-route"></i> Connection port</div>
          <input class="cp-input-full" id="nl-port" type="number" min="1" max="65535" placeholder="443" value="443">
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-users"></i> IP limit / concurrent users</div>
          <input class="cp-input-full" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = Unlimited" value="0">
          <div tabindex="0" role="button" class="chip-row" id="iplimit-chips">
            <span tabindex="0" role="button" class="chip active" onclick="setIpLimit(0,this)">Unlimited</span>
            <span tabindex="0" role="button" class="chip" onclick="setIpLimit(1,this)">1 user</span>
            <span tabindex="0" role="button" class="chip" onclick="setIpLimit(2,this)">2 users</span>
            <span tabindex="0" role="button" class="chip" onclick="setIpLimit(5,this)">5 users</span>
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block" style="flex:1">
          <div class="cp-block-label"><i class="ti ti-gauge"></i> Speed limit</div>
          <div class="form-row">
            <input class="cp-input-full" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = Unlimited" value="0" style="flex:1">
            <select class="fs" id="nl-speed-unit" style="flex:0 0 100px">
              <option value="MBIT" selected>Mbps</option>
              <option value="KB">KB/s</option>
              <option value="MB">MB/s</option>
            </select>
          </div>
          <div tabindex="0" role="button" class="chip-row" id="speed-chips">
            <span tabindex="0" role="button" class="chip active" onclick="setSpeedLimit(0,this)">Unlimited</span>
            <span tabindex="0" role="button" class="chip" onclick="setSpeedLimit(1,this)">1 Mbps</span>
            <span tabindex="0" role="button" class="chip" onclick="setSpeedLimit(5,this)">5 Mbps</span>
            <span tabindex="0" role="button" class="chip" onclick="setSpeedLimit(10,this)">10 Mbps</span>
            <span tabindex="0" role="button" class="chip" onclick="setSpeedLimit(25,this)">25 Mbps</span>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID Generated randomly · Only registered UUIDs may connect · The protocol cannot be changed after creation.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> Create config</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>No configs yet</p></div>
</section>
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> Sub groups</div><div class="tb-sub">Each group has its own public page with its configs</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">0 groups</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> New group</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="Search groups..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">No groups yet</div><div class="subs-empty-v2-sub">Create a group to organize your configs</div></div>
  </div>
</section>
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> Subscription</div><div class="tb-sub">Subscription links for apps like v2ray</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> Single subscription (each config)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:12px">Every config has its own subscription URL. On the config card, click the <i class="ti ti-rss"></i> icon.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> Full subscription (admin)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:4px">Includes all active configs.</p>
      <div class="sub-box"><span class="sub-url" id="sub-all-url">Fetching...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
      <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span>This URL only works in a browser that is signed in to the panel (requires the session cookie).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> Group subscription links</div>
    <div id="sub-groups-list">Loading...</div>
  </div>
</section>
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> Traffic</div><div class="tb-sub">Bandwidth usage analytics and monitoring</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh</button></div>
  </div>

  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> Total traffic used</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">Hourly average</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB per hour</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">Peak usage</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">Busiest hour</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">Lowest usage</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB per hour</div></div>
    </div>
  </div>

  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> Traffic trend</div>
        <div class="traf-chart-sub">Megabytes per hour</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> Usage</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> Average</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> Live connections</div><div class="tb-sub">Live IP and traffic monitoring for every connection</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh</button></div>
  </div>

  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">Live connections</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">Current total traffic</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">Average session length</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">Unique IPs</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>

  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> Connection list</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> Auto-refreshes every 5 seconds</div>
  </div>

  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">No active connections</div>
    <div class="conn-empty-v2-sub">Clients appear here as soon as they connect</div>
  </div>
</section>
<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> Security</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> Encryption</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● Active (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> Protocols</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> Password hash</span><span class="sr-v">SHA-256+Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> Session</span><span class="sr-v">HttpOnly · 7 days</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> Access control</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth strict</span><span class="sr-v" style="color:var(--green-t)">● Active v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> Enable / disable configs</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> Traffic quota</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> Expiry date</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> Sub public page password</span><span class="sr-v" style="color:var(--green-t)">● Optional · SHA-256</span></div>
    </div>
  </div>
</section>
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> Activity log</div><div class="tb-sub">Full history of panel events</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>No activity recorded yet</p></div></div>
</section>
<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> Errors</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">0</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> Error log</div><div id="errs-full">—</div></div>
</section>
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> WebSocket test</div></div></div>
  <div class="card" style="max-width:660px">
    <div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span>Only registered, active UUIDs can connect (this only tests VLESS/WS; XHTTP is tested from the client itself).</span></div>
    <div class="form-row" style="margin-bottom:12px">
      <div class="fg" style="flex:1"><label>UUID (must exist in Configs)</label><input class="fi" id="ws-uuid" placeholder="UUID an active config" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> connections</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> Disconnect</button>
    </div>
    <div class="form-row" style="margin-bottom:12px">
      <input class="fi" id="ws-msg" placeholder="Test message..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> Send</button>
    </div>
    <div style="background:var(--field);border:1px solid var(--card-b);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--t3)">Waiting for connection...</p>
    </div>
  </div>
</section>
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> Settings</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> Online · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Default port</div><div class="srv-tile-val">443 (TLS) · Editable per config</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Version</div><div class="srv-tile-val">v11</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Framework</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Platform</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Storage</div><div class="srv-tile-val">JSON File (/data)</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">Change password</div>
          <div class="pw-hero-sub">Choose a strong password and keep it somewhere safe</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>Current password</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="Enter your current password">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:6px">
          <label>New password</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="At least 4 characters" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> Password strength</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> At least 4 characters</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> Contains a number</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> Upper and lower case</span>
        </div>
        <div class="pw-field" style="margin-bottom:18px">
          <label>Confirm new password</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="Confirm new password">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> Save new password</button>
      </div>
    </div>
  </div>
</section>
<section class="pg" id="pg-support">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-headset"></i> Support</div></div></div>
  <div class="srv-panel">
    <div class="srv-hero">
      <div class="srv-hero-icon"><i class="ti ti-headset"></i></div>
      <div class="srv-hero-text">
        <div class="srv-hero-domain">Support</div>
        <div class="srv-hero-sub"><span class="dot dg pulse"></span> Contact</div>
      </div>
    </div>
    <div class="srv-tiles">
      <a class="srv-tile" href="https://t.me/X4GHUB" target="_blank" style="text-decoration:none;cursor:pointer">
        <div class="srv-tile-icon"><i class="ti ti-speakerphone"></i></div>
        <div class="srv-tile-text"><div class="srv-tile-label">Telegram channel</div><div class="srv-tile-val">t.me/X4GHUB</div></div>
      </a>
      <a class="srv-tile" href="https://github.com/x4gpanell" target="_blank" style="text-decoration:none;cursor:pointer">
        <div class="srv-tile-icon"><i class="ti ti-brand-github"></i></div>
        <div class="srv-tile-text"><div class="srv-tile-label">GitHub</div><div class="srv-tile-val">github.com/x4gpanell</div></div>
      </a>
    </div>
  </div>
</section>
</main>
<script>
let isDark=localStorage.getItem('gateway-theme')!=='light';
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  const icon=dark?'ti-sun':'ti-moon',label=dark?'Light theme':'Dark theme';
  document.getElementById('theme-icon').className='ti '+icon;
  document.getElementById('theme-label').textContent=label;
  const mobI=document.getElementById('theme-mob-icon');if(mobI)mobI.className='ti '+icon;
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('gateway-theme',isDark?'dark':'light');applyTheme(isDark);if(typeof restyleCharts==='function')restyleCharts()}
applyTheme(isDark);
function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n)}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> Expired</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> Unlimited</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> Expired</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} days left</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} days left</span>`;
}
function protoBadge(p){
  const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · packet-up','pc-xhttp'],'xhttp-stream-up':['XHTTP · stream-up','pc-xhttp'],'xhttp-stream-one':['XHTTP ULTRA','pc-ultra']};
  const v=m[p]||m['vless-ws'];
  return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function selectProto(val,el){
  document.getElementById('nl-proto').value = val;
  document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setIpLimit(n,el){
  document.getElementById('nl-iplimit').value = n;
  document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setSpeedLimit(n,el){
  document.getElementById('nl-speed').value = n;
  document.getElementById('nl-speed-unit').value = 'MBIT';
  document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function onAlpnPresetChange(){
  const p=document.getElementById('nl-alpn-preset').value;
  const inp=document.getElementById('nl-alpn');
  if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus();}
  else{inp.style.display='none';inp.value=p;}
}
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity};
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
let prevTraf=0,ch1,ch2,ch3;
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='of '+d.links_count+' configs';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' errors';
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;
    document.getElementById('last-upd').textContent='Last updated: '+new Date().toLocaleTimeString('en-US');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' connections';
    document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    const delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));
    document.getElementById('bw-pct').textContent=pct+'%';
    document.getElementById('bw-bar').style.width=pct+'%';
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));
      [ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
      if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> No errors</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('en-US')}</div><div class="emsg">${esc(e.error)}${e.url?' — '+esc(e.url):''}</div></div>`).join('');
}
async function loadActivity(){
  try{
    const r=await authF('/api/activity'),d=await r.json();
    const logs=(d.logs||[]).slice().reverse();
    const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    const kindFa={link:'Config',sub:'Group',auth:'Sign-in',connection:'Connection',system:'System'};
    el.innerHTML=logs.map(l=>`
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
        <div class="log-body">
          <div class="log-msg">${esc(l.message)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('en-US')} <span class="log-kind">${kindFa[l.kind]||l.kind}</span></div>
        </div>
      </div>
    `).join('');
  }catch(e){console.error(e)}
}
let allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    allSubsList=subs;allLinksList=links;
    const nlSub=document.getElementById('nl-sub');
    nlSub.innerHTML='<option value="">— No group —</option>'+subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' configs';
    document.getElementById('lsummary-badge').textContent=toFa(links.length);
    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>No configs</p></div>';return}
    empty.style.display='none';
    const subMap=Object.fromEntries(subs.map(s=>[s.sub_id,s.name]));
    grid.innerHTML=links.map(l=>{
  const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
  const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  const allowed=l.active&&!l.expired;
  const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
  return `<div class="cfg-card ${cardCls}">
    <div class="cfg-row">
      <span class="cfg-status-dot ${allowed?'pulse':''}"></span>
      <div class="cfg-identity">
        <div class="cfg-label">${esc(l.label)}</div>
        <div class="cfg-sub-meta">
          <span tabindex="0" role="button" class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID Copied','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
          <span>${new Date(l.created_at).toLocaleDateString('en-US')}</span>
        </div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-usage-col">
        <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
        <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>of ${lim}</span></div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-badges-col">
        ${protoBadge(l.protocol)}
        <span class="cfg-sub-tag" title="Connection port"><i class="ti ti-route"></i> :${l.port||443}</span>
        <span class="cfg-sub-tag" title="Fingerprint"><i class="ti ti-fingerprint"></i> ${esc(l.fingerprint||'chrome')}</span>
        <span class="cfg-sub-tag" title="Connected IPs / limit"><i class="ti ti-users"></i> ${l.connected_ips||0}${l.ip_limit?('/'+l.ip_limit):' (∞)'}</span>
        <span class="cfg-sub-tag" title="Speed limit"><i class="ti ti-gauge"></i> ${l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'Unlimited'}</span>
        ${l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?`<span class="cfg-sub-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)}</span>`:''}
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-actions">
        <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="Enable / disable" aria-label="Enable / disable"></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('Link copied','ok'))" title="Copy link"><i class="ti ti-copy"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub Copied','ok'))" title="Sub URL"><i class="ti ti-rss"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR" aria-label="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="Edit" aria-label="Edit"><i class="ti ti-edit"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="Reset usage" aria-label="Reset usage"><i class="ti ti-rotate"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="Delete" aria-label="Delete"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  </div>`;
}).join('');
    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}" style="color:${l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)'}"></i>${esc(l.label)}</span><span class="sr-v" style="font-size:10px">${fmtB(l.used_bytes)} / ${l.limit_bytes===0?'∞':fmtB(l.limit_bytes)}</span></div>`).join('');
  }catch(e){console.error(e)}
}
async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'New config';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=document.getElementById('nl-note').value.trim();
  const sub_id=document.getElementById('nl-sub').value||null;
  const protocol=document.getElementById('nl-proto').value||'vless-ws';
  const fingerprint=document.getElementById('nl-fp').value||'chrome';
  const alpn=document.getElementById('nl-alpn').value.trim();
  const port=Number(document.getElementById('nl-port').value)||443;
  const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;
  const speed_limit_unit=document.getElementById('nl-speed-unit').value;
  try{
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');
    document.getElementById('nl-port').value='443';
    document.getElementById('nl-iplimit').value='0';
    document.getElementById('nl-speed').value='0';
    document.getElementById('nl-alpn-preset').value='';
    document.getElementById('nl-alpn').style.display='none';
    toast('Config created ✓','ok');loadLinks();
  }catch(e){toast('Could not create config','err')}
}
function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  document.getElementById('el-fp').value=l.fingerprint||'chrome';
  document.getElementById('el-alpn').value=l.alpn||'';
  document.getElementById('el-port').value=l.port||443;
  document.getElementById('el-iplimit').value=l.ip_limit||0;
  if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';document.getElementById('el-speed-unit').value='MBIT';}
  else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);document.getElementById('el-speed-unit').value='MBIT';}
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const label=document.getElementById('el-label').value.trim();
  const note=document.getElementById('el-note').value.trim();
  const val=document.getElementById('el-val').value;
  const unit=document.getElementById('el-unit').value;
  const exp=document.getElementById('el-exp').value;
  const fingerprint=document.getElementById('el-fp').value||'chrome';
  const alpn=document.getElementById('el-alpn').value.trim();
  const port=Number(document.getElementById('el-port').value)||443;
  const ip_limit=Number(document.getElementById('el-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('el-speed').value)||0;
  const speed_limit_unit=document.getElementById('el-speed-unit').value;
  const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('Config updated ✓','ok');loadLinks();
  }catch(e){toast('Could not update config','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'Enabled ✓':'Disabled','ok');loadLinks();}catch(e){toast('Error','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('Usage reset ✓','ok');loadLinks();}catch(e){toast('Error','err')}
}
async function deleteLink(uuid){
  if(!confirm('Delete this config?'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('Deleted ✓','ok');loadLinks();}catch(e){toast('Error','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' Group';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  const grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">No groups yet</div><div class="subs-empty-v2-sub">Create a group to organize your configs</div></div>';
    return;
  }
  grid.innerHTML=subs.map(s=>`
    <div class="sub-card">
      <div class="sub-card-top">
        <div class="sub-card-head-v2">
          <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
          <div class="sub-card-titles">
            <div class="sub-card-name-v2">${esc(s.name)}</div>
            ${s.desc?`<div class="sub-card-desc-v2">${esc(s.desc)}</div>`:'<div class="sub-card-desc-v2" style="opacity:.5">No description</div>'}
          </div>
          <div class="sub-card-lock-badge ${s.has_password?'locked':'open'}" title="${s.has_password?'Password protected':'Public'}">
            <i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i>
          </div>
        </div>
        <div class="sub-card-stats">
          <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label">configs</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label">Active</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">used</div></div>
        </div>
      </div>
      <div class="sub-card-url-row">
        <span class="sub-card-url-text">${esc(s.public_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('Public link copied','ok'))" title="Copy"><i class="ti ti-copy"></i></button>
        <button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')" title="Open" aria-label="Open"><i class="ti ti-external-link"></i></button>
      </div>
      <div class="sub-card-bottom">
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> Configs</button>
        <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('Sub link copied','ok'))"><i class="ti ti-rss"></i> Sub</button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')" title="QR" aria-label="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')" title="Delete" aria-label="Delete"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  `).join('');
}
function filterSubs(q){
  q=q.trim().toLowerCase();
  if(!q){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(s=>s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)));
}
async function createSub(){
  const name=document.getElementById('ns-name').value.trim()||'New group';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-sub');
    toast('Group created ✓','ok');loadSubs();
  }catch(e){toast('Could not create group','err')}
}
async function deleteSub(sub_id){
  if(!confirm('Delete this group? Its configs will not be deleted.'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('Group deleted ✓','ok');loadSubs();loadLinks();}catch(e){toast('Error','err')}
}
let lmodalLinks=[],lmodalInSub=new Set();
async function openSubLinks(sub_id,name){
  currentSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name;
  document.getElementById('modal-links-body').innerHTML='<div style="color:var(--t3);font-size:12px;padding:20px;text-align:center"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:20px"></i></div>';
  document.getElementById('lmodal-search-inp').value='';
  openModal('modal-links');
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const thisSub=subs.find(s=>s.sub_id===sub_id);
    lmodalInSub=new Set(thisSub?.link_ids||[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('Failed to load','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:30px"><i class="ti ti-link-off"></i><p>No configs yet</p></div>';updateLmodalCount();return}
  body.innerHTML=links.map(l=>{
    const checked=lmodalInSub.has(l.uuid);
    const on=l.active&&!l.expired;
    return `<div tabindex="0" role="button" class="lrow-v2 ${checked?'checked':''}" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}',this)">
      <div tabindex="0" role="button" class="lrow-v2-check"><i class="ti ti-check"></i></div>
      <div tabindex="0" role="button" class="lrow-v2-avatar"><i class="ti ti-key"></i></div>
      <div tabindex="0" role="button" class="lrow-v2-info">
        <div tabindex="0" role="button" class="lrow-v2-name">${esc(l.label)}</div>
        <div tabindex="0" role="button" class="lrow-v2-meta"><i class="ti ti-database" style="font-size:10px"></i> ${fmtB(l.used_bytes)}</div>
      </div>
      <span tabindex="0" role="button" class="lrow-v2-status ${on?'on':'off'}">${on?'Active':'Disabled'}</span>
    </div>`;
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('checked')}
  else{lmodalInSub.add(uuid);el.classList.add('checked')}
  updateLmodalCount();
}
function lmodalSelectAll(state){
  lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});
  renderLmodalList(lmodalLinks);
}
function updateLmodalCount(){
  const el=document.getElementById('lmodal-count');
  if(el)el.textContent=toFa(lmodalInSub.size)+' selected';
}
function filterLmodal(q){
  q=q.trim().toLowerCase();
  document.querySelectorAll('#modal-links-body .lrow-v2').forEach(row=>{
    row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none';
  });
}
async function saveSubLinks(){
  if(!currentSubId)return;
  const link_ids=[...lmodalInSub];
  try{
    const r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});
    if(!r.ok)throw new Error();
    await Promise.all(lmodalLinks.map(l=>
      authF('/api/links/'+l.uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub_id:lmodalInSub.has(l.uuid)?currentSubId:null})})
    ));
    closeModal('modal-links');
    toast('Group configs saved ✓','ok');
    loadSubs();loadLinks();
  }catch(e){toast('Could not save','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>No groups yet</p></div>';return}
    el.innerHTML=subs.map(s=>`
      <div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div>
          <div style="font-weight:700;font-size:13px;margin-bottom:3px">${esc(s.name)}</div>
          <div style="font-family:ui-monospace,monospace;font-size:10px;color:var(--purple)">${esc(s.sub_url)}</div>
          <div style="font-size:10px;color:var(--t3);margin-top:3px">${toFa(s.links_count)} configs · ${esc(s.total_used_fmt)} used ${s.has_password?'· 🔒 Password protected':''}</div>
        </div>
        <div style="display:flex;gap:5px;flex-wrap:wrap">
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('Copied','ok'))"><i class="ti ti-copy"></i> Sub</button>
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('Copied','ok'))"><i class="ti ti-globe"></i> Public</button>
          <button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        </div>
      </div>
    `).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('Copied ✓','ok'))}
function parseBytesFmt(s){
  if(!s)return 0;
  const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  const n=parseFloat(m[1]),u=m[2].toUpperCase();
  const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};
  return n*(mult[u]||1);
}
async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' connections';
    document.getElementById('ch-count').textContent=toFa(d.count);
    const conns=d.connections||[];
    if(!d.count){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    const uniqIps=new Set(conns.map(c=>c.ip)).size;
    document.getElementById('ch-uniq').textContent=toFa(uniqIps);
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+'s':avgSec<3600?Math.floor(avgSec/60)+'m':Math.floor(avgSec/3600)+'h';
    const maxDur=Math.max(...durs,1);
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+'s':secs<3600?Math.floor(secs/60)+'m':Math.floor(secs/3600)+'h';
      const durPct=Math.min(100,Math.round((secs/maxDur)*100));
      const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-glow"></div>
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div class="conn-card-v2-id">
            <div class="conn-ip-v2">${esc(c.ip)}
              <button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP Copied','ok'))" title="Copy IP"><i class="ti ti-copy"></i></button>
            </div>
            <div class="conn-label-v2">${esc(c.label)}</div>
          </div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> Live</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div class="conn-proto-row">${protoBadge(protoVal)}</div>
          <div class="conn-stat-row">
            <div class="conn-stat-box">
              <div class="conn-stat-icon"><i class="ti ti-transfer"></i></div>
              <div>
                <div class="conn-stat-text-label">Traffic</div>
                <div class="conn-stat-text-val">${esc(c.bytes_fmt)}</div>
              </div>
            </div>
            <div class="conn-stat-box">
              <div class="conn-stat-icon time"><i class="ti ti-clock"></i></div>
              <div>
                <div class="conn-stat-text-label">Session length</div>
                <div class="conn-stat-text-val">${dur}</div>
              </div>
            </div>
          </div>
          <div class="conn-duration-track"><div class="conn-duration-fill" style="width:${durPct}%"></div></div>
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
async function fetchDefaultVless(){
  try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'No configs yet';}catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('Copied ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('Refreshed','ok')}
async function changePw(){
  const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
  if(!cur||!nw||!cf){toast('Fill in all fields','err');return}
  if(nw.length<4){toast('At least 4 characters','err');return}
  if(nw!==cf){toast('Passwords do not match','err');return}
  try{
    const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'Error');
    toast('Password updated ✓','ok');
    ['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');
  }catch(e){toast('✗ '+e.message,'err')}
}
function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}
function checkPwStrength(val){
  const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
  const label=document.getElementById('pw-strength-label');
  const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');
  const hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;
  reqLen.classList.toggle('met',hasLen);
  reqNum.classList.toggle('met',hasNum);
  reqCase.classList.toggle('met',hasCase);
  let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;
  const colors=[cv('--red'),cv('--amber'),cv('--accent'),cv('--green')],labels=['Very weak','Weak','Fair','Strong'];
  segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:cv('--bg3')});
  if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> Password strength';return}
  label.innerHTML=`<i class="ti ti-shield-check" style="color:${colors[Math.max(0,score-1)]}"></i> ${labels[Math.max(0,score-1)]}`;
}
function makeGradient(ctx,color1,color2){
  const g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function cv(n){return getComputedStyle(document.documentElement).getPropertyValue(n).trim()}
function hexA(h,a){h=h.replace('#','');return 'rgba('+parseInt(h.slice(0,2),16)+','+parseInt(h.slice(2,4),16)+','+parseInt(h.slice(4,6),16)+','+a+')'}
function restyleCharts(){
  const a=cv('--accent'),t3=cv('--t3'),bd=cv('--card-b');
  [typeof ch1!=='undefined'?ch1:null,typeof ch3!=='undefined'?ch3:null].forEach(c=>{
    if(!c)return;
    const o=c.options;
    o.scales.x.ticks.color=t3;o.scales.y.ticks.color=t3;o.scales.y.grid.color=bd;
    const tp=o.plugins.tooltip;tp.backgroundColor=cv('--card');tp.borderColor=bd;tp.titleColor=cv('--t1');tp.bodyColor=cv('--t2');
    const d=c.data.datasets[0];d.borderColor=a;
    const g=c.ctx.createLinearGradient(0,0,0,c.height||300);g.addColorStop(0,hexA(a,.4));g.addColorStop(1,hexA(a,0));d.backgroundColor=g;
    if(c.data.datasets[1])c.data.datasets[1].borderColor=cv('--amber');
    c.update('none');
  });
  if(typeof ch2!=='undefined'&&ch2){
    const d=ch2.data.datasets[0];d.backgroundColor=[a,cv('--purple'),cv('--amber')];d.borderColor=cv('--card');
    ch2.options.plugins.legend.labels.color=cv('--t2');ch2.update('none');
  }
}
function initCharts(){
  const c1=document.getElementById('ch1').getContext('2d');
  const grad1=makeGradient(c1,hexA(cv('--accent'),.4),hexA(cv('--accent'),0));
  const opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:cv('--card'),borderColor:cv('--card-b'),borderWidth:1,
        titleColor:cv('--t1'),bodyColor:cv('--t2'),padding:11,cornerRadius:10,displayColors:false,
        titleFont:{family:'system-ui',size:11,weight:'700'},bodyFont:{family:'system-ui',size:11},
        callbacks:{label:v=>`${v.parsed.y.toFixed(2)} MB`}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:cv('--t3'),font:{size:9,family:'system-ui'}}},
      y:{grid:{color:cv('--card-b')},border:{display:false},ticks:{color:cv('--t3'),font:{size:9,family:'system-ui'},callback:v=>v+' MB'}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  const ds1={label:'MB',data:[],borderColor:cv('--accent'),backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:cv('--accent'),pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});

  function makeGradientV2(ctx,c1,c2,c3){
    const g=ctx.createLinearGradient(0,0,0,320);
    g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);
    return g;
  }
  const c3ctx=document.getElementById('ch3').getContext('2d');
  const gradFill3=makeGradientV2(c3ctx,hexA(cv('--accent'),.4),hexA(cv('--accent'),.08),hexA(cv('--accent'),0));
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'Usage',data:[],borderColor:cv('--accent'),backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:cv('--accent'),pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'Average',data:[],borderColor:cv('--amber'),borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:cv('--card'),borderColor:cv('--card-b'),borderWidth:1,
          titleColor:cv('--t1'),bodyColor:cv('--t2'),padding:13,cornerRadius:12,displayColors:true,boxPadding:4,
          titleFont:{family:'system-ui',size:11.5,weight:'700'},bodyFont:{family:'system-ui',size:11},
          callbacks:{label:v=>` ${v.dataset.label}: ${v.parsed.y.toFixed(2)} MB`}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:cv('--t3'),font:{size:9.5,family:'system-ui'},maxRotation:0}},
        y:{grid:{color:cv('--card-b')},border:{display:false},ticks:{color:cv('--t3'),font:{size:9.5,family:'system-ui'},callback:v=>v+' MB'}}
      }
    }
  });

  ch2=new Chart(document.getElementById('ch2'),{
    type:'doughnut',
    data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{
      data:[55,35,10],
      backgroundColor:[cv('--accent'),cv('--purple'),cv('--amber')],
      borderColor:getComputedStyle(document.documentElement).getPropertyValue('--card')||'#0f1923',
      borderWidth:4,hoverOffset:10,borderRadius:6,spacing:3
    }]},
    options:{
      responsive:true,maintainAspectRatio:false,cutout:'72%',
      plugins:{
        legend:{position:'bottom',labels:{color:cv('--t2'),font:{size:10,family:'system-ui'},padding:12,usePointStyle:true,pointStyle:'circle'}},
        tooltip:{backgroundColor:cv('--card'),borderColor:cv('--card-b'),borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'system-ui'},titleFont:{family:'system-ui'}}
      }
    }
  });
}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'var(--green-t)',err:'var(--red-t)',info:'var(--t2)',sent:'var(--amber-t)'};p.style.color=colors[c]||'var(--t1)';p.textContent='['+new Date().toLocaleTimeString('en-US')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('Enter a UUID','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','Connecting: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ Connected - valid UUID');ws.onerror=()=>wsLog('err','✗ Error - invalid or disabled UUID');ws.onmessage=m=>wsLog('info','Received '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','Disconnected ('+e.code+')'+(e.code===1008?' - Access denied':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','Sent: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
document.addEventListener('DOMContentLoaded',async()=>{
  await checkAuth();
  initCharts();
  document.getElementById('set-host').textContent=location.host;
  document.getElementById('sub-all-url')&&(document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all');
  fetchStats();fetchDefaultVless();loadLinks();loadSubs();
  setInterval(fetchStats,4000);
  setInterval(()=>{
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();
    if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
  },5000);
});

document.addEventListener('keydown',e=>{
  if((e.key==='Enter'||e.key===' ')&&e.target.matches&&e.target.matches('.nav-it,.chip,.proto-card,.lrow-v2,.cfg-uuid-mini,.traf-range-tab')){e.preventDefault();e.target.click()}
});
</script>
</body></html>"""

NOT_FOUND_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="dark light"><title>Group not found · Lumen Gate</title>
<style>
:root{color-scheme:dark light}
body{margin:0;min-height:100vh;display:grid;place-items:center;padding:24px;font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:#080f17;color:#e8eff5;text-align:center}
@media(prefers-color-scheme:light){body{background:#f2f5f7;color:#0b1620}p{color:#4b5b6a!important}}
h1{font-size:24px;letter-spacing:-.02em;margin:18px 0 6px}p{margin:0;color:#9db0c0;max-width:34ch}
svg{width:48px;height:48px}
</style></head><body><main><svg viewBox="0 0 32 32" role="img" aria-label="Lumen Gate"><defs><linearGradient id="lgN" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:#2dd4bf"/><stop offset="1" style="stop-color:#2563c9"/></linearGradient></defs><rect width="32" height="32" rx="9" fill="url(#lgN)"/><path d="M6 17h5l3-8 4 14 3-6h5" fill="none" stroke="#04201c" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
<h1>Group not found</h1><p>This link is invalid or the group has been removed. Check the address and try again.</p></main></body></html>"""

def get_public_page_html(uuid_key: str) -> str:
    """Public subscription page: hidden config links with a reveal button and a dedicated password screen."""
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="dark light">
<title>Subscription · Lumen Gate</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%2032%2032%22%3E%3Cdefs%3E%3ClinearGradient%20id%3D%22g%22%20x1%3D%220%22%20y1%3D%220%22%20x2%3D%221%22%20y2%3D%221%22%3E%3Cstop%20offset%3D%220%22%20stop-color%3D%22%232dd4bf%22/%3E%3Cstop%20offset%3D%221%22%20stop-color%3D%22%232563c9%22/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect%20width%3D%2232%22%20height%3D%2232%22%20rx%3D%229%22%20fill%3D%22url%28%23g%29%22/%3E%3Cpath%20d%3D%22M6%2017h5l3-8%204%2014%203-6h5%22%20fill%3D%22none%22%20stroke%3D%22%2304201c%22%20stroke-width%3D%222.6%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22/%3E%3C/svg%3E">
<script>try{{document.documentElement.setAttribute('data-theme',localStorage.getItem('gateway-pub-theme')==='light'?'light':'dark')}}catch(e){{}}</script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
/* Lumen Gate — public subscription page */
:root{{
  color-scheme:dark;
  --bg:#080f17;--bg2:#0c1520;--bg3:#15212d;
  --card:#0f1923;--card-b:#233443;--card-bh:#35506a;
  --t1:#e8eff5;--t2:#9db0c0;--t3:#6b8093;
  --accent:#2dd4bf;--accent2:#5eead4;--accent-d:rgba(45,212,191,.12);--on-accent:#04201c;
  --green:#4ade80;--green-t:#4ade80;--green-bg:rgba(74,222,128,.12);
  --red:#f87171;--red-t:#f87171;--red-bg:rgba(248,113,113,.12);
  --amber:#fbbf24;--amber-bg:rgba(251,191,36,.12);--amber-t:#fbbf24;
  --purple:#7aa7f5;--purple-bg:rgba(122,167,245,.13);--purple-t:#7aa7f5;
  --shadow:0 12px 40px -12px rgba(0,0,0,.7);--field:rgba(0,0,0,.22);--scrim:rgba(3,8,13,.72);
  --ring:0 0 0 3px rgba(45,212,191,.32);
  --font:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --serif:var(--font);--radius:16px;--ease:cubic-bezier(.2,.8,.2,1);
}}
[data-theme="light"]{{
  color-scheme:light;
  --bg:#f2f5f7;--bg2:#ffffff;--bg3:#e9eef2;
  --card:#ffffff;--card-b:#dbe2e9;--card-bh:#b7c4d1;
  --t1:#0b1620;--t2:#4b5b6a;--t3:#7a8896;
  --accent:#0b8f84;--accent2:#097a71;--accent-d:#dcf3f0;--on-accent:#ffffff;
  --green:#138a55;--green-t:#0f7547;--green-bg:#dcf3e6;
  --red:#d43b3b;--red-t:#b92f2f;--red-bg:#fbe3e3;
  --amber:#b36a00;--amber-bg:#fbefd5;--amber-t:#935700;
  --purple:#2563c9;--purple-bg:#e0eafb;--purple-t:#2563c9;
  --shadow:0 12px 36px -12px rgba(11,22,32,.2);--field:#f6f8fa;--scrim:rgba(11,22,32,.5);
  --ring:0 0 0 3px rgba(11,143,132,.3);
}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--font);color:var(--t1);font-size:14px;line-height:1.5;-webkit-font-smoothing:antialiased;transition:background .25s,color .25s}}
button,input{{font:inherit;color:inherit}}
button{{cursor:pointer}}
:focus-visible{{outline:none;box-shadow:var(--ring)}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(60% 40% at 50% -5%,var(--accent-d),transparent 70%);z-index:0;pointer-events:none}}
.grid-fx{{display:none}}
.wrap{{position:relative;z-index:10;max-width:760px;margin:0 auto;padding:calc(24px + env(safe-area-inset-top,0px)) 16px calc(64px + env(safe-area-inset-bottom,0px))}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:28px;gap:10px}}
.brand{{display:flex;align-items:center;gap:10px;min-width:0}}
.brand-img{{display:flex;flex-shrink:0}}.brand-img svg{{width:34px;height:34px}}
.brand-name{{font-size:15px;font-weight:650;letter-spacing:-.01em}}
.brand-sub{{font-size:11px;color:var(--t3)}}
.top-actions{{display:flex;align-items:center;gap:6px;flex-shrink:0}}
.icon-btn{{width:36px;height:36px;border-radius:var(--r-md,12px);background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:17px;transition:.15s}}
.icon-btn:hover{{background:var(--bg3);color:var(--t1)}}

.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:24px;margin-bottom:16px;box-shadow:var(--shadow);border-top:3px solid var(--accent)}}
.sub-eyebrow{{font-size:12.5px;font-weight:600;color:var(--accent2);margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-eyebrow i{{font-size:15px}}
.sub-name{{font-size:26px;font-weight:700;margin-bottom:6px;letter-spacing:-.03em;line-height:1.15}}
.sub-desc{{font-size:14px;color:var(--t2);line-height:1.7;margin-bottom:14px}}
.sub-meta-row{{font-size:12px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.sub-sub-box{{background:var(--bg2);border:1px solid var(--card-b);border-radius:12px;padding:10px 12px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}}
.sub-sub-url{{font-family:var(--mono);font-size:12px;color:var(--t2);word-break:break-all;flex:1;min-width:140px}}

.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px}}
.stat-card{{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:16px;transition:border-color .2s}}
.stat-card:hover{{border-color:var(--card-bh)}}
.stat-label{{font-size:12.5px;color:var(--t2);margin-bottom:8px;font-weight:550}}
.stat-val{{font-size:24px;font-weight:700;line-height:1;letter-spacing:-.03em;font-variant-numeric:tabular-nums}}
.stat-sub{{font-size:12px;color:var(--t3);margin-top:8px}}

.copy-all-bar{{display:flex;align-items:center;gap:12px;background:var(--accent);color:var(--on-accent);border-radius:var(--radius);padding:16px 18px;margin-bottom:20px;flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:15px;font-weight:650;display:flex;align-items:center;gap:8px}}
.copy-all-sub{{font-size:12.5px;opacity:.8;margin-top:2px}}
.copy-all-btn{{background:var(--on-accent);color:var(--accent);border:0;border-radius:12px;height:38px;padding:0 18px;font-size:13.5px;font-weight:650;display:flex;align-items:center;gap:6px;transition:transform .12s,filter .15s}}
[data-theme="light"] .copy-all-btn{{background:#fff;color:var(--accent2)}}
.copy-all-btn:hover{{filter:brightness(1.1)}}.copy-all-btn:active{{transform:scale(.97)}}

.cfg-title{{font-size:15px;font-weight:650;margin-bottom:12px;display:flex;align-items:center;gap:8px}}
.cfg-title i{{color:var(--accent);font-size:18px}}
.cfg-grid{{display:grid;gap:14px}}
/* Config card: a "pass" with a perforated tear line between usage and link */
.cfg-card{{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);transition:border-color .2s,box-shadow .2s;position:relative;overflow:hidden}}
.cfg-card:hover{{border-color:var(--card-bh);box-shadow:var(--shadow)}}
.cfg-top{{padding:18px 20px 16px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;left:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:16px;font-weight:650;letter-spacing:-.01em}}
.cfg-badges{{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}}
.proto-chip{{font-size:11px;padding:2px 9px;border-radius:7px;font-weight:600;display:inline-flex;align-items:center;gap:4px}}
.pc-ws{{background:var(--accent-d);color:var(--accent2)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:6px;font-size:12px;font-weight:600;padding:3px 10px;border-radius:99px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:6px;border-radius:99px;background:var(--bg3);overflow:hidden;margin-bottom:6px}}
.ubar-f{{height:100%;border-radius:99px;transition:width .6s var(--ease)}}
.utxt{{font-size:12px;color:var(--t3);display:flex;justify-content:space-between}}
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 20px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{left:-30px}}.cfg-tear::after{{right:-30px}}
.cfg-bottom{{padding:14px 20px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px solid var(--card-b);border-radius:12px;padding:10px 14px;color:var(--t2);font-size:13px;font-weight:550;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--bg3);color:var(--t1)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:8px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s var(--ease)}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{margin-top:10px;background:var(--field);border:1px solid var(--card-b);border-radius:12px;padding:12px 14px;font-size:11.5px;font-family:var(--mono);color:var(--accent2);word-break:break-all;line-height:1.7}}
.cfg-actions{{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:6px;height:34px;padding:0 14px;border-radius:12px;border:1px solid transparent;font-size:13px;font-weight:600;white-space:nowrap;transition:background .15s,filter .15s,transform .12s}}
.btn i{{font-size:15px}}.btn:active{{transform:scale(.97)}}.btn:disabled{{opacity:.5;cursor:not-allowed}}
.btn-p{{background:var(--accent);color:var(--on-accent)}}.btn-p:hover{{filter:brightness(1.1)}}
.btn-g{{background:var(--accent-d);color:var(--accent2)}}.btn-g:hover{{filter:brightness(1.15)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t)}}.btn-pur:hover{{filter:brightness(1.15)}}
.conn-chip{{display:inline-flex;align-items:center;gap:6px;font-size:12px;padding:2px 10px;border-radius:99px;background:var(--green-bg);color:var(--green-t);font-weight:600}}
.dot{{width:7px;height:7px;border-radius:50%;background:var(--green);color:var(--green);display:inline-block;animation:ring 2s infinite}}
@keyframes ring{{0%{{box-shadow:0 0 0 0 currentColor}}70%,100%{{box-shadow:0 0 0 6px transparent}}}}

/* Locked (password-protected) state */
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:76vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-b);border-radius:24px;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden}}
.lock-banner{{padding:36px 28px 22px;border-bottom:1px solid var(--card-b)}}
.lock-shield{{width:60px;height:60px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-7px;border-radius:24px;border:1px solid var(--accent);opacity:.35;animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.4}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:28px;color:var(--accent)}}
.lock-title{{font-size:20px;font-weight:700;margin-bottom:6px;letter-spacing:-.02em}}
.lock-sub{{font-size:13.5px;color:var(--t2);line-height:1.6}}
.lock-form{{padding:22px 28px 28px}}
.lock-field{{position:relative;margin-bottom:12px}}
.lock-inp{{width:100%;height:46px;padding:0 44px;border-radius:12px;border:1px solid var(--card-b);background:var(--field);color:var(--t1);font-size:15px;outline:none;text-align:center;transition:border-color .15s,box-shadow .15s}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:var(--ring)}}
.lock-eye{{position:absolute;right:8px;top:50%;transform:translateY(-50%);width:32px;height:32px;background:none;border:0;border-radius:8px;color:var(--t3);font-size:17px;display:flex;align-items:center;justify-content:center}}
.lock-eye:hover{{color:var(--t1);background:var(--bg3)}}
.lock-lockicon{{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:16px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:13px;margin-bottom:10px;min-height:18px;display:flex;align-items:center;justify-content:center;gap:6px}}
.lock-btn{{width:100%;height:44px;font-size:14px;border-radius:12px}}
.lock-footer{{padding:14px 28px;border-top:1px solid var(--card-b);font-size:12px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}
.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}

.toast{{position:fixed;bottom:calc(22px + env(safe-area-inset-bottom,0px));left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);border-left:3px solid var(--accent);color:var(--t1);border-radius:12px;padding:11px 18px;font-size:13.5px;opacity:0;transition:opacity .25s,transform .25s var(--ease);z-index:900;box-shadow:var(--shadow);pointer-events:none;max-width:calc(100vw - 32px)}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-left-color:var(--green)}}
.qr-modal{{display:none;position:fixed;inset:0;background:var(--scrim);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:24px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}}
.qr-title{{font-size:15px;font-weight:650;margin-bottom:16px}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:16px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:14px}}
.footer{{text-align:center;padding-top:32px;font-size:12px;color:var(--t3)}}
.footer a{{color:var(--accent2);font-weight:600}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;transition:none!important}}}}
@media(max-width:520px){{
  .stats-bar{{grid-template-columns:1fr 1fr}}
  .stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}
  .sub-name{{font-size:21px}}
  .copy-all-bar{{flex-direction:column;align-items:stretch}}
  .copy-all-btn{{justify-content:center}}
  .wrap{{padding-left:12px;padding-right:12px}}
  .lock-banner{{padding:30px 20px 20px}}.lock-form{{padding:20px 20px 24px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
</style>
</head>
<body>
<div class="bg-fx"></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> Close</button>
  </div>
</div>
<main class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-img"><svg viewBox="0 0 32 32" role="img" aria-label="Lumen Gate"><defs><linearGradient id="lgP" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--accent)"/><stop offset="1" style="stop-color:var(--purple)"/></linearGradient></defs><rect width="32" height="32" rx="9" fill="url(#lgP)"/><path d="M6 17h5l3-8 4 14 3-6h5" fill="none" stroke="var(--on-accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div><div class="brand-name">Lumen Gate</div><div class="brand-sub">v11</div></div>
    </div>
    <div class="top-actions">
      <button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="Toggle theme" aria-label="Toggle theme"><i class="ti ti-sun" id="theme-icon"></i></button>
      
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>Loading...</div>
  </div>
  <footer class="footer">Lumen Gate v11</footer>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

let isDark=localStorage.getItem('gateway-pub-theme')!=='light';
function applyTheme(dark){{
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');
}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('gateway-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);

function toast(msg,type=''){{
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n)}}
function protoChip(p){{
  if(p==='xhttp-stream-one')return '<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';
  if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';
  return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}}

function showQR(label,link){{
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}}

function toggleLink(i){{
  const wrap=document.getElementById('vw-'+i);
  const btn=document.getElementById('vt-'+i);
  const open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? 'Hide link' : 'Show config link';
}}

async function loadData(pw=''){{
  const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  const r=await fetch(url);
  return r.json();
}}

function renderLock(name,errMsg=''){{
  document.getElementById('root').innerHTML=`
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${{esc(name)}}</div>
          <div class="lock-sub">This group is password protected. Enter the password to view its configs.</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> Unlock group</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> Your connection is encrypted</div>
      </div>
    </div>
  `;
  const inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});
}}

function togglePwVis(){{
  const inp=document.getElementById('lock-pw');
  const icon=document.getElementById('lock-eye-icon');
  const toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}}

async function submitLock(){{
  const pw=document.getElementById('lock-pw').value;
  const data=await loadData(pw);
  if(data.locked){{renderLock(data.name,'Incorrect password');return}}
  savedPw=pw;
  renderContent(data);
}}

function renderContent(d){{
  const activeCount=d.links.filter(l=>l.active).length;
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/sub-group/' + UUID_KEY);
  const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');

  window._subUrl  = subUrl;
  window._subName = d.name;
  window._links   = d.links.map(l => ({{
    vless : l.vless_link,
    sub   : l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),
    label : l.label,
  }}));

  document.getElementById('root').innerHTML=`
    <div class="sub-info">
      <div class="sub-eyebrow"><i class="ti ti-folders"></i> Access group</div>
      <div class="sub-name">${{esc(d.name)}}</div>
      ${{d.desc ? `<div class="sub-desc">${{esc(d.desc)}}</div>` : ''}}
      <div class="sub-meta-row"><i class="ti ti-clock"></i> Last updated: ${{new Date().toLocaleTimeString('en-US')}}</div>
      <div class="sub-sub-box">
        <span class="sub-sub-url">${{esc(subUrl)}}</span>
        <button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px"
          onclick="navigator.clipboard.writeText(window._subUrl).then(()=>toast('Sub link copied ✓','ok'))">
          <i class="ti ti-copy"></i> Copy sub link
        </button>
        <button class="btn btn-g" style="padding:7px 12px;font-size:10.5px"
          onclick="showQR(window._subName + ' — Entire group', window._subUrl)">
          <i class="ti ti-qrcode"></i> Group QR
        </button>
      </div>
    </div>

    <div class="copy-all-bar">
      <div class="copy-all-text">
        <div class="copy-all-title"><i class="ti ti-copy"></i> Copy all configs</div>
        <div class="copy-all-sub">Copy every active link in this group at once</div>
      </div>
      <button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> Copy all (${{toFa(activeCount)}})</button>
    </div>

    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-label">Active configs</div>
        <div class="stat-val">${{toFa(activeCount)}}</div>
        <div class="stat-sub">of ${{toFa(d.links.length)}} configs</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Live connections</div>
        <div class="stat-val">${{toFa(d.active_connections)}}</div>
        <div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:4px"><span class="dot"></span> Online</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Total usage</div>
        <div class="stat-val" style="font-size:17px;margin-top:3px">${{esc(d.total_used_fmt)}}</div>
        <div class="stat-sub">All configs</div>
      </div>
    </div>

    <div class="cfg-title"><i class="ti ti-link"></i> Configs (${{toFa(d.links.length)}} items)</div>
    <div class="cfg-grid">
      ${{d.links.map((l, i) => {{
        const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
        const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
        const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
        return `
          <div class="cfg-card${{l.active ? '' : ' inactive'}}">
            <div class="cfg-top">
              <div class="cfg-head">
                <div>
                  <div class="cfg-label">${{esc(l.label)}}</div>
                  <div class="cfg-badges">
                    ${{protoChip(l.protocol)}}
                    ${{l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} connections</span>` : ''}}
                  </div>
                </div>
                <span class="cfg-status ${{l.active ? 'ok' : 'no'}}">${{l.active ? '<i class="ti ti-circle-check"></i> Active' : '<i class="ti ti-circle-x"></i> Disabled'}}</span>
              </div>
              <div class="cfg-usage">
                <div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div>
                <div class="utxt"><span>${{esc(l.used_fmt)}} used</span><span>Quota: ${{lim}}</span></div>
              </div>
            </div>
            <div class="cfg-tear"></div>
            <div class="cfg-bottom">
              <button class="cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})">
                <span class="ltl"><i class="ti ti-eye"></i> <span>Show config link</span></span>
                <i class="ti ti-chevron-down"></i>
              </button>
              <div class="cfg-vless-wrap" id="vw-${{i}}">
                <div class="cfg-vless-inner">
                  <div class="cfg-vless">${{esc(l.vless_link)}}</div>
                </div>
              </div>
              <div class="cfg-actions">
                <button class="btn btn-p"
                  onclick="navigator.clipboard.writeText(window._links[${{i}}].vless).then(()=>toast('Link copied ✓','ok'))">
                  <i class="ti ti-copy"></i> Copy link
                </button>
                <button class="btn btn-g"
                  onclick="showQR(window._links[${{i}}].label, window._links[${{i}}].vless)">
                  <i class="ti ti-qrcode"></i> QR
                </button>
              </div>
            </div>
          </div>
        `;
      }}).join('')}}
    </div>
  `;
  setTimeout(() => autoRefresh(), 30000);
}}

function copyAllConfigs(){{
  const links=window._links||[];
  if(!links.length){{toast('No configs to copy','');return}}
  const text=links.map(l=>l.vless).join('\\n');
  navigator.clipboard.writeText(text).then(()=>toast('All '+toFa(links.length)+' configs copied ✓','ok'));
}}

async function autoRefresh(){{
  try{{
    const data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  }} catch(e) {{}}
}}

async function init(){{
  try{{
    const data = await loadData();
    if (data.locked) {{ renderLock(data.name); return; }}
    renderContent(data);
  }} catch(e) {{
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>Failed to load</div>';
  }}
}}

init();
</script>
</body></html>"""
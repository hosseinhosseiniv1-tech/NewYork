# pages.py — Gateway v12
# Full template set for login, dashboard, and public sub page.
# All strings and identifiers are in English.

LOGO_B64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="

_COMMON_CSS = r"""
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --c-indigo-300:#8E8EF8;--c-indigo-400:#7070F5;--c-indigo-500:#5B5BF7;
  --c-indigo-600:#4949E8;--c-indigo-700:#3838C9;
  --c-coral-500:#FF6B4A;--c-coral-600:#F05334;
  --c-emerald-400:#34D399;--c-emerald-500:#10B981;--c-emerald-600:#059669;
  --c-amber-400:#FBBF24;--c-amber-500:#F59E0B;--c-amber-600:#D97706;
  --c-rose-400:#FB7185;--c-rose-500:#F43F5E;--c-rose-600:#E11D48;
  --c-sky-400:#38BDF8;--c-sky-500:#0EA5E9;--c-sky-600:#0284C7;
  --font-sans:'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  --font-mono:'Geist Mono',ui-monospace,'SF Mono',monospace;
  --sp-1:4px;--sp-2:8px;--sp-3:12px;--sp-4:16px;--sp-5:20px;--sp-6:24px;
  --sp-8:32px;--sp-10:40px;--sp-12:48px;--sp-16:64px;
  --r-xs:4px;--r-sm:6px;--r-md:10px;--r-lg:14px;--r-xl:20px;--r-full:999px;
  --ease:cubic-bezier(.2,.8,.2,1);
  --dur-1:120ms;--dur-2:180ms;--dur-3:240ms;
  --fs-11:11px;--fs-12:12px;--fs-13:13px;--fs-14:14px;--fs-15:15px;
  --fs-17:17px;--fs-20:20px;--fs-24:24px;--fs-30:30px;--fs-36:36px;
}
[data-theme="dark"]{
  --bg-0:#0A0A0F;--bg-1:#0F1016;--bg-2:#15161E;--bg-3:#1B1D28;--bg-4:#23242F;
  --bg-hover:#1E2029;
  --fg-0:#F4F5F7;--fg-1:#C8CBD4;--fg-2:#8B8FA1;--fg-3:#5C6072;--fg-4:#3A3D4B;
  --line-1:rgba(255,255,255,.06);--line-2:rgba(255,255,255,.10);--line-3:rgba(255,255,255,.16);
  --brand:var(--c-indigo-400);--brand-hi:var(--c-indigo-300);
  --brand-lo:rgba(112,112,245,.14);--brand-line:rgba(112,112,245,.30);
  --ok-bg:rgba(52,211,153,.10);--ok-fg:var(--c-emerald-400);--ok-line:rgba(52,211,153,.22);
  --warn-bg:rgba(251,191,36,.10);--warn-fg:var(--c-amber-400);--warn-line:rgba(251,191,36,.22);
  --err-bg:rgba(251,113,133,.10);--err-fg:var(--c-rose-400);--err-line:rgba(251,113,133,.22);
  --info-bg:rgba(56,189,248,.10);--info-fg:var(--c-sky-400);--info-line:rgba(56,189,248,.22);
  --shadow-1:0 1px 2px rgba(0,0,0,.4);
  --shadow-2:0 4px 12px rgba(0,0,0,.35);
  --shadow-3:0 12px 32px rgba(0,0,0,.5);
  --shadow-glow:0 0 0 1px var(--brand-line),0 8px 24px rgba(91,91,247,.22);
}
[data-theme="light"]{
  --bg-0:#FAFAF7;--bg-1:#FFFFFF;--bg-2:#F4F4F0;--bg-3:#EAEAE3;--bg-4:#E0E0D9;
  --bg-hover:#F0F0EB;
  --fg-0:#16161C;--fg-1:#3A3D47;--fg-2:#6B6E7B;--fg-3:#989BA9;--fg-4:#C7C9D2;
  --line-1:rgba(20,20,30,.06);--line-2:rgba(20,20,30,.10);--line-3:rgba(20,20,30,.18);
  --brand:var(--c-indigo-600);--brand-hi:var(--c-indigo-700);
  --brand-lo:rgba(73,73,232,.10);--brand-line:rgba(73,73,232,.28);
  --ok-bg:rgba(5,150,105,.10);--ok-fg:var(--c-emerald-600);--ok-line:rgba(5,150,105,.22);
  --warn-bg:rgba(217,119,6,.10);--warn-fg:var(--c-amber-600);--warn-line:rgba(217,119,6,.22);
  --err-bg:rgba(225,29,72,.09);--err-fg:var(--c-rose-600);--err-line:rgba(225,29,72,.22);
  --info-bg:rgba(14,165,233,.09);--info-fg:var(--c-sky-600);--info-line:rgba(14,165,233,.22);
  --shadow-1:0 1px 2px rgba(20,20,30,.06);
  --shadow-2:0 4px 12px rgba(20,20,30,.08);
  --shadow-3:0 12px 32px rgba(20,20,30,.12);
  --shadow-glow:0 0 0 1px var(--brand-line),0 8px 24px rgba(73,73,232,.15);
}
html{color-scheme:dark light}
[data-theme="light"] html{color-scheme:light}
body{
  font-family:var(--font-sans);font-size:var(--fs-14);line-height:1.5;
  color:var(--fg-0);background:var(--bg-0);
  -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;
  transition:background var(--dur-3) var(--ease),color var(--dur-3) var(--ease);
  min-height:100vh;
}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;background:none;border:none;cursor:pointer}
input,select,textarea{font:inherit;color:inherit}
code,.mono{font-family:var(--font-mono);font-feature-settings:"ss01"}
::selection{background:var(--brand-lo);color:var(--fg-0)}
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--line-2);border-radius:var(--r-full);border:2px solid var(--bg-0)}
::-webkit-scrollbar-thumb:hover{background:var(--line-3)}
:focus-visible{outline:2px solid var(--brand);outline-offset:2px}

.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:6px;
  height:34px;padding:0 var(--sp-3);border-radius:var(--r-md);
  font-size:var(--fs-13);font-weight:500;border:1px solid transparent;
  transition:background var(--dur-1) var(--ease),border-color var(--dur-1) var(--ease),
    color var(--dur-1) var(--ease),transform var(--dur-1) var(--ease);
  white-space:nowrap;user-select:none;
}
.btn i{font-size:15px}
.btn-primary{background:var(--brand);color:#fff;box-shadow:0 1px 0 rgba(255,255,255,.12) inset,var(--shadow-1)}
.btn-primary:hover{background:var(--brand-hi)}
.btn-primary:active{transform:translateY(1px)}
.btn-secondary{background:var(--bg-2);color:var(--fg-0);border-color:var(--line-2)}
.btn-secondary:hover{background:var(--bg-3);border-color:var(--line-3)}
.btn-secondary:active{transform:translateY(1px)}
.btn-ghost{background:transparent;color:var(--fg-1)}
.btn-ghost:hover{background:var(--bg-hover);color:var(--fg-0)}
.btn-outline{background:transparent;color:var(--fg-0);border-color:var(--line-2)}
.btn-outline:hover{border-color:var(--line-3);background:var(--bg-hover)}
.btn-danger{background:var(--err-bg);color:var(--err-fg);border-color:var(--err-line)}
.btn-danger:hover{background:rgba(244,63,94,.16)}
.btn-success{background:var(--ok-bg);color:var(--ok-fg);border-color:var(--ok-line)}
.btn-success:hover{background:rgba(52,211,153,.16)}
.btn-sm{height:28px;padding:0 10px;font-size:var(--fs-12);border-radius:var(--r-sm)}
.btn-sm i{font-size:13px}
.btn-lg{height:42px;padding:0 var(--sp-5);font-size:var(--fs-14);border-radius:var(--r-lg)}
.btn-lg i{font-size:17px}
.btn-icon{width:34px;padding:0}
.btn-icon.btn-sm{width:28px}
.btn:disabled,.btn[aria-disabled="true"]{opacity:.45;cursor:not-allowed;pointer-events:none}
.btn.is-loading{pointer-events:none}
.btn.is-loading::before{
  content:'';width:12px;height:12px;border-radius:50%;
  border:2px solid currentColor;border-right-color:transparent;
  animation:spin .7s linear infinite;
}
@keyframes spin{to{transform:rotate(360deg)}}

.field{display:flex;flex-direction:column;gap:6px}
.field-label{font-size:var(--fs-12);font-weight:500;color:var(--fg-1)}
.field-help{font-size:var(--fs-11);color:var(--fg-3)}
.field-error{font-size:var(--fs-11);color:var(--err-fg);display:flex;align-items:center;gap:4px}
.input,.select,.textarea{
  height:34px;padding:0 var(--sp-3);
  background:var(--bg-2);border:1px solid var(--line-2);border-radius:var(--r-md);
  color:var(--fg-0);font-size:var(--fs-13);width:100%;
  transition:border-color var(--dur-1) var(--ease),box-shadow var(--dur-1) var(--ease),
    background var(--dur-1) var(--ease);
}
.textarea{height:auto;padding:var(--sp-2) var(--sp-3);min-height:80px;resize:vertical}
.input::placeholder,.textarea::placeholder{color:var(--fg-3)}
.input:hover,.select:hover,.textarea:hover{border-color:var(--line-3)}
.input:focus,.select:focus,.textarea:focus{
  outline:none;border-color:var(--brand);
  box-shadow:0 0 0 3px var(--brand-lo);background:var(--bg-1);
}
.input:disabled,.select:disabled{opacity:.5;cursor:not-allowed}
.input[aria-invalid="true"]{border-color:var(--err-fg);box-shadow:0 0 0 3px var(--err-bg)}
.input.is-mono{font-family:var(--font-mono);font-size:var(--fs-12)}
.input-wrap{position:relative}
.input-wrap .input{padding-right:34px}
.input-wrap .trail{
  position:absolute;right:4px;top:50%;transform:translateY(-50%);
  width:26px;height:26px;display:flex;align-items:center;justify-content:center;
  color:var(--fg-3);border-radius:var(--r-sm);
  transition:color var(--dur-1) var(--ease),background var(--dur-1) var(--ease);
}
.input-wrap .trail:hover{color:var(--fg-1);background:var(--bg-hover)}
.input-wrap .lead{
  position:absolute;left:10px;top:50%;transform:translateY(-50%);
  color:var(--fg-3);font-size:15px;pointer-events:none;
}
.input-wrap.has-lead .input{padding-left:32px}
.select{
  appearance:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%238B8FA1' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 10px center;padding-right:30px;
}
.search-wrap{position:relative}
.search-wrap i{
  position:absolute;left:10px;top:50%;transform:translateY(-50%);
  color:var(--fg-3);font-size:14px;pointer-events:none;
}
.search-input{
  height:34px;padding:0 var(--sp-3) 0 32px;
  background:var(--bg-2);border:1px solid var(--line-2);border-radius:var(--r-md);
  color:var(--fg-0);font-size:var(--fs-13);width:100%;
  transition:border-color var(--dur-1) var(--ease),box-shadow var(--dur-1) var(--ease);
}
.search-input::placeholder{color:var(--fg-3)}
.search-input:focus{outline:none;border-color:var(--brand);box-shadow:0 0 0 3px var(--brand-lo)}

.checkbox{display:inline-flex;align-items:center;gap:8px;cursor:pointer;user-select:none;font-size:var(--fs-13);color:var(--fg-0)}
.checkbox input{position:absolute;opacity:0;pointer-events:none}
.checkbox .box{
  width:16px;height:16px;border-radius:var(--r-xs);
  border:1.5px solid var(--line-3);background:var(--bg-2);
  display:flex;align-items:center;justify-content:center;
  transition:all var(--dur-1) var(--ease);flex-shrink:0;
}
.checkbox .box i{font-size:11px;color:#fff;opacity:0;transform:scale(.6);transition:all var(--dur-1) var(--ease)}
.checkbox input:checked ~ .box{background:var(--brand);border-color:var(--brand)}
.checkbox input:checked ~ .box i{opacity:1;transform:scale(1)}
.radio{display:inline-flex;align-items:center;gap:8px;cursor:pointer;user-select:none;font-size:var(--fs-13);color:var(--fg-0)}
.radio input{position:absolute;opacity:0;pointer-events:none}
.radio .dot{
  width:16px;height:16px;border-radius:50%;
  border:1.5px solid var(--line-3);background:var(--bg-2);
  display:flex;align-items:center;justify-content:center;
  transition:all var(--dur-1) var(--ease);flex-shrink:0;
}
.radio .dot::after{
  content:'';width:6px;height:6px;border-radius:50%;background:#fff;
  opacity:0;transform:scale(.5);transition:all var(--dur-1) var(--ease);
}
.radio input:checked ~ .dot{background:var(--brand);border-color:var(--brand)}
.radio input:checked ~ .dot::after{opacity:1;transform:scale(1)}
.switch{display:inline-flex;align-items:center;gap:8px;cursor:pointer;user-select:none;font-size:var(--fs-13);color:var(--fg-0)}
.switch input{position:absolute;opacity:0;pointer-events:none}
.switch .track{
  width:32px;height:18px;border-radius:var(--r-full);
  background:var(--bg-3);border:1px solid var(--line-2);
  position:relative;transition:all var(--dur-2) var(--ease);flex-shrink:0;
}
.switch .track::after{
  content:'';position:absolute;top:1px;left:1px;
  width:14px;height:14px;border-radius:50%;background:#fff;
  box-shadow:var(--shadow-1);transition:all var(--dur-2) var(--ease);
}
.switch input:checked ~ .track{background:var(--brand);border-color:var(--brand)}
.switch input:checked ~ .track::after{left:15px}

.chip{
  display:inline-flex;align-items:center;gap:4px;
  height:26px;padding:0 10px;border-radius:var(--r-full);
  background:var(--bg-2);border:1px solid var(--line-2);
  font-size:var(--fs-12);font-weight:500;color:var(--fg-1);
  transition:all var(--dur-1) var(--ease);cursor:pointer;white-space:nowrap;
}
.chip:hover{background:var(--bg-3);color:var(--fg-0)}
.chip.is-active{background:var(--brand);color:#fff;border-color:var(--brand)}
.chip i{font-size:12px}
.chip-sm{height:22px;padding:0 8px;font-size:11px}
.chip-sm i{font-size:11px}
.badge{
  display:inline-flex;align-items:center;gap:4px;
  height:22px;padding:0 8px;border-radius:var(--r-sm);
  font-size:var(--fs-11);font-weight:600;font-family:var(--font-mono);
  white-space:nowrap;
}
.badge.brand{background:var(--brand-lo);color:var(--brand)}
.badge.ok{background:var(--ok-bg);color:var(--ok-fg)}
.badge.warn{background:var(--warn-bg);color:var(--warn-fg)}
.badge.err{background:var(--err-bg);color:var(--err-fg)}
.badge.info{background:var(--info-bg);color:var(--info-fg)}
.badge.neutral{background:var(--bg-3);color:var(--fg-1)}
.dot{width:6px;height:6px;border-radius:2px;display:inline-block;flex-shrink:0}
.dot.ok{background:var(--ok-fg);box-shadow:0 0 0 2px var(--ok-bg)}
.dot.warn{background:var(--warn-fg);box-shadow:0 0 0 2px var(--warn-bg)}
.dot.err{background:var(--err-fg);box-shadow:0 0 0 2px var(--err-bg)}
.dot.info{background:var(--info-fg);box-shadow:0 0 0 2px var(--info-bg)}
.dot.muted{background:var(--fg-4);box-shadow:0 0 0 2px var(--line-1)}
.dot.live::after{content:'';display:block;width:6px;height:6px;border-radius:2px;background:inherit;animation:live 2s ease-in-out infinite}
@keyframes live{0%,100%{opacity:0;transform:scale(1)}50%{opacity:.8;transform:scale(2.2)}}
.status-pill{
  display:inline-flex;align-items:center;gap:5px;
  height:22px;padding:0 8px;border-radius:var(--r-sm);
  font-size:var(--fs-11);font-weight:600;
}
.status-pill.online{background:var(--ok-bg);color:var(--ok-fg)}
.status-pill.offline{background:var(--err-bg);color:var(--err-fg)}
.status-pill.warn{background:var(--warn-bg);color:var(--warn-fg)}

.tabs{display:flex;gap:var(--sp-1);border-bottom:1px solid var(--line-1)}
.tab{
  padding:var(--sp-2) var(--sp-3);font-size:var(--fs-13);font-weight:500;
  color:var(--fg-2);border-bottom:2px solid transparent;margin-bottom:-1px;
  transition:color var(--dur-1) var(--ease),border-color var(--dur-1) var(--ease);
}
.tab:hover{color:var(--fg-0)}
.tab.is-active{color:var(--fg-0);border-bottom-color:var(--brand)}
.segmented{
  display:inline-flex;padding:3px;gap:2px;
  background:var(--bg-2);border:1px solid var(--line-2);border-radius:var(--r-md);
}
.segmented button{
  padding:4px 12px;border-radius:var(--r-sm);font-size:var(--fs-12);font-weight:500;
  color:var(--fg-2);transition:all var(--dur-1) var(--ease);
}
.segmented button:hover{color:var(--fg-0)}
.segmented button.is-active{background:var(--bg-4);color:var(--fg-0);box-shadow:var(--shadow-1)}

.card{
  background:var(--bg-1);border:1px solid var(--line-1);
  border-radius:var(--r-lg);padding:var(--sp-5);
  transition:border-color var(--dur-2) var(--ease),background var(--dur-2) var(--ease);
}
.metric-card{
  background:var(--bg-1);border:1px solid var(--line-1);
  border-radius:var(--r-lg);padding:var(--sp-5);
  display:flex;flex-direction:column;gap:var(--sp-2);
  position:relative;overflow:hidden;
}
.metric-card .label{font-size:var(--fs-12);color:var(--fg-2);font-weight:500;display:flex;align-items:center;gap:6px}
.metric-card .label i{font-size:14px;color:var(--fg-3)}
.metric-card .value{font-size:var(--fs-30);font-weight:600;letter-spacing:-.02em;line-height:1.1}
.metric-card .value .unit{font-size:var(--fs-13);color:var(--fg-2);font-weight:500;margin-left:4px}
.metric-card .meta{font-size:var(--fs-12);color:var(--fg-2);display:flex;align-items:center;gap:6px}
.metric-card .rail{position:absolute;top:0;left:0;width:2px;height:100%;background:var(--brand);opacity:.8}
.metric-card.rail-ok .rail{background:var(--ok-fg)}
.metric-card.rail-warn .rail{background:var(--warn-fg)}
.metric-card.rail-err .rail{background:var(--err-fg)}

.progress{height:5px;background:var(--bg-3);border-radius:var(--r-full);overflow:hidden;position:relative}
.progress .fill{height:100%;background:var(--brand);border-radius:var(--r-full);transition:width var(--dur-3) var(--ease)}
.progress .fill.ok{background:var(--ok-fg)}
.progress .fill.warn{background:var(--warn-fg)}
.progress .fill.err{background:var(--err-fg)}
.progress-meta{display:flex;justify-content:space-between;font-size:var(--fs-11);color:var(--fg-2);margin-top:6px}

.config-card{
  background:var(--bg-1);border:1px solid var(--line-1);border-radius:var(--r-lg);
  overflow:hidden;position:relative;
  transition:border-color var(--dur-2) var(--ease),box-shadow var(--dur-2) var(--ease);
}
.config-card:hover{border-color:var(--line-2);box-shadow:var(--shadow-2)}
.config-card::before{
  content:'';position:absolute;top:0;left:0;bottom:0;width:3px;
  background:var(--ok-fg);opacity:.9;
}
.config-card.is-inactive::before{background:var(--fg-4);opacity:.5}
.config-card.is-expired::before{background:var(--warn-fg);opacity:.7}
.config-body{padding:var(--sp-4) var(--sp-5)}
.config-head{display:flex;align-items:flex-start;justify-content:space-between;gap:var(--sp-3);margin-bottom:var(--sp-3)}
.config-name{font-size:var(--fs-15);font-weight:600;color:var(--fg-0);letter-spacing:-.01em}
.config-uuid{
  font-family:var(--font-mono);font-size:var(--fs-11);color:var(--fg-2);
  margin-top:3px;cursor:pointer;transition:color var(--dur-1) var(--ease);
}
.config-uuid:hover{color:var(--brand)}
.config-tags{display:flex;flex-wrap:wrap;gap:4px;margin-top:var(--sp-2)}
.config-tear{
  height:1px;position:relative;
  background:repeating-linear-gradient(90deg,var(--line-2) 0 4px,transparent 4px 8px);
  margin:0 var(--sp-4);
}
.config-tear::before,.config-tear::after{
  content:'';position:absolute;top:50%;width:12px;height:12px;border-radius:50%;
  background:var(--bg-0);border:1px solid var(--line-1);transform:translateY(-50%);
}
.config-tear::before{left:-7px}
.config-tear::after{right:-7px}
.config-foot{
  padding:var(--sp-3) var(--sp-5);
  display:flex;align-items:center;justify-content:space-between;
  gap:var(--sp-3);flex-wrap:wrap;
}
.config-foot .meta{
  font-family:var(--font-mono);font-size:var(--fs-11);color:var(--fg-2);
  display:flex;align-items:center;gap:var(--sp-3);
}
.config-foot .meta i{font-size:12px;opacity:.7}
.config-actions{display:flex;gap:4px}

.group-card{
  background:var(--bg-1);border:1px solid var(--line-1);border-radius:var(--r-lg);
  padding:var(--sp-5);display:flex;flex-direction:column;gap:var(--sp-3);
  transition:border-color var(--dur-2) var(--ease);
}
.group-card:hover{border-color:var(--line-2)}
.group-head{display:flex;align-items:flex-start;gap:var(--sp-3)}
.group-icon{
  width:36px;height:36px;border-radius:var(--r-md);
  background:var(--brand-lo);color:var(--brand);
  display:flex;align-items:center;justify-content:center;
  font-size:17px;flex-shrink:0;
}
.group-name{font-weight:600;font-size:var(--fs-14)}
.group-desc{font-size:var(--fs-12);color:var(--fg-2);margin-top:2px}
.group-stats{display:flex;gap:var(--sp-4);padding-top:var(--sp-3);border-top:1px solid var(--line-1)}
.group-stat .v{font-size:var(--fs-15);font-weight:600;font-family:var(--font-mono)}
.group-stat .l{font-size:var(--fs-11);color:var(--fg-2)}
.group-url{
  font-family:var(--font-mono);font-size:var(--fs-11);color:var(--fg-2);
  background:var(--bg-2);padding:8px 10px;border-radius:var(--r-sm);
  border:1px solid var(--line-1);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}

.conn-card{background:var(--bg-1);border:1px solid var(--line-1);border-radius:var(--r-lg);padding:var(--sp-4) var(--sp-5)}
.conn-head{display:flex;align-items:center;gap:var(--sp-3)}
.conn-avatar{
  width:34px;height:34px;border-radius:var(--r-md);
  background:var(--ok-bg);color:var(--ok-fg);
  display:flex;align-items:center;justify-content:center;
  font-size:15px;flex-shrink:0;
}
.conn-ip{font-family:var(--font-mono);font-size:var(--fs-13);font-weight:600}
.conn-label{font-size:var(--fs-11);color:var(--fg-2);margin-top:2px}
.conn-body{
  display:grid;grid-template-columns:1fr 1fr;gap:var(--sp-3);
  margin-top:var(--sp-3);padding-top:var(--sp-3);border-top:1px solid var(--line-1);
}
.conn-stat .l{font-size:var(--fs-11);color:var(--fg-2);text-transform:uppercase;letter-spacing:.04em}
.conn-stat .v{font-family:var(--font-mono);font-size:var(--fs-13);font-weight:500;margin-top:2px}

.list-row{
  display:flex;align-items:center;gap:var(--sp-3);padding:var(--sp-3);
  border-radius:var(--r-md);transition:background var(--dur-1) var(--ease);cursor:pointer;
}
.list-row:hover{background:var(--bg-hover)}
.list-row .ico{
  width:30px;height:30px;border-radius:var(--r-sm);
  background:var(--bg-3);color:var(--fg-1);
  display:flex;align-items:center;justify-content:center;
  font-size:14px;flex-shrink:0;
}
.list-row .txt{flex:1;min-width:0}
.list-row .ttl{font-size:var(--fs-13);font-weight:500}
.list-row .sub{font-size:var(--fs-11);color:var(--fg-2);margin-top:1px}
.list-row .trail{color:var(--fg-3);font-size:14px}

.empty{
  padding:var(--sp-8) var(--sp-5);text-align:center;
  border:1px dashed var(--line-2);border-radius:var(--r-lg);background:var(--bg-1);
}
.empty .ic{
  width:40px;height:40px;margin:0 auto var(--sp-3);
  background:var(--bg-3);color:var(--fg-2);border-radius:var(--r-md);
  display:flex;align-items:center;justify-content:center;font-size:18px;
}
.empty .ttl{font-size:var(--fs-14);font-weight:500;margin-bottom:4px}
.empty .sub{font-size:var(--fs-12);color:var(--fg-2)}
.skeleton{
  background:linear-gradient(90deg,var(--bg-2) 0%,var(--bg-3) 50%,var(--bg-2) 100%);
  background-size:200% 100%;animation:skeleton 1.4s ease-in-out infinite;
  border-radius:var(--r-sm);display:block;
}
@keyframes skeleton{0%{background-position:200% 0}100%{background-position:-200% 0}}

.modal-backdrop{
  position:fixed;inset:0;background:rgba(0,0,0,.6);backdrop-filter:blur(3px);
  display:none;align-items:center;justify-content:center;padding:var(--sp-4);z-index:500;
}
.modal-backdrop.open{display:flex}
.modal{
  background:var(--bg-1);border:1px solid var(--line-2);border-radius:var(--r-xl);
  box-shadow:var(--shadow-3);width:100%;max-width:440px;overflow:hidden;
  animation:modalIn var(--dur-2) var(--ease);
}
@keyframes modalIn{from{opacity:0;transform:translateY(8px) scale(.98)}to{opacity:1;transform:none}}
.modal-head{display:flex;align-items:center;justify-content:space-between;padding:var(--sp-5) var(--sp-5) var(--sp-3)}
.modal-title{font-size:var(--fs-17);font-weight:600;letter-spacing:-.01em}
.modal-sub{font-size:var(--fs-12);color:var(--fg-2);margin-top:3px}
.modal-body{padding:0 var(--sp-5) var(--sp-5);display:flex;flex-direction:column;gap:var(--sp-4)}
.modal-foot{padding:var(--sp-3) var(--sp-5) var(--sp-5);display:flex;gap:8px;justify-content:flex-end}
.modal-close{color:var(--fg-2);width:26px;height:26px;border-radius:var(--r-sm);display:flex;align-items:center;justify-content:center}
.modal-close:hover{background:var(--bg-hover);color:var(--fg-0)}

.toast-host{
  position:fixed;bottom:20px;left:50%;transform:translateX(-50%);
  display:flex;flex-direction:column;gap:8px;z-index:900;pointer-events:none;
  max-width:calc(100vw - 32px);
}
.toast{
  display:flex;align-items:flex-start;gap:10px;padding:12px 14px;
  background:var(--bg-2);border:1px solid var(--line-2);border-radius:var(--r-md);
  box-shadow:var(--shadow-2);font-size:var(--fs-13);pointer-events:auto;
  animation:toastIn var(--dur-2) var(--ease);
  max-width:380px;
}
.toast.out{animation:toastOut var(--dur-2) var(--ease) forwards}
@keyframes toastIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes toastOut{to{opacity:0;transform:translateY(12px)}}
.toast .ic{
  width:18px;height:18px;border-radius:50%;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:1px;
}
.toast .body{flex:1}
.toast .ttl{font-weight:500}
.toast .msg{font-size:var(--fs-12);color:var(--fg-2);margin-top:2px}
.toast.ok{border-color:var(--ok-line)}
.toast.ok .ic{background:var(--ok-bg);color:var(--ok-fg)}
.toast.err{border-color:var(--err-line)}
.toast.err .ic{background:var(--err-bg);color:var(--err-fg)}
.toast.warn{border-color:var(--warn-line)}
.toast.warn .ic{background:var(--warn-bg);color:var(--warn-fg)}
.toast.info{border-color:var(--info-line)}
.toast.info .ic{background:var(--info-bg);color:var(--info-fg)}

.qr-box{display:flex;flex-direction:column;align-items:center;gap:var(--sp-3)}
.qr-canvas{
  width:220px;height:220px;background:#fff;border-radius:var(--r-md);
  padding:10px;box-shadow:var(--shadow-2);
}
.qr-canvas img{width:100%;height:100%;display:block}

.theme-btn{
  display:inline-flex;align-items:center;gap:6px;
  padding:6px 12px;border-radius:var(--r-full);
  background:var(--bg-2);border:1px solid var(--line-2);
  color:var(--fg-1);font-size:var(--fs-12);font-weight:500;
  transition:all var(--dur-2) var(--ease);
}
.theme-btn:hover{color:var(--fg-0);border-color:var(--line-3)}
.theme-btn i{font-size:14px}

@keyframes spin360{to{transform:rotate(360deg)}}

/* App layout */
.app{display:grid;grid-template-columns:240px 1fr;min-height:100vh}
.side{
  position:sticky;top:0;align-self:start;height:100vh;
  background:var(--bg-1);border-right:1px solid var(--line-1);
  display:flex;flex-direction:column;padding:var(--sp-4) var(--sp-3);
  overflow-y:auto;
}
.side-brand{
  display:flex;align-items:center;gap:var(--sp-2);
  padding:var(--sp-2) var(--sp-2) var(--sp-4);
  margin-bottom:var(--sp-3);
  border-bottom:1px solid var(--line-1);
}
.brand-mark{
  width:28px;height:28px;border-radius:var(--r-sm);
  background:linear-gradient(135deg,var(--brand),var(--c-coral-500));
  display:flex;align-items:center;justify-content:center;
  color:#fff;font-family:var(--font-mono);font-weight:700;font-size:13px;
  flex-shrink:0;
}
.brand-txt{font-weight:600;font-size:var(--fs-13);letter-spacing:-.01em}
.brand-ver{font-family:var(--font-mono);font-size:10px;color:var(--fg-3);margin-left:auto}
.side-sec{
  font-size:10px;text-transform:uppercase;letter-spacing:.08em;
  color:var(--fg-3);font-weight:600;
  padding:var(--sp-4) var(--sp-2) var(--sp-2);
}
.side-nav{display:flex;flex-direction:column;gap:2px}
.side-item{
  display:flex;align-items:center;gap:var(--sp-2);
  padding:6px var(--sp-2);border-radius:var(--r-sm);
  font-size:var(--fs-13);color:var(--fg-2);cursor:pointer;
  transition:background var(--dur-1) var(--ease),color var(--dur-1) var(--ease);
}
.side-item i{font-size:15px;flex-shrink:0}
.side-item:hover{background:var(--bg-hover);color:var(--fg-0)}
.side-item.is-active{background:var(--brand-lo);color:var(--brand)}
.side-item .count{
  margin-left:auto;font-family:var(--font-mono);font-size:10px;
  background:var(--bg-3);color:var(--fg-2);padding:1px 6px;border-radius:var(--r-xs);
}
.side-item.is-active .count{background:rgba(112,112,245,.2);color:var(--brand)}
.side-foot{
  margin-top:auto;display:flex;flex-direction:column;gap:6px;
  padding-top:var(--sp-4);border-top:1px solid var(--line-1);
}
.side-foot .btn{justify-content:flex-start}

.mobile-bar{
  display:none;position:sticky;top:0;z-index:100;
  height:52px;background:var(--bg-1);
  border-bottom:1px solid var(--line-1);
  align-items:center;padding:0 var(--sp-4);gap:var(--sp-3);
}
.mobile-bar .brand-mark{width:24px;height:24px;font-size:11px}
.mobile-bar .brand-txt{font-size:var(--fs-13)}
.mobile-bar .spacer{flex:1}
.mobile-bar .btn-icon{background:var(--bg-2);border:1px solid var(--line-2)}

.main{padding:var(--sp-6) var(--sp-8);max-width:1400px;width:100%}
.page{display:none}
.page.on{display:block;animation:pageIn var(--dur-2) var(--ease)}
@keyframes pageIn{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.page-top{
  display:flex;align-items:flex-start;justify-content:space-between;
  gap:var(--sp-4);margin-bottom:var(--sp-5);flex-wrap:wrap;
}
.page-title{font-size:var(--fs-20);font-weight:600;letter-spacing:-.02em}
.page-sub{font-size:var(--fs-12);color:var(--fg-2);margin-top:3px}
.page-top-actions{display:flex;gap:6px;align-items:center;flex-wrap:wrap}

.grid{display:grid;gap:var(--sp-3)}
.grid-4{grid-template-columns:repeat(4,1fr)}
.grid-3-1{grid-template-columns:3fr 1fr}
.grid-2{grid-template-columns:repeat(2,1fr)}
.grid-auto{grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}

.chart-wrap{position:relative;height:240px;margin-top:var(--sp-3)}
.chart-wrap.tall{height:300px}

.default-link-card{
  background:linear-gradient(135deg,var(--bg-2),var(--bg-1));
  border:1px solid var(--line-1);border-radius:var(--r-lg);
  padding:var(--sp-5);margin-bottom:var(--sp-4);
}
.default-link-label{
  font-size:var(--fs-11);text-transform:uppercase;letter-spacing:.06em;
  color:var(--fg-2);font-weight:600;margin-bottom:var(--sp-2);
  display:flex;align-items:center;gap:6px;
}
.default-link-label i{color:var(--brand)}
.default-link-code{
  font-family:var(--font-mono);font-size:var(--fs-11);
  color:var(--fg-1);background:var(--bg-0);
  border:1px solid var(--line-1);border-radius:var(--r-sm);
  padding:10px 12px;word-break:break-all;line-height:1.7;
  max-height:80px;overflow-y:auto;
}
.default-link-actions{display:flex;gap:6px;margin-top:var(--sp-3);flex-wrap:wrap}

.create-panel{
  background:var(--bg-1);border:1px solid var(--line-1);border-radius:var(--r-lg);
  padding:var(--sp-5);margin-bottom:var(--sp-4);
}
.create-grid{display:grid;grid-template-columns:1fr 1fr;gap:var(--sp-4)}
.create-col{display:flex;flex-direction:column;gap:var(--sp-3)}
.chip-row{display:flex;gap:4px;flex-wrap:wrap}
.create-foot{
  margin-top:var(--sp-4);padding-top:var(--sp-4);
  border-top:1px solid var(--line-1);
  display:flex;align-items:center;justify-content:space-between;
  gap:var(--sp-3);flex-wrap:wrap;
}
.create-hint{
  font-size:var(--fs-11);color:var(--fg-3);line-height:1.6;
  display:flex;align-items:flex-start;gap:6px;flex:1;min-width:200px;
}
.create-hint i{color:var(--brand);font-size:14px;margin-top:1px;flex-shrink:0}

.filters{
  display:flex;align-items:center;gap:6px;flex-wrap:wrap;
  margin-bottom:var(--sp-4);
}
.filters .search-wrap{width:240px;margin-left:auto}

.config-grid{display:grid;gap:var(--sp-3);grid-template-columns:repeat(auto-fill,minmax(380px,1fr))}

.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--sp-3);margin-bottom:var(--sp-4)}

.traffic-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:var(--sp-3);margin-bottom:var(--sp-4)}
.traffic-main{
  background:linear-gradient(155deg,var(--bg-2),var(--bg-1));
  border:1px solid var(--line-1);border-radius:var(--r-lg);
  padding:var(--sp-5);position:relative;overflow:hidden;
}
.traffic-main::before{
  content:'';position:absolute;top:-40px;right:-40px;
  width:160px;height:160px;
  background:radial-gradient(circle,var(--brand-lo),transparent 70%);
  pointer-events:none;
}
.traffic-main .label{
  font-size:var(--fs-11);color:var(--fg-2);
  text-transform:uppercase;letter-spacing:.06em;font-weight:600;
  margin-bottom:var(--sp-2);display:flex;align-items:center;gap:6px;
}
.traffic-main .label i{color:var(--brand)}
.traffic-main .value{
  font-size:var(--fs-36);font-weight:700;letter-spacing:-.03em;
  line-height:1;display:flex;align-items:baseline;gap:6px;
}
.traffic-main .value .unit{font-size:var(--fs-14);color:var(--fg-2);font-weight:500}

.group-grid{display:grid;gap:var(--sp-3);grid-template-columns:repeat(auto-fill,minmax(340px,1fr));margin-bottom:var(--sp-4)}
.conn-grid{display:grid;gap:var(--sp-3);grid-template-columns:repeat(auto-fill,minmax(320px,1fr))}

.sub-list-row{
  display:flex;align-items:center;justify-content:space-between;gap:var(--sp-3);
  padding:var(--sp-3);background:var(--bg-2);border:1px solid var(--line-1);
  border-radius:var(--r-md);margin-bottom:6px;flex-wrap:wrap;
}
.sub-list-row .info{flex:1;min-width:200px}
.sub-list-row .name{font-weight:600;font-size:var(--fs-13)}
.sub-list-row .url{font-family:var(--font-mono);font-size:var(--fs-11);color:var(--fg-2);margin-top:3px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.sub-list-row .actions{display:flex;gap:4px}

.log-item{
  display:flex;gap:var(--sp-3);padding:var(--sp-3) 0;
  border-bottom:1px solid var(--line-1);
}
.log-item:last-child{border-bottom:none}
.log-ic{
  width:30px;height:30px;border-radius:var(--r-sm);
  display:flex;align-items:center;justify-content:center;
  font-size:14px;flex-shrink:0;
}
.log-ic.ok{background:var(--ok-bg);color:var(--ok-fg)}
.log-ic.err{background:var(--err-bg);color:var(--err-fg)}
.log-ic.warn{background:var(--warn-bg);color:var(--warn-fg)}
.log-ic.info{background:var(--info-bg);color:var(--info-fg)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:var(--fs-13);line-height:1.6}
.log-time{
  font-size:var(--fs-11);color:var(--fg-3);margin-top:3px;
  display:flex;align-items:center;gap:6px;font-family:var(--font-mono);
}
.log-kind{
  font-size:9px;padding:1px 6px;border-radius:var(--r-xs);
  background:var(--bg-3);color:var(--fg-2);
  text-transform:uppercase;letter-spacing:.04em;font-weight:600;
}
.err-item{padding:var(--sp-3) 0;border-bottom:1px solid var(--line-1)}
.err-item:last-child{border-bottom:none}
.err-time{font-family:var(--font-mono);font-size:var(--fs-11);color:var(--fg-3);margin-bottom:4px}
.err-msg{
  font-family:var(--font-mono);font-size:var(--fs-11);
  background:var(--err-bg);color:var(--err-fg);
  padding:8px 10px;border-radius:var(--r-sm);word-break:break-all;
  border:1px solid var(--err-line);
}

.settings-grid{display:grid;grid-template-columns:1fr 1fr;gap:var(--sp-4)}
.pw-form{display:flex;flex-direction:column;gap:var(--sp-3);max-width:420px}
.pw-strength{display:flex;gap:3px;margin-top:6px}
.pw-strength span{flex:1;height:3px;border-radius:2px;background:var(--bg-3);transition:background var(--dur-2) var(--ease)}
.pw-strength.l1 span:nth-child(1){background:var(--err-fg)}
.pw-strength.l2 span:nth-child(1),.pw-strength.l2 span:nth-child(2){background:var(--warn-fg)}
.pw-strength.l3 span:nth-child(-n+3){background:var(--info-fg)}
.pw-strength.l4 span{background:var(--ok-fg)}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.pw-req{
  font-size:10px;padding:3px 8px;border-radius:var(--r-xs);
  background:var(--bg-2);color:var(--fg-3);font-weight:500;
  transition:all var(--dur-2) var(--ease);
}
.pw-req.met{background:var(--ok-bg);color:var(--ok-fg)}

.support-tiles{display:grid;grid-template-columns:repeat(2,1fr);gap:var(--sp-3)}
.support-tile{
  display:flex;align-items:center;gap:var(--sp-3);
  padding:var(--sp-4);background:var(--bg-2);
  border:1px solid var(--line-1);border-radius:var(--r-md);
  transition:border-color var(--dur-2) var(--ease);
}
.support-tile:hover{border-color:var(--line-2)}
.support-tile .ico{
  width:36px;height:36px;border-radius:var(--r-md);
  background:var(--brand-lo);color:var(--brand);
  display:flex;align-items:center;justify-content:center;font-size:17px;
}
.support-tile .t{font-size:var(--fs-11);color:var(--fg-3);text-transform:uppercase;letter-spacing:.05em;font-weight:600}
.support-tile .v{font-size:var(--fs-13);font-weight:500;margin-top:2px}

.ws-log{
  background:var(--bg-0);border:1px solid var(--line-1);border-radius:var(--r-md);
  padding:var(--sp-3);height:240px;overflow-y:auto;
  font-family:var(--font-mono);font-size:var(--fs-11);line-height:1.7;
}

.picker-list{max-height:320px;overflow-y:auto;margin:var(--sp-2) 0}
.picker-row{
  display:flex;align-items:center;gap:var(--sp-3);padding:8px;
  border-radius:var(--r-sm);cursor:pointer;transition:background var(--dur-1) var(--ease);
  font-size:var(--fs-13);
}
.picker-row:hover{background:var(--bg-hover)}
.picker-row input{accent-color:var(--brand);width:15px;height:15px}
.picker-row .lbl{flex:1}
.picker-row .meta{font-family:var(--font-mono);font-size:var(--fs-11);color:var(--fg-3)}

.row{display:flex;align-items:center;gap:var(--sp-2);flex-wrap:wrap}
.mt-3{margin-top:var(--sp-3)}
.mt-4{margin-top:var(--sp-4)}
.mono{font-family:var(--font-mono)}
.text-muted{color:var(--fg-2)}
.text-sm{font-size:var(--fs-12)}

/* Public page */
.wrap{max-width:720px;margin:0 auto;padding:var(--sp-6) var(--sp-4) var(--sp-12)}
.top{display:flex;align-items:center;justify-content:space-between;gap:var(--sp-3);margin-bottom:var(--sp-6)}
.brand{display:flex;align-items:center;gap:var(--sp-2);min-width:0}
.brand-mark{width:32px;height:32px;border-radius:var(--r-md);background:linear-gradient(135deg,var(--brand),var(--c-coral-500));display:flex;align-items:center;justify-content:center;color:#fff;font-family:var(--font-mono);font-weight:700;font-size:14px;flex-shrink:0}
.top-actions{display:flex;gap:6px}
.hero{background:var(--bg-1);border:1px solid var(--line-1);border-radius:var(--r-xl);padding:var(--sp-6);margin-bottom:var(--sp-4);position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--brand-lo),transparent 70%);pointer-events:none}
.hero-eyebrow{font-family:var(--font-mono);font-size:var(--fs-11);color:var(--brand);letter-spacing:.06em;margin-bottom:var(--sp-2);display:flex;align-items:center;gap:6px}
.hero-title{font-size:var(--fs-24);font-weight:700;letter-spacing:-.02em;margin-bottom:6px}
.hero-desc{font-size:var(--fs-13);color:var(--fg-2);line-height:1.6;margin-bottom:var(--sp-3)}
.hero-meta{font-family:var(--font-mono);font-size:var(--fs-11);color:var(--fg-3);display:flex;align-items:center;gap:6px;margin-bottom:var(--sp-3)}
.sub-pill{display:flex;align-items:center;gap:var(--sp-2);flex-wrap:wrap;background:var(--bg-2);border:1px solid var(--line-1);border-radius:var(--r-md);padding:6px 6px 6px 12px}
.sub-pill .url{flex:1;min-width:120px;font-family:var(--font-mono);font-size:var(--fs-11);color:var(--fg-2);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.stat-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--sp-2);margin-bottom:var(--sp-4)}
.cfg-title{display:flex;align-items:center;gap:6px;font-size:var(--fs-12);font-weight:600;color:var(--fg-2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:var(--sp-3)}
.cfg-title i{color:var(--brand)}
.cfg-grid{display:grid;gap:var(--sp-3)}
.cfg-link-toggle{width:100%;display:flex;align-items:center;justify-content:space-between;gap:var(--sp-2);padding:8px 12px;background:transparent;border:1px dashed var(--line-2);border-radius:var(--r-sm);color:var(--fg-2);font-size:var(--fs-12);font-weight:500;cursor:pointer;transition:all var(--dur-1) var(--ease)}
.cfg-link-toggle:hover{background:var(--brand-lo);border-color:var(--brand-line);color:var(--brand)}
.cfg-link-wrap{display:grid;grid-template-rows:0fr;transition:grid-template-rows var(--dur-2) var(--ease)}
.cfg-link-wrap.open{grid-template-rows:1fr}
.cfg-link-inner{overflow:hidden}
.cfg-link{font-family:var(--font-mono);font-size:10px;background:var(--bg-0);border:1px solid var(--line-1);border-radius:var(--r-sm);padding:10px 12px;color:var(--fg-1);word-break:break-all;line-height:1.7;margin-top:8px;max-height:100px;overflow-y:auto}
.empty-hero{text-align:center;padding:var(--sp-10) var(--sp-4);background:var(--bg-1);border:1px dashed var(--line-2);border-radius:var(--r-xl)}
.empty-hero .ic{width:52px;height:52px;margin:0 auto var(--sp-3);background:var(--bg-3);border-radius:var(--r-lg);display:flex;align-items:center;justify-content:center;color:var(--fg-2);font-size:24px}
.lock-wrap{min-height:calc(100vh - 120px);display:flex;align-items:center;justify-content:center}
.lock-card{width:100%;max-width:380px;background:var(--bg-1);border:1px solid var(--line-2);border-radius:var(--r-xl);padding:var(--sp-8) var(--sp-6);text-align:center;box-shadow:var(--shadow-3)}
.lock-icon-wrap{width:52px;height:52px;margin:0 auto var(--sp-4);background:var(--brand-lo);border-radius:var(--r-lg);display:flex;align-items:center;justify-content:center;color:var(--brand);font-size:22px;position:relative}
.lock-icon-wrap::after{content:'';position:absolute;inset:-6px;border-radius:var(--r-xl);border:1px solid var(--brand-line);animation:lockPulse 2.4s ease-in-out infinite}
@keyframes lockPulse{0%,100%{opacity:.4;transform:scale(1)}50%{opacity:0;transform:scale(1.1)}}
.lock-title{font-size:var(--fs-17);font-weight:600;margin-bottom:6px}
.lock-sub{font-size:var(--fs-12);color:var(--fg-2);margin-bottom:var(--sp-5);line-height:1.6}
.lock-form{display:flex;flex-direction:column;gap:var(--sp-3);text-align:left}
.lock-form .btn{height:42px;font-size:var(--fs-14);border-radius:var(--r-lg);justify-content:center}
.lock-foot{margin-top:var(--sp-5);padding-top:var(--sp-4);border-top:1px solid var(--line-1);font-family:var(--font-mono);font-size:10px;color:var(--fg-3);display:flex;align-items:center;justify-content:center;gap:6px}
.foot{text-align:center;padding-top:var(--sp-8);font-family:var(--font-mono);font-size:10px;color:var(--fg-3)}

@media(max-width:1100px){
  .app{grid-template-columns:1fr}
  .side{display:none}
  .mobile-bar{display:flex}
  .main{padding:var(--sp-4)}
  .grid-4{grid-template-columns:repeat(2,1fr)}
  .grid-3-1{grid-template-columns:1fr}
  .traffic-hero{grid-template-columns:1fr 1fr}
  .conn-hero{grid-template-columns:1fr 1fr}
  .create-grid{grid-template-columns:1fr}
  .settings-grid{grid-template-columns:1fr}
}
@media(max-width:640px){
  .grid-4,.grid-2{grid-template-columns:1fr}
  .traffic-hero{grid-template-columns:1fr}
  .conn-hero{grid-template-columns:1fr 1fr}
  .filters .search-wrap{width:100%;margin-left:0}
  .config-grid,.group-grid,.conn-grid{grid-template-columns:1fr}
  .support-tiles{grid-template-columns:1fr}
  .page-top-actions{width:100%}
  .wrap{padding:var(--sp-4) var(--sp-3) var(--sp-10)}
  .hero{padding:var(--sp-5)}
  .hero-title{font-size:var(--fs-20)}
  .stat-strip{grid-template-columns:1fr 1fr}
  .stat-strip > :nth-child(3){grid-column:1/-1}
  .lock-card{padding:var(--sp-6) var(--sp-5)}
}
.side.open{display:flex;position:fixed;z-index:200;width:240px;box-shadow:var(--shadow-3);transform:translateX(0)}
.side-backdrop{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:150;backdrop-filter:blur(2px)}
.side-backdrop.open{display:block}
"""

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sign in · Gateway</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
__COMMON_CSS__
body{
  display:flex;align-items:center;justify-content:center;padding:20px;
  background:
    radial-gradient(ellipse 600px 300px at 20% 0%,var(--brand-lo),transparent 60%),
    radial-gradient(ellipse 500px 260px at 100% 100%,rgba(255,107,74,.06),transparent 60%),
    var(--bg-0);
}
.login-card{
  width:100%;max-width:400px;
  background:var(--bg-1);border:1px solid var(--line-2);border-radius:var(--r-xl);
  padding:var(--sp-8) var(--sp-6) var(--sp-6);
  box-shadow:var(--shadow-3);
}
.login-brand{display:flex;align-items:center;gap:10px;margin-bottom:var(--sp-6)}
.brand-mark{
  width:36px;height:36px;border-radius:var(--r-md);
  background:linear-gradient(135deg,var(--brand),var(--c-coral-500));
  display:flex;align-items:center;justify-content:center;
  color:#fff;font-family:var(--font-mono);font-weight:700;font-size:16px;
}
.brand-txt{font-weight:600;font-size:var(--fs-14);letter-spacing:-.01em}
.brand-ver{font-family:var(--font-mono);font-size:var(--fs-11);color:var(--fg-2);margin-top:1px}
.login-title{font-size:var(--fs-20);font-weight:700;letter-spacing:-.02em;margin-bottom:6px}
.login-sub{font-size:var(--fs-13);color:var(--fg-2);margin-bottom:var(--sp-5);line-height:1.5}
.login-form{display:flex;flex-direction:column;gap:var(--sp-4)}
.login-form .btn-primary{height:42px;font-size:var(--fs-14);border-radius:var(--r-lg)}
.login-hint{
  margin-top:var(--sp-5);padding-top:var(--sp-4);
  border-top:1px solid var(--line-1);
  display:flex;align-items:center;justify-content:space-between;
  font-size:var(--fs-11);color:var(--fg-3);font-family:var(--font-mono);
}
.login-hint code{
  background:var(--bg-2);border:1px solid var(--line-1);
  padding:2px 8px;border-radius:var(--r-xs);color:var(--fg-1);
}
.login-err{
  display:none;padding:10px 12px;
  background:var(--err-bg);border:1px solid var(--err-line);
  border-radius:var(--r-md);color:var(--err-fg);font-size:var(--fs-12);
  align-items:center;gap:6px;
}
.login-err.show{display:flex}
.login-theme{position:fixed;top:20px;right:20px}
@media(max-width:420px){
  .login-theme{top:12px;right:12px}
  .login-card{padding:var(--sp-6) var(--sp-5) var(--sp-5)}
}
</style>
</head>
<body>
<button class="theme-btn login-theme" onclick="toggleTheme()" aria-label="Toggle theme">
  <i class="ti ti-sun" id="theme-icon"></i>
  <span id="theme-label">Light</span>
</button>

<div class="login-card">
  <div class="login-brand">
    <div class="brand-mark">G</div>
    <div>
      <div class="brand-txt">Gateway</div>
      <div class="brand-ver">v12 · admin panel</div>
    </div>
  </div>
  <div class="login-title">Sign in</div>
  <div class="login-sub">Enter the admin password to access the dashboard.</div>

  <form class="login-form" id="form" autocomplete="on">
    <div class="login-err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="field">
      <label class="field-label" for="pw">Password</label>
      <div class="input-wrap">
        <input class="input" id="pw" type="password" placeholder="••••••••" autocomplete="current-password" required autofocus>
        <button class="trail" type="button" onclick="togglePw('pw', this)" aria-label="Show password"><i class="ti ti-eye"></i></button>
      </div>
    </div>
    <button class="btn btn-primary" type="submit" id="submit-btn"><i class="ti ti-arrow-right"></i> Continue</button>
  </form>

  <div class="login-hint">
    <span>default password</span>
    <code onclick="document.getElementById('pw').value='admin';document.getElementById('pw').focus()">admin</code>
  </div>
</div>

<script>
(function(){
  const saved = localStorage.getItem('gateway-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  renderToggle(saved);
})();
function renderToggle(theme){
  const icon = document.getElementById('theme-icon');
  const label = document.getElementById('theme-label');
  if (theme === 'dark') { icon.className = 'ti ti-sun'; label.textContent = 'Light'; }
  else { icon.className = 'ti ti-moon'; label.textContent = 'Dark'; }
}
function toggleTheme(){
  const cur = document.documentElement.getAttribute('data-theme');
  const next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('gateway-theme', next);
  renderToggle(next);
}
function togglePw(id, btn){
  const el = document.getElementById(id);
  const show = el.type === 'password';
  el.type = show ? 'text' : 'password';
  btn.querySelector('i').className = show ? 'ti ti-eye-off' : 'ti ti-eye';
  btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
}
document.getElementById('form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const btn = document.getElementById('submit-btn');
  const err = document.getElementById('err');
  const errText = document.getElementById('err-text');
  err.classList.remove('show');
  btn.disabled = true;
  btn.classList.add('is-loading');
  btn.innerHTML = 'Signing in…';
  try {
    const r = await fetch('/api/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({password: document.getElementById('pw').value}),
    });
    if (!r.ok) {
      const d = await r.json().catch(() => ({}));
      throw new Error(d.detail || 'Invalid password');
    }
    location.href = '/dashboard';
  } catch (e) {
    errText.textContent = e.message;
    err.classList.add('show');
    btn.disabled = false;
    btn.classList.remove('is-loading');
    btn.innerHTML = '<i class="ti ti-arrow-right"></i> Continue';
  }
});
</script>
</body>
</html>""".replace("__COMMON_CSS__", _COMMON_CSS)


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gateway · Dashboard</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
__COMMON_CSS__
</style>
</head>
<body>

<div class="mobile-bar">
  <div class="brand-mark">G</div>
  <div class="brand-txt">Gateway</div>
  <div class="spacer"></div>
  <button class="btn btn-icon btn-sm" onclick="toggleTheme()" aria-label="Toggle theme"><i class="ti ti-sun" id="mob-theme-icon"></i></button>
  <button class="btn btn-icon btn-sm" onclick="openNav()" aria-label="Open menu"><i class="ti ti-menu-2"></i></button>
</div>
<div class="side-backdrop" id="nav-backdrop" onclick="closeNav()"></div>

<div class="app">
  <aside class="side" id="side">
    <div class="side-brand">
      <div class="brand-mark">G</div>
      <div class="brand-txt">Gateway</div>
      <div class="brand-ver">v12</div>
    </div>

    <div class="side-sec">Panel</div>
    <nav class="side-nav">
      <div class="side-item is-active" data-page="overview"><i class="ti ti-layout-dashboard"></i>Overview</div>
      <div class="side-item" data-page="links"><i class="ti ti-link"></i>Configs<span class="count" id="nb-links">0</span></div>
      <div class="side-item" data-page="subgroups"><i class="ti ti-folders"></i>Sub-groups<span class="count" id="nb-subs">0</span></div>
      <div class="side-item" data-page="subscriptions"><i class="ti ti-rss"></i>Subscriptions</div>
      <div class="side-item" data-page="traffic"><i class="ti ti-chart-area"></i>Traffic</div>
      <div class="side-item" data-page="connections"><i class="ti ti-plug-connected"></i>Connections<span class="count" id="nb-conns">0</span></div>
    </nav>

    <div class="side-sec">System</div>
    <nav class="side-nav">
      <div class="side-item" data-page="security"><i class="ti ti-shield-lock"></i>Security</div>
      <div class="side-item" data-page="logs"><i class="ti ti-history"></i>Activity</div>
      <div class="side-item" data-page="errors"><i class="ti ti-alert-triangle"></i>Errors</div>
      <div class="side-item" data-page="testws"><i class="ti ti-wifi"></i>WebSocket test</div>
      <div class="side-item" data-page="settings"><i class="ti ti-settings"></i>Settings</div>
      <div class="side-item" data-page="support"><i class="ti ti-headset"></i>Support</div>
    </nav>

    <div class="side-foot">
      <button class="btn btn-secondary btn-sm" onclick="toggleTheme()"><i class="ti ti-sun" id="side-theme-icon"></i><span id="side-theme-label">Light mode</span></button>
      <button class="btn btn-ghost btn-sm" style="color:var(--err-fg)" onclick="logout()"><i class="ti ti-logout"></i>Sign out</button>
    </div>
  </aside>

  <main class="main">
    <section class="page on" id="page-overview">
      <div class="page-top">
        <div>
          <div class="page-title">Overview</div>
          <div class="page-sub" id="last-update">Loading…</div>
        </div>
        <div class="page-top-actions">
          <span class="badge ok"><span class="dot ok live"></span> Online</span>
          <span class="badge neutral" id="uptime-badge">—</span>
          <button class="btn btn-secondary btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button>
          <button class="btn btn-primary btn-sm" onclick="navTo('links')"><i class="ti ti-plus"></i> New config</button>
        </div>
      </div>

      <div class="grid grid-4" style="margin-bottom:var(--sp-4)">
        <div class="metric-card">
          <div class="rail"></div>
          <div class="label"><i class="ti ti-plug-connected"></i> Connections</div>
          <div class="value" id="m-conns">—</div>
          <div class="meta"><span class="dot ok live"></span> Live</div>
        </div>
        <div class="metric-card rail-ok">
          <div class="rail"></div>
          <div class="label"><i class="ti ti-arrows-exchange"></i> Total traffic</div>
          <div class="value" id="m-traffic">—<span class="unit">MB</span></div>
          <div class="meta">Since boot</div>
        </div>
        <div class="metric-card">
          <div class="rail"></div>
          <div class="label"><i class="ti ti-link"></i> Active configs</div>
          <div class="value" id="m-active">—</div>
          <div class="meta" id="m-total">of —</div>
        </div>
        <div class="metric-card rail-warn">
          <div class="rail"></div>
          <div class="label"><i class="ti ti-folders"></i> Sub-groups</div>
          <div class="value" id="m-subs">—</div>
          <div class="meta">Total</div>
        </div>
      </div>

      <div class="default-link-card">
        <div class="default-link-label"><i class="ti ti-key"></i> Default config (unlimited)</div>
        <div class="default-link-code" id="default-link">Loading…</div>
        <div class="default-link-actions">
          <button class="btn btn-primary btn-sm" onclick="copyText('default-link')"><i class="ti ti-copy"></i> Copy</button>
          <button class="btn btn-secondary btn-sm" onclick="showQR('Default config', document.getElementById('default-link').textContent)"><i class="ti ti-qrcode"></i> QR</button>
          <button class="btn btn-secondary btn-sm" onclick="navTo('links')"><i class="ti ti-link"></i> All configs</button>
          <button class="btn btn-secondary btn-sm" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> Sub-groups</button>
        </div>
      </div>

      <div class="grid grid-3-1" style="margin-bottom:var(--sp-4)">
        <div class="card">
          <div class="row" style="justify-content:space-between;margin-bottom:var(--sp-3)">
            <div style="font-size:var(--fs-13);font-weight:600">Hourly traffic</div>
            <div class="badge neutral">MB</div>
          </div>
          <div class="chart-wrap"><canvas id="chart-hourly"></canvas></div>
        </div>
        <div class="card">
          <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-3)">Distribution</div>
          <div class="chart-wrap" style="height:200px"><canvas id="chart-dist"></canvas></div>
        </div>
      </div>

      <div class="grid grid-2">
        <div class="card">
          <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-3)">Service status</div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-shield-check"></i></div><div class="txt"><div class="ttl">UUID auth</div><div class="sub">Strict</div></div><span class="badge ok">On</span></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-circle-check"></i></div><div class="txt"><div class="ttl">VLESS / WS tunnel</div><div class="sub">Active</div></div><span class="badge ok">On</span></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-bolt"></i></div><div class="txt"><div class="ttl">XHTTP Ultra</div><div class="sub">All modes</div></div><span class="badge ok">On</span></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-folders"></i></div><div class="txt"><div class="ttl">Sub-groups</div><div class="sub">v12</div></div><span class="badge ok">On</span></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-clock"></i></div><div class="txt"><div class="ttl">Uptime</div><div class="sub" id="uptime-inline">—</div></div></div>
        </div>
        <div class="card">
          <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-3)">Configs at a glance</div>
          <div id="overview-configs">—</div>
        </div>
      </div>
    </section>

    <section class="page" id="page-links">
      <div class="page-top">
        <div>
          <div class="page-title">Configs</div>
          <div class="page-sub">Create, edit and inspect access tokens.</div>
        </div>
        <div class="page-top-actions">
          <span class="badge neutral" id="badge-links">0 configs</span>
        </div>
      </div>

      <div class="create-panel">
        <div style="font-size:var(--fs-14);font-weight:600;margin-bottom:var(--sp-4)">New config</div>
        <div class="create-grid">
          <div class="create-col">
            <div class="field">
              <label class="field-label" for="nl-label">Label</label>
              <input class="input" id="nl-label" placeholder="e.g. Ali — main phone">
            </div>
            <div class="field">
              <label class="field-label" for="nl-protocol">Protocol</label>
              <select class="select" id="nl-protocol">
                <option value="vless-ws">VLESS / WebSocket</option>
                <option value="xhttp-packet-up">XHTTP — packet-up</option>
                <option value="xhttp-stream-up">XHTTP — stream-up</option>
              </select>
            </div>
            <div class="field">
              <label class="field-label" for="nl-fp">Fingerprint (uTLS)</label>
              <select class="select" id="nl-fp">
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
            <div class="field">
              <label class="field-label" for="nl-alpn">ALPN (blank = default)</label>
              <input class="input" id="nl-alpn" placeholder="h2,http/1.1">
            </div>
          </div>
          <div class="create-col">
            <div class="field">
              <label class="field-label" for="nl-sub">Sub-group</label>
              <select class="select" id="nl-sub"><option value="">— none —</option></select>
            </div>
            <div class="field">
              <label class="field-label" for="nl-val">Quota</label>
              <div class="row" style="flex-wrap:nowrap">
                <input class="input" id="nl-val" placeholder="0 = unlimited" style="flex:1">
                <select class="select" id="nl-unit" style="width:90px;flex-shrink:0"><option>GB</option><option selected>MB</option></select>
              </div>
              <div class="chip-row" id="quota-chips">
                <button class="chip chip-sm" data-quota="0,GB" onclick="setQuota(this)">Unlimited</button>
                <button class="chip chip-sm" data-quota="500,MB" onclick="setQuota(this)">500 MB</button>
                <button class="chip chip-sm is-active" data-quota="1,GB" onclick="setQuota(this)">1 GB</button>
                <button class="chip chip-sm" data-quota="5,GB" onclick="setQuota(this)">5 GB</button>
                <button class="chip chip-sm" data-quota="10,GB" onclick="setQuota(this)">10 GB</button>
              </div>
            </div>
            <div class="field">
              <label class="field-label" for="nl-exp">Expiry (days, 0 = never)</label>
              <input class="input" id="nl-exp" type="number" min="0" placeholder="30">
              <div class="chip-row" id="exp-chips">
                <button class="chip chip-sm" data-exp="0" onclick="setExpiry(this)">Never</button>
                <button class="chip chip-sm" data-exp="7" onclick="setExpiry(this)">7d</button>
                <button class="chip chip-sm is-active" data-exp="30" onclick="setExpiry(this)">30d</button>
                <button class="chip chip-sm" data-exp="90" onclick="setExpiry(this)">90d</button>
              </div>
            </div>
            <div class="row" style="flex-wrap:nowrap;gap:var(--sp-3)">
              <div class="field" style="flex:1">
                <label class="field-label" for="nl-port">Port</label>
                <input class="input" id="nl-port" type="number" min="1" max="65535" value="443">
              </div>
              <div class="field" style="flex:1">
                <label class="field-label" for="nl-ip">IP limit</label>
                <input class="input" id="nl-ip" type="number" min="0" value="0" placeholder="0 = ∞">
              </div>
            </div>
            <div class="field">
              <label class="field-label" for="nl-speed">Speed limit (Mbps, 0 = ∞)</label>
              <input class="input" id="nl-speed" type="number" min="0" value="0">
              <div class="chip-row" id="speed-chips">
                <button class="chip chip-sm is-active" data-speed="0" onclick="setSpeed(this)">∞</button>
                <button class="chip chip-sm" data-speed="1" onclick="setSpeed(this)">1</button>
                <button class="chip chip-sm" data-speed="5" onclick="setSpeed(this)">5</button>
                <button class="chip chip-sm" data-speed="10" onclick="setSpeed(this)">10</button>
                <button class="chip chip-sm" data-speed="25" onclick="setSpeed(this)">25</button>
              </div>
            </div>
          </div>
        </div>
        <div class="create-foot">
          <div class="create-hint"><i class="ti ti-info-circle"></i> The UUID is randomly generated; only registered UUIDs can connect. Protocol cannot be changed after creation.</div>
          <button class="btn btn-primary" onclick="createConfig()"><i class="ti ti-plus"></i> Create config</button>
        </div>
      </div>

      <div class="filters">
        <button class="chip is-active" data-filter="all" onclick="filterConfigs(this)">All</button>
        <button class="chip" data-filter="active" onclick="filterConfigs(this)">Active</button>
        <button class="chip" data-filter="expired" onclick="filterConfigs(this)">Expiring</button>
        <button class="chip" data-filter="disabled" onclick="filterConfigs(this)">Disabled</button>
        <div class="search-wrap">
          <i class="ti ti-search"></i>
          <input class="search-input" id="link-search" placeholder="Search configs…" oninput="renderConfigs()">
        </div>
      </div>

      <div class="config-grid" id="config-grid"></div>
      <div class="empty" id="config-empty" style="display:none">
        <div class="ic"><i class="ti ti-link-off"></i></div>
        <div class="ttl">No configs yet</div>
        <div class="sub">Create your first access token above.</div>
      </div>
    </section>

    <section class="page" id="page-subgroups">
      <div class="page-top">
        <div>
          <div class="page-title">Sub-groups</div>
          <div class="page-sub">Bundle configs behind a single public page.</div>
        </div>
        <div class="page-top-actions">
          <span class="badge neutral" id="badge-subs">0 groups</span>
          <button class="btn btn-primary btn-sm" onclick="openModal('modal-newsub')"><i class="ti ti-folder-plus"></i> New group</button>
        </div>
      </div>

      <div class="filters">
        <div class="search-wrap" style="margin-left:0">
          <i class="ti ti-search"></i>
          <input class="search-input" id="sub-search" placeholder="Search groups…" oninput="renderGroups()">
        </div>
      </div>

      <div class="group-grid" id="group-grid"></div>
      <div class="empty" id="group-empty" style="display:none">
        <div class="ic"><i class="ti ti-folders"></i></div>
        <div class="ttl">No groups yet</div>
        <div class="sub">Create one to share configs through a public page.</div>
      </div>
    </section>

    <section class="page" id="page-subscriptions">
      <div class="page-top">
        <div>
          <div class="page-title">Subscriptions</div>
          <div class="page-sub">Plain-text subscription URLs for v2ray clients.</div>
        </div>
      </div>

      <div class="grid grid-2" style="margin-bottom:var(--sp-4)">
        <div class="card">
          <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-2)">Per-config</div>
          <p class="text-sm text-muted" style="line-height:1.7">Each config has its own <code>/sub/{uuid}</code> URL. Copy it from the <i class="ti ti-rss"></i> button on a config card.</p>
        </div>
        <div class="card">
          <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-2)">All configs (admin)</div>
          <p class="text-sm text-muted" style="line-height:1.7;margin-bottom:var(--sp-2)">Includes every active config on the server.</p>
          <div class="sub-list-row">
            <div class="info"><div class="url" id="sub-all-url">…</div></div>
            <div class="actions">
              <button class="btn btn-secondary btn-sm" onclick="copyText('sub-all-url')"><i class="ti ti-copy"></i></button>
              <button class="btn btn-secondary btn-sm" onclick="window.open('/sub-all')"><i class="ti ti-external-link"></i></button>
            </div>
          </div>
          <div class="create-hint" style="margin-top:8px"><i class="ti ti-info-circle"></i> This URL requires an authenticated admin session.</div>
        </div>
      </div>

      <div class="card">
        <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-3)">Group subscriptions</div>
        <div id="sub-groups-list">Loading…</div>
      </div>
    </section>

    <section class="page" id="page-traffic">
      <div class="page-top">
        <div>
          <div class="page-title">Traffic</div>
          <div class="page-sub">Bandwidth consumption over time.</div>
        </div>
        <div class="page-top-actions">
          <button class="btn btn-secondary btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button>
        </div>
      </div>

      <div class="traffic-hero">
        <div class="traffic-main">
          <div class="label"><i class="ti ti-database"></i> Total traffic</div>
          <div class="value" id="t-total">—<span class="unit">MB</span></div>
        </div>
        <div class="metric-card">
          <div class="label">Hourly avg</div>
          <div class="value" id="t-avg">—<span class="unit">MB</span></div>
          <div class="meta">MB / hour</div>
        </div>
        <div class="metric-card rail-warn">
          <div class="label">Peak</div>
          <div class="value" id="t-peak">—<span class="unit">MB</span></div>
          <div class="meta">Highest hour</div>
        </div>
        <div class="metric-card">
          <div class="label">Low</div>
          <div class="value" id="t-low">—<span class="unit">MB</span></div>
          <div class="meta">Lowest hour</div>
        </div>
      </div>

      <div class="card">
        <div class="row" style="justify-content:space-between;margin-bottom:var(--sp-3)">
          <div style="font-size:var(--fs-13);font-weight:600">Traffic trend</div>
          <div class="segmented"><button class="is-active">24h</button><button>7d</button><button>30d</button></div>
        </div>
        <div class="chart-wrap tall"><canvas id="chart-traffic"></canvas></div>
      </div>
    </section>

    <section class="page" id="page-connections">
      <div class="page-top">
        <div>
          <div class="page-title">Live connections</div>
          <div class="page-sub">Grouped by IP address, refreshed every 5s.</div>
        </div>
        <div class="page-top-actions">
          <span class="badge ok" id="conn-live-badge"><span class="dot ok live"></span> —</span>
          <button class="btn btn-secondary btn-sm" onclick="loadConnections()"><i class="ti ti-refresh"></i></button>
        </div>
      </div>

      <div class="conn-hero">
        <div class="metric-card">
          <div class="label"><i class="ti ti-plug-connected"></i> Live</div>
          <div class="value" id="ch-count">—</div>
        </div>
        <div class="metric-card rail-ok">
          <div class="label"><i class="ti ti-arrows-exchange"></i> Traffic</div>
          <div class="value" id="ch-traffic">—</div>
        </div>
        <div class="metric-card">
          <div class="label"><i class="ti ti-clock"></i> Avg duration</div>
          <div class="value" id="ch-avgdur">—</div>
        </div>
        <div class="metric-card rail-warn">
          <div class="label"><i class="ti ti-map-pin"></i> Unique IPs</div>
          <div class="value" id="ch-uniq">—</div>
        </div>
      </div>

      <div class="conn-grid" id="conn-grid"></div>
      <div class="empty" id="conn-empty" style="display:none">
        <div class="ic"><i class="ti ti-plug-off"></i></div>
        <div class="ttl">No active connections</div>
        <div class="sub">As soon as clients connect, they'll appear here.</div>
      </div>
    </section>

    <section class="page" id="page-security">
      <div class="page-top">
        <div>
          <div class="page-title">Security</div>
          <div class="page-sub">Cryptography and access control in use.</div>
        </div>
      </div>

      <div class="grid grid-2">
        <div class="card">
          <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-3)">Encryption</div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-certificate"></i></div><div class="txt"><div class="ttl">TLS / HTTPS</div><div class="sub">port 443</div></div><span class="badge ok">On</span></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-fingerprint"></i></div><div class="txt"><div class="ttl">Fingerprint</div><div class="sub">uTLS chrome spoof</div></div></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-network"></i></div><div class="txt"><div class="ttl">Protocols</div><div class="sub">VLESS/WS + XHTTP Ultra</div></div></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-key"></i></div><div class="txt"><div class="ttl">Password hash</div><div class="sub">SHA-256 + secret</div></div></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-cookie"></i></div><div class="txt"><div class="ttl">Session</div><div class="sub">HttpOnly · 365 days</div></div></div>
        </div>
        <div class="card">
          <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-3)">Access control</div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-id-badge"></i></div><div class="txt"><div class="ttl">Strict UUID auth</div><div class="sub">Unknown UUID → rejected</div></div><span class="badge ok">On</span></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-toggle-right"></i></div><div class="txt"><div class="ttl">Active toggle</div><div class="sub">Instant per-config switch</div></div><span class="badge ok">On</span></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-gauge"></i></div><div class="txt"><div class="ttl">Quota</div><div class="sub">Bytes per config</div></div><span class="badge ok">On</span></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-calendar-x"></i></div><div class="txt"><div class="ttl">Expiration</div><div class="sub">Per-config date</div></div><span class="badge ok">On</span></div>
          <div class="list-row" style="padding:10px 0"><div class="ico"><i class="ti ti-lock"></i></div><div class="txt"><div class="ttl">Group password</div><div class="sub">SHA-256, optional</div></div><span class="badge ok">On</span></div>
        </div>
      </div>
    </section>

    <section class="page" id="page-logs">
      <div class="page-top">
        <div>
          <div class="page-title">Activity</div>
          <div class="page-sub">Full timeline of panel events.</div>
        </div>
        <div class="page-top-actions">
          <button class="btn btn-secondary btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button>
        </div>
      </div>
      <div class="card"><div id="logs-list">Loading…</div></div>
    </section>

    <section class="page" id="page-errors">
      <div class="page-top">
        <div>
          <div class="page-title">Errors</div>
          <div class="page-sub">Recent runtime errors.</div>
        </div>
        <div class="page-top-actions">
          <span class="badge err" id="err-badge">0</span>
          <button class="btn btn-secondary btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button>
        </div>
      </div>
      <div class="card"><div id="err-list">—</div></div>
    </section>

    <section class="page" id="page-testws">
      <div class="page-top">
        <div>
          <div class="page-title">WebSocket test</div>
          <div class="page-sub">Verify that a config's UUID can reach the VLESS/WS tunnel.</div>
        </div>
      </div>
      <div class="card" style="max-width:720px">
        <div class="create-hint" style="margin-bottom:var(--sp-3)"><i class="ti ti-info-circle"></i> Only registered and active UUIDs will connect. This tests VLESS/WS only — use your client for XHTTP.</div>
        <div class="row" style="flex-wrap:nowrap;margin-bottom:var(--sp-3)">
          <input class="input is-mono" id="ws-uuid" placeholder="UUID of an active config" style="flex:1">
          <button class="btn btn-primary" onclick="wsConnect()"><i class="ti ti-plug-connected"></i></button>
          <button class="btn btn-danger" onclick="wsClose()"><i class="ti ti-plug-x"></i></button>
        </div>
        <div class="row" style="flex-wrap:nowrap;margin-bottom:var(--sp-3)">
          <input class="input" id="ws-msg" placeholder="Message to send…" style="flex:1">
          <button class="btn btn-secondary" onclick="wsSend()"><i class="ti ti-send"></i></button>
        </div>
        <div class="ws-log" id="ws-log"><span style="color:var(--fg-3)">Waiting for connection…</span></div>
      </div>
    </section>

    <section class="page" id="page-settings">
      <div class="page-top">
        <div>
          <div class="page-title">Settings</div>
          <div class="page-sub">Server info and admin password.</div>
        </div>
      </div>

      <div class="settings-grid">
        <div class="card">
          <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-3)">Server</div>
          <div class="list-row"><div class="ico"><i class="ti ti-world"></i></div><div class="txt"><div class="ttl">Domain</div><div class="sub mono" id="set-host">—</div></div></div>
          <div class="list-row"><div class="ico"><i class="ti ti-versions"></i></div><div class="txt"><div class="ttl">Version</div><div class="sub">v12</div></div></div>
          <div class="list-row"><div class="ico"><i class="ti ti-brand-fastapi"></i></div><div class="txt"><div class="ttl">Stack</div><div class="sub">FastAPI · Uvicorn</div></div></div>
          <div class="list-row"><div class="ico"><i class="ti ti-cloud"></i></div><div class="txt"><div class="ttl">Platform</div><div class="sub">Railway</div></div></div>
          <div class="list-row"><div class="ico"><i class="ti ti-device-floppy"></i></div><div class="txt"><div class="ttl">Storage</div><div class="sub mono">/data/gateway_state.json</div></div></div>
        </div>

        <div class="card">
          <div style="font-size:var(--fs-13);font-weight:600;margin-bottom:var(--sp-3)">Change password</div>
          <div class="pw-form">
            <div class="field">
              <label class="field-label" for="cp-current">Current password</label>
              <div class="input-wrap">
                <input class="input" id="cp-current" type="password" placeholder="••••••••">
                <button class="trail" onclick="togglePw('cp-current', this)" aria-label="Show"><i class="ti ti-eye"></i></button>
              </div>
            </div>
            <div class="field">
              <label class="field-label" for="cp-new">New password</label>
              <div class="input-wrap">
                <input class="input" id="cp-new" type="password" placeholder="At least 4 characters" oninput="updatePwStrength(this.value)">
                <button class="trail" onclick="togglePw('cp-new', this)" aria-label="Show"><i class="ti ti-eye"></i></button>
              </div>
              <div class="pw-strength" id="pw-strength"><span></span><span></span><span></span><span></span></div>
              <div class="pw-reqs">
                <span class="pw-req" id="req-len">4+ chars</span>
                <span class="pw-req" id="req-num">contains digit</span>
                <span class="pw-req" id="req-case">mixed case</span>
                <span class="pw-req" id="req-long">8+ chars</span>
              </div>
            </div>
            <div class="field">
              <label class="field-label" for="cp-confirm">Confirm new password</label>
              <div class="input-wrap">
                <input class="input" id="cp-confirm" type="password" placeholder="Repeat new password">
                <button class="trail" onclick="togglePw('cp-confirm', this)" aria-label="Show"><i class="ti ti-eye"></i></button>
              </div>
            </div>
            <button class="btn btn-primary" style="align-self:flex-start" onclick="changePassword()"><i class="ti ti-shield-check"></i> Save password</button>
          </div>
        </div>
      </div>
    </section>

    <section class="page" id="page-support">
      <div class="page-top">
        <div>
          <div class="page-title">Support</div>
          <div class="page-sub">Where to reach the maintainers.</div>
        </div>
      </div>
      <div class="support-tiles" style="max-width:640px">
        <a class="support-tile" href="https://t.me/X4GHUB" target="_blank" rel="noopener">
          <div class="ico"><i class="ti ti-speakerphone"></i></div>
          <div><div class="t">Telegram</div><div class="v">t.me/X4GHUB</div></div>
        </a>
        <a class="support-tile" href="https://github.com/x4gpanell" target="_blank" rel="noopener">
          <div class="ico"><i class="ti ti-brand-github"></i></div>
          <div><div class="t">GitHub</div><div class="v">github.com/x4gpanell</div></div>
        </a>
      </div>
    </section>
  </main>
</div>

<div class="modal-backdrop" id="modal-edit">
  <div class="modal">
    <div class="modal-head">
      <div>
        <div class="modal-title">Edit config</div>
        <div class="modal-sub">Update label, quota and behaviour.</div>
      </div>
      <button class="modal-close" onclick="closeModal('modal-edit')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <input type="hidden" id="el-uuid">
      <div class="field"><label class="field-label">Label</label><input class="input" id="el-label"></div>
      <div class="field"><label class="field-label">Note</label><input class="input" id="el-note" placeholder="Optional"></div>
      <div class="row" style="flex-wrap:nowrap;gap:var(--sp-2)">
        <div class="field" style="flex:1"><label class="field-label">Quota</label><input class="input" id="el-quota" type="number" min="0" placeholder="0 = ∞"></div>
        <div class="field" style="width:90px"><label class="field-label">Unit</label><select class="select" id="el-unit"><option>GB</option><option>MB</option></select></div>
      </div>
      <div class="field"><label class="field-label">Expires in (days, 0 = keep current)</label><input class="input" id="el-exp" type="number" min="0"></div>
      <div class="field"><label class="field-label">Fingerprint</label>
        <select class="select" id="el-fp">
          <option>chrome</option><option>firefox</option><option>safari</option><option>ios</option><option>android</option>
          <option>edge</option><option>360</option><option>qq</option><option>random</option><option>randomized</option>
        </select>
      </div>
      <div class="field"><label class="field-label">ALPN</label><input class="input" id="el-alpn" placeholder="Blank = default"></div>
      <div class="row" style="flex-wrap:nowrap;gap:var(--sp-2)">
        <div class="field" style="flex:1"><label class="field-label">Port</label><input class="input" id="el-port" type="number" min="1" max="65535"></div>
        <div class="field" style="flex:1"><label class="field-label">IP limit</label><input class="input" id="el-ip" type="number" min="0"></div>
      </div>
      <div class="field"><label class="field-label">Speed limit (Mbps, 0 = ∞)</label><input class="input" id="el-speed" type="number" min="0" step="0.5"></div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-edit')">Cancel</button>
      <button class="btn btn-primary" onclick="saveEditConfig()"><i class="ti ti-check"></i> Save</button>
    </div>
  </div>
</div>

<div class="modal-backdrop" id="modal-delete">
  <div class="modal">
    <div class="modal-head">
      <div>
        <div class="modal-title">Delete config?</div>
        <div class="modal-sub">This action cannot be undone.</div>
      </div>
      <button class="modal-close" onclick="closeModal('modal-delete')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <p style="font-size:var(--fs-13);color:var(--fg-1);line-height:1.6" id="delete-msg">Are you sure?</p>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-delete')">Cancel</button>
      <button class="btn btn-danger" id="delete-ok-btn"><i class="ti ti-trash"></i> Delete</button>
    </div>
  </div>
</div>

<div class="modal-backdrop" id="modal-newsub">
  <div class="modal">
    <div class="modal-head">
      <div>
        <div class="modal-title">New sub-group</div>
        <div class="modal-sub">A public page bundling selected configs.</div>
      </div>
      <button class="modal-close" onclick="closeModal('modal-newsub')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="field"><label class="field-label">Name</label><input class="input" id="ns-name" placeholder="e.g. Team — Europe"></div>
      <div class="field"><label class="field-label">Description</label><input class="input" id="ns-desc" placeholder="Optional"></div>
      <div class="field"><label class="field-label">Password (optional)</label>
        <div class="input-wrap">
          <input class="input" id="ns-pw" type="password" placeholder="Leave blank for public">
          <button class="trail" onclick="togglePw('ns-pw', this)" aria-label="Show"><i class="ti ti-eye"></i></button>
        </div>
      </div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-newsub')">Cancel</button>
      <button class="btn btn-primary" onclick="createGroup()"><i class="ti ti-folder-plus"></i> Create</button>
    </div>
  </div>
</div>

<div class="modal-backdrop" id="modal-pick">
  <div class="modal" style="max-width:520px">
    <div class="modal-head">
      <div>
        <div class="modal-title" id="pick-title">Manage configs</div>
        <div class="modal-sub">Toggle configs to include or exclude them.</div>
      </div>
      <button class="modal-close" onclick="closeModal('modal-pick')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="search-wrap">
        <i class="ti ti-search"></i>
        <input class="search-input" id="pick-search" placeholder="Search configs…" oninput="filterPicker(this.value)">
      </div>
      <div class="picker-list" id="pick-list"></div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-pick')">Close</button>
      <button class="btn btn-primary" onclick="savePicker()"><i class="ti ti-check"></i> Save</button>
    </div>
  </div>
</div>

<div class="modal-backdrop" id="modal-qr">
  <div class="modal" style="max-width:380px">
    <div class="modal-head">
      <div>
        <div class="modal-title" id="qr-title">Scan QR</div>
        <div class="modal-sub">Point your VPN client's scanner at it.</div>
      </div>
      <button class="modal-close" onclick="closeModal('modal-qr')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="qr-box"><div class="qr-canvas" id="qr-img-wrap"><img id="qr-img" src="" alt="QR"></div></div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-primary" onclick="copyQRText()"><i class="ti ti-copy"></i> Copy link</button>
    </div>
  </div>
</div>

<div class="toast-host" id="toast-host"></div>

<script>
(function(){
  const saved = localStorage.getItem('gateway-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  renderThemeLabels(saved);
})();
function renderThemeLabels(theme){
  const icon = theme === 'dark' ? 'ti-sun' : 'ti-moon';
  const sideLabel = theme === 'dark' ? 'Light mode' : 'Dark mode';
  const mobIcon = document.getElementById('mob-theme-icon');
  if (mobIcon) mobIcon.className = 'ti ' + icon;
  const sideIcon = document.getElementById('side-theme-icon');
  if (sideIcon) sideIcon.className = 'ti ' + icon;
  const sideLbl = document.getElementById('side-theme-label');
  if (sideLbl) sideLbl.textContent = sideLabel;
}
function toggleTheme(){
  const cur = document.documentElement.getAttribute('data-theme');
  const next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('gateway-theme', next);
  renderThemeLabels(next);
  if (typeof rebuildCharts === 'function') rebuildCharts();
}

const PAGE_LOADERS = {
  overview: () => { refreshOverview(); },
  links: () => { loadConfigs(); loadGroupsListForPicker(); },
  subgroups: () => { loadGroups(); },
  subscriptions: () => { loadSubsPage(); },
  traffic: () => { refreshTraffic(); },
  connections: () => { loadConnections(); },
  logs: () => { loadActivity(); },
  errors: () => { loadErrors(); },
  settings: () => { document.getElementById('set-host').textContent = location.host; }
};
function navTo(name){
  document.querySelectorAll('.side-item').forEach(el => el.classList.toggle('is-active', el.dataset.page === name));
  document.querySelectorAll('.page').forEach(el => el.classList.toggle('on', el.id === 'page-' + name));
  if (PAGE_LOADERS[name]) PAGE_LOADERS[name]();
  closeNav();
  window.scrollTo({top: 0, behavior: 'smooth'});
}
document.querySelectorAll('.side-item').forEach(el => el.addEventListener('click', () => navTo(el.dataset.page)));

function openNav(){
  document.getElementById('side').classList.add('open');
  document.getElementById('nav-backdrop').classList.add('open');
}
function closeNav(){
  document.getElementById('side').classList.remove('open');
  document.getElementById('nav-backdrop').classList.remove('open');
}

function esc(s){return String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function fmtB(b){
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if (b < 1024**3) return (b/1024**2).toFixed(2) + ' MB';
  return (b/1024**3).toFixed(2) + ' GB';
}
function daysLeft(exp){ if (!exp) return null; return Math.ceil((new Date(exp) - Date.now()) / 864e5); }
function toast(title, msg = '', level = 'info'){
  const host = document.getElementById('toast-host');
  const icons = { ok: 'ti-check', err: 'ti-x', warn: 'ti-alert-triangle', info: 'ti-info-circle' };
  const el = document.createElement('div');
  el.className = 'toast ' + level;
  el.innerHTML = `<div class="ic"><i class="ti ${icons[level] || icons.info}"></i></div><div class="body"><div class="ttl">${esc(title)}</div>${msg ? `<div class="msg">${esc(msg)}</div>` : ''}</div>`;
  host.appendChild(el);
  setTimeout(() => { el.classList.add('out'); setTimeout(() => el.remove(), 250); }, 2600);
}
function copyText(id){
  const el = document.getElementById(id);
  if (!el) return;
  const txt = el.textContent;
  navigator.clipboard.writeText(txt).then(() => toast('Copied to clipboard', '', 'ok'));
}
function copyRaw(txt){
  navigator.clipboard.writeText(txt).then(() => toast('Copied to clipboard', '', 'ok'));
}
function togglePw(id, btn){
  const el = document.getElementById(id);
  const show = el.type === 'password';
  el.type = show ? 'text' : 'password';
  btn.querySelector('i').className = show ? 'ti ti-eye-off' : 'ti ti-eye';
  btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
}

async function api(url, opts = {}){
  const r = await fetch(url, opts);
  if (r.status === 401){ location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}

let allLinks = [];
let allGroups = [];
let activeFilter = 'all';

async function refreshOverview(){
  try {
    const r = await api('/stats');
    const d = await r.json();
    document.getElementById('m-conns').textContent = d.active_connections;
    document.getElementById('nb-conns').textContent = d.active_connections;
    document.getElementById('m-traffic').innerHTML = d.total_traffic_mb.toFixed(1) + '<span class="unit">MB</span>';
    document.getElementById('m-active').textContent = d.active_links ?? '—';
    document.getElementById('m-total').textContent = 'of ' + d.links_count;
    document.getElementById('m-subs').textContent = d.subs_count ?? 0;
    document.getElementById('nb-links').textContent = d.links_count;
    document.getElementById('nb-subs').textContent = d.subs_count ?? 0;
    document.getElementById('uptime-badge').textContent = d.uptime;
    document.getElementById('uptime-inline').textContent = d.uptime;
    document.getElementById('last-update').textContent = 'Updated ' + new Date().toLocaleTimeString();
    document.getElementById('err-badge').textContent = d.total_errors;
    renderOverviewConfigs();
    renderErrors(d.recent_errors || []);
    if (d.hourly) updateHourlyChart(d.hourly);
  } catch (e) { /* silent */ }
}

async function refreshDefaultLink(){
  try {
    const r = await api('/api/links');
    const d = await r.json();
    allLinks = d.links || [];
    const def = allLinks.find(l => l.is_default) || allLinks.find(l => l.active && !l.expired) || allLinks[0];
    document.getElementById('default-link').textContent = def ? def.vless_link : 'No configs yet';
    document.getElementById('badge-links').textContent = allLinks.length + ' configs';
  } catch (e) {}
}

function renderOverviewConfigs(){
  const host = document.getElementById('overview-configs');
  if (!allLinks.length){ host.innerHTML = '<div class="text-sm text-muted">No configs yet.</div>'; return; }
  host.innerHTML = allLinks.slice(0, 6).map(l => `
    <div class="list-row" style="padding:8px 0">
      <div class="ico"><i class="ti ti-key"></i></div>
      <div class="txt"><div class="ttl">${esc(l.label)}</div><div class="sub mono">${fmtB(l.used_bytes)} / ${l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes)}</div></div>
    </div>
  `).join('');
}

function renderErrors(errs){
  const host = document.getElementById('err-list');
  if (!host) return;
  if (!errs.length){
    host.innerHTML = '<div class="text-sm" style="color:var(--ok-fg);display:flex;align-items:center;gap:6px"><i class="ti ti-circle-check"></i>No errors.</div>';
    return;
  }
  host.innerHTML = errs.slice().reverse().map(e => `
    <div class="err-item">
      <div class="err-time">${new Date(e.time).toLocaleString()}</div>
      <div class="err-msg">${esc(e.error)}${e.url ? ' — ' + esc(e.url) : ''}</div>
    </div>
  `).join('');
}

async function loadConfigs(){
  try {
    const [lr, sr] = await Promise.all([api('/api/links'), api('/api/subs')]);
    const ld = await lr.json();
    const sd = await sr.json();
    allLinks = ld.links || [];
    allGroups = sd.subs || [];
    document.getElementById('badge-links').textContent = allLinks.length + ' configs';
    document.getElementById('nb-links').textContent = allLinks.length;

    const sel = document.getElementById('nl-sub');
    sel.innerHTML = '<option value="">— none —</option>' + allGroups.map(g => `<option value="${esc(g.sub_id)}">${esc(g.name)}</option>`).join('');

    renderConfigs();
  } catch (e) { toast('Could not load configs', '', 'err'); }
}

function renderConfigs(){
  const grid = document.getElementById('config-grid');
  const empty = document.getElementById('config-empty');
  const query = (document.getElementById('link-search').value || '').trim().toLowerCase();

  let list = allLinks;
  if (activeFilter === 'active') list = list.filter(l => l.active && !l.expired);
  else if (activeFilter === 'expired') list = list.filter(l => l.expired || (l.expires_at && daysLeft(l.expires_at) <= 3 && daysLeft(l.expires_at) > 0));
  else if (activeFilter === 'disabled') list = list.filter(l => !l.active);
  if (query) list = list.filter(l => (l.label || '').toLowerCase().includes(query) || (l.uuid || '').includes(query));

  if (!list.length){ grid.innerHTML = ''; empty.style.display = 'block'; return; }
  empty.style.display = 'none';
  grid.innerHTML = list.map(l => renderConfigCard(l)).join('');
}

function renderConfigCard(l){
  const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
  const fillClass = pct > 90 ? 'err' : pct > 70 ? 'warn' : '';
  const statusClass = !l.active ? 'is-inactive' : (l.expired ? 'is-expired' : '');
  const statusPill = !l.active
    ? '<span class="status-pill offline"><span class="dot err"></span> Disabled</span>'
    : l.expired
      ? '<span class="status-pill warn"><span class="dot warn"></span> Expired</span>'
      : '<span class="status-pill online"><span class="dot ok live"></span> Active</span>';
  const protoBadge = l.protocol === 'vless-ws' ? '<span class="badge brand">VLESS · WS</span>'
    : l.protocol === 'xhttp-packet-up' ? '<span class="badge info">XHTTP · packet-up</span>'
    : '<span class="badge info">XHTTP · stream-up</span>';
  const dl = daysLeft(l.expires_at);
  const expLabel = !l.expires_at ? '<span class="meta"><i class="ti ti-infinity"></i> never</span>'
    : dl > 0 ? `<span class="meta"><i class="ti ti-calendar"></i> ${dl}d</span>`
    : '<span class="meta"><i class="ti ti-calendar-x"></i> expired</span>';
  const group = l.sub_id && allGroups.find(g => g.sub_id === l.sub_id);
  const groupBadge = group ? `<span class="badge brand">${esc(group.name)}</span>` : '';
  return `
    <div class="config-card ${statusClass}">
      <div class="config-body">
        <div class="config-head">
          <div>
            <div class="config-name">${esc(l.label)}</div>
            <div class="config-uuid" onclick="copyRaw('${esc(l.uuid)}')" title="Click to copy UUID">${esc(l.uuid.slice(0, 16))}…</div>
          </div>
          ${statusPill}
        </div>
        <div class="config-tags">
          ${protoBadge}
          ${groupBadge}
        </div>
        <div class="progress" style="margin-top:12px"><div class="fill ${fillClass}" style="width:${pct}%"></div></div>
        <div class="progress-meta">
          <span>${fmtB(l.used_bytes)} / ${l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes)}</span>
          <span>${pct.toFixed(0)}%</span>
        </div>
      </div>
      <div class="config-tear"></div>
      <div class="config-foot">
        <div class="meta">
          <span><i class="ti ti-route"></i> :${l.port || 443}</span>
          <span><i class="ti ti-users"></i> ${l.connected_ips || 0}/${l.ip_limit || '∞'}</span>
          ${expLabel}
        </div>
        <div class="config-actions">
          <button class="btn btn-secondary btn-icon btn-sm" onclick="copyRaw('${esc(l.vless_link)}')" title="Copy link"><i class="ti ti-copy"></i></button>
          <button class="btn btn-secondary btn-icon btn-sm" onclick="showQR('${esc(l.label)}', '${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
          <button class="btn btn-secondary btn-icon btn-sm" onclick="openEdit('${l.uuid}')" title="Edit"><i class="ti ti-edit"></i></button>
          <button class="btn btn-secondary btn-icon btn-sm" onclick="toggleConfig('${l.uuid}', ${!l.active})" title="${l.active ? 'Disable' : 'Enable'}"><i class="ti ti-${l.active ? 'toggle-right' : 'toggle-left'}"></i></button>
          <button class="btn btn-danger btn-icon btn-sm" onclick="askDelete('${l.uuid}', '${esc(l.label)}')" title="Delete"><i class="ti ti-trash"></i></button>
        </div>
      </div>
    </div>
  `;
}

function filterConfigs(btn){
  document.querySelectorAll('.filters .chip').forEach(c => c.classList.remove('is-active'));
  btn.classList.add('is-active');
  activeFilter = btn.dataset.filter;
  renderConfigs();
}

function setQuota(btn){
  document.querySelectorAll('#quota-chips .chip').forEach(c => c.classList.remove('is-active'));
  btn.classList.add('is-active');
  const [v, u] = btn.dataset.quota.split(',');
  document.getElementById('nl-val').value = v === '0' ? '' : v;
  document.getElementById('nl-unit').value = u;
}
function setExpiry(btn){
  document.querySelectorAll('#exp-chips .chip').forEach(c => c.classList.remove('is-active'));
  btn.classList.add('is-active');
  document.getElementById('nl-exp').value = btn.dataset.exp === '0' ? '' : btn.dataset.exp;
}
function setSpeed(btn){
  document.querySelectorAll('#speed-chips .chip').forEach(c => c.classList.remove('is-active'));
  btn.classList.add('is-active');
  document.getElementById('nl-speed').value = btn.dataset.speed;
}

async function createConfig(){
  const body = {
    label: document.getElementById('nl-label').value.trim() || 'New config',
    protocol: document.getElementById('nl-protocol').value,
    fingerprint: document.getElementById('nl-fp').value,
    alpn: document.getElementById('nl-alpn').value.trim(),
    sub_id: document.getElementById('nl-sub').value || null,
    limit_value: parseFloat(document.getElementById('nl-val').value) || 0,
    limit_unit: document.getElementById('nl-unit').value,
    expires_days: parseInt(document.getElementById('nl-exp').value) || 0,
    port: parseInt(document.getElementById('nl-port').value) || 443,
    ip_limit: parseInt(document.getElementById('nl-ip').value) || 0,
    speed_limit_value: parseFloat(document.getElementById('nl-speed').value) || 0,
    speed_limit_unit: 'MBIT',
  };
  try {
    const r = await api('/api/links', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body),
    });
    if (!r.ok) throw new Error('failed');
    toast('Config created', '', 'ok');
    ['nl-label', 'nl-val', 'nl-exp', 'nl-alpn'].forEach(id => document.getElementById(id).value = '');
    document.getElementById('nl-port').value = '443';
    document.getElementById('nl-ip').value = '0';
    document.getElementById('nl-speed').value = '0';
    loadConfigs();
  } catch (e) { toast('Could not create config', '', 'err'); }
}

function openEdit(uuid){
  const l = allLinks.find(x => x.uuid === uuid);
  if (!l) return;
  document.getElementById('el-uuid').value = uuid;
  document.getElementById('el-label').value = l.label;
  document.getElementById('el-note').value = l.note || '';
  if (l.limit_bytes === 0){ document.getElementById('el-quota').value = ''; document.getElementById('el-unit').value = 'GB'; }
  else { document.getElementById('el-quota').value = (l.limit_bytes / 1024**3).toFixed(2); document.getElementById('el-unit').value = 'GB'; }
  document.getElementById('el-exp').value = '';
  document.getElementById('el-fp').value = l.fingerprint || 'chrome';
  document.getElementById('el-alpn').value = l.alpn || '';
  document.getElementById('el-port').value = l.port || 443;
  document.getElementById('el-ip').value = l.ip_limit || 0;
  document.getElementById('el-speed').value = l.speed_limit_bytes ? (l.speed_limit_bytes * 8 / 1024 / 1024).toFixed(2) : 0;
  openModal('modal-edit');
}

async function saveEditConfig(){
  const uuid = document.getElementById('el-uuid').value;
  const body = {
    label: document.getElementById('el-label').value.trim(),
    note: document.getElementById('el-note').value.trim(),
    limit_value: parseFloat(document.getElementById('el-quota').value) || 0,
    limit_unit: document.getElementById('el-unit').value,
    fingerprint: document.getElementById('el-fp').value,
    alpn: document.getElementById('el-alpn').value.trim(),
    port: parseInt(document.getElementById('el-port').value) || 443,
    ip_limit: parseInt(document.getElementById('el-ip').value) || 0,
    speed_limit_value: parseFloat(document.getElementById('el-speed').value) || 0,
    speed_limit_unit: 'MBIT',
  };
  const exp = parseInt(document.getElementById('el-exp').value);
  if (exp && exp > 0) body.expires_days = exp;
  try {
    const r = await api('/api/links/' + uuid, {
      method: 'PATCH',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body),
    });
    if (!r.ok) throw new Error();
    closeModal('modal-edit');
    toast('Config updated', '', 'ok');
    loadConfigs();
  } catch (e) { toast('Could not update config', '', 'err'); }
}

async function toggleConfig(uuid, active){
  try {
    const r = await api('/api/links/' + uuid, {
      method: 'PATCH',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({active}),
    });
    if (!r.ok) throw new Error();
    toast(active ? 'Config enabled' : 'Config disabled', '', 'ok');
    loadConfigs();
  } catch (e) { toast('Update failed', '', 'err'); }
}

let pendingDeleteUuid = null;
function askDelete(uuid, label){
  pendingDeleteUuid = uuid;
  document.getElementById('delete-msg').innerHTML = 'Delete <strong>' + esc(label) + '</strong>? Any active sessions will be terminated.';
  document.getElementById('delete-ok-btn').onclick = confirmDelete;
  openModal('modal-delete');
}
async function confirmDelete(){
  if (!pendingDeleteUuid) return;
  try {
    const r = await api('/api/links/' + pendingDeleteUuid, { method: 'DELETE' });
    if (!r.ok) throw new Error();
    closeModal('modal-delete');
    toast('Config deleted', '', 'ok');
    pendingDeleteUuid = null;
    loadConfigs();
  } catch (e) { toast('Delete failed', '', 'err'); }
}

async function loadGroups(){
  try {
    const r = await api('/api/subs');
    const d = await r.json();
    allGroups = d.subs || [];
    document.getElementById('badge-subs').textContent = allGroups.length + ' groups';
    document.getElementById('nb-subs').textContent = allGroups.length;
    renderGroups();
  } catch (e) { toast('Could not load groups', '', 'err'); }
}

function renderGroups(){
  const grid = document.getElementById('group-grid');
  const empty = document.getElementById('group-empty');
  const q = (document.getElementById('sub-search').value || '').trim().toLowerCase();
  let list = allGroups;
  if (q) list = list.filter(g => (g.name || '').toLowerCase().includes(q) || (g.desc || '').toLowerCase().includes(q));
  if (!list.length){ grid.innerHTML = ''; empty.style.display = 'block'; return; }
  empty.style.display = 'none';
  grid.innerHTML = list.map(g => `
    <div class="group-card">
      <div class="group-head">
        <div class="group-icon"><i class="ti ti-folder"></i></div>
        <div style="flex:1;min-width:0">
          <div class="group-name">${esc(g.name)}</div>
          <div class="group-desc">${esc(g.desc || 'No description')}</div>
        </div>
        <i class="ti ${g.has_password ? 'ti-lock' : 'ti-lock-open'}" style="color:${g.has_password ? 'var(--warn-fg)' : 'var(--ok-fg)'}"></i>
      </div>
      <div class="group-url" title="${esc(g.public_url)}">${esc(g.public_url)}</div>
      <div class="group-stats">
        <div class="group-stat"><div class="v">${g.links_count}</div><div class="l">configs</div></div>
        <div class="group-stat"><div class="v">${g.active_count}</div><div class="l">active</div></div>
        <div class="group-stat"><div class="v">${esc(g.total_used_fmt)}</div><div class="l">used</div></div>
      </div>
      <div class="row">
        <button class="btn btn-secondary btn-sm" onclick="openPicker('${esc(g.sub_id)}', '${esc(g.name)}')"><i class="ti ti-link-plus"></i> Configs</button>
        <button class="btn btn-secondary btn-sm" onclick="copyRaw('${esc(g.sub_url)}')"><i class="ti ti-rss"></i> Sub</button>
        <button class="btn btn-secondary btn-sm" onclick="copyRaw('${esc(g.public_url)}')"><i class="ti ti-globe"></i> Public</button>
        <button class="btn btn-danger btn-sm" style="margin-left:auto" onclick="deleteGroup('${esc(g.sub_id)}', '${esc(g.name)}')"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  `).join('');
}

async function createGroup(){
  const name = document.getElementById('ns-name').value.trim() || 'New group';
  const desc = document.getElementById('ns-desc').value.trim();
  const pw = document.getElementById('ns-pw').value;
  try {
    const r = await api('/api/subs', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({name, desc, password: pw}),
    });
    if (!r.ok) throw new Error();
    ['ns-name', 'ns-desc', 'ns-pw'].forEach(id => document.getElementById(id).value = '');
    closeModal('modal-newsub');
    toast('Group created', '', 'ok');
    loadGroups();
  } catch (e) { toast('Could not create group', '', 'err'); }
}

async function deleteGroup(sub_id, name){
  if (!confirm('Delete group "' + name + '"? Configs inside it will not be deleted.')) return;
  try {
    const r = await api('/api/subs/' + sub_id, { method: 'DELETE' });
    if (!r.ok) throw new Error();
    toast('Group deleted', '', 'ok');
    loadGroups();
    loadConfigs();
  } catch (e) { toast('Delete failed', '', 'err'); }
}

let pickerSubId = null;
let pickerSelection = new Set();
async function openPicker(subId, groupName){
  pickerSubId = subId;
  document.getElementById('pick-title').textContent = 'Manage "' + groupName + '"';
  document.getElementById('pick-search').value = '';
  const r = await api('/api/subs');
  const d = await r.json();
  const group = (d.subs || []).find(g => g.sub_id === subId);
  pickerSelection = new Set(group?.link_ids || []);
  renderPickerList();
  openModal('modal-pick');
}
function renderPickerList(){
  const host = document.getElementById('pick-list');
  if (!allLinks.length){ host.innerHTML = '<div class="text-sm text-muted">No configs available.</div>'; return; }
  host.innerHTML = allLinks.map(l => `
    <label class="picker-row">
      <input type="checkbox" ${pickerSelection.has(l.uuid) ? 'checked' : ''} onchange="togglePicker('${l.uuid}', this.checked)">
      <span class="lbl">${esc(l.label)}</span>
      <span class="meta">${fmtB(l.used_bytes)}</span>
    </label>
  `).join('');
}
function togglePicker(uuid, checked){
  if (checked) pickerSelection.add(uuid); else pickerSelection.delete(uuid);
}
function filterPicker(q){
  q = q.trim().toLowerCase();
  document.querySelectorAll('.picker-row').forEach(row => {
    const lbl = row.querySelector('.lbl').textContent.toLowerCase();
    row.style.display = (!q || lbl.includes(q)) ? '' : 'none';
  });
}
async function savePicker(){
  if (!pickerSubId) return;
  const ids = [...pickerSelection];
  try {
    await api('/api/subs/' + pickerSubId, {
      method: 'PATCH',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({link_ids: ids}),
    });
    await Promise.all(allLinks.map(l => api('/api/links/' + l.uuid, {
      method: 'PATCH',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({sub_id: pickerSelection.has(l.uuid) ? pickerSubId : null}),
    })));
    closeModal('modal-pick');
    toast('Group configs updated', '', 'ok');
    loadGroups();
    loadConfigs();
  } catch (e) { toast('Save failed', '', 'err'); }
}

function loadSubsPage(){
  document.getElementById('sub-all-url').textContent = location.origin + '/sub-all';
  const host = document.getElementById('sub-groups-list');
  if (!allGroups.length){
    host.innerHTML = '<div class="text-sm text-muted">No groups yet.</div>';
    return;
  }
  host.innerHTML = allGroups.map(g => `
    <div class="sub-list-row">
      <div class="info">
        <div class="name">${esc(g.name)}</div>
        <div class="url">${esc(g.sub_url)}</div>
        <div style="font-size:var(--fs-11);color:var(--fg-3);margin-top:2px">${g.links_count} configs · ${esc(g.total_used_fmt)} used${g.has_password ? ' · password-protected' : ''}</div>
      </div>
      <div class="actions">
        <button class="btn btn-secondary btn-sm" onclick="copyRaw('${esc(g.sub_url)}')"><i class="ti ti-copy"></i></button>
        <button class="btn btn-secondary btn-sm" onclick="copyRaw('${esc(g.public_url)}')"><i class="ti ti-globe"></i></button>
        <button class="btn btn-secondary btn-sm" onclick="showQR('${esc(g.name)}', '${esc(g.sub_url)}')"><i class="ti ti-qrcode"></i></button>
      </div>
    </div>
  `).join('');
}

async function refreshTraffic(){
  try {
    const r = await api('/stats');
    const d = await r.json();
    document.getElementById('t-total').innerHTML = d.total_traffic_mb.toFixed(1) + '<span class="unit">MB</span>';
    const hourly = d.hourly || {};
    const vals = Object.values(hourly).map(v => v / 1024**2);
    if (vals.length){
      const avg = vals.reduce((a,b)=>a+b,0) / vals.length;
      const peak = Math.max(...vals);
      const low = Math.min(...vals);
      document.getElementById('t-avg').innerHTML = avg.toFixed(1) + '<span class="unit">MB</span>';
      document.getElementById('t-peak').innerHTML = peak.toFixed(1) + '<span class="unit">MB</span>';
      document.getElementById('t-low').innerHTML = low.toFixed(1) + '<span class="unit">MB</span>';
    }
    updateTrafficChart(hourly);
  } catch (e) {}
}

async function loadConnections(){
  try {
    const r = await api('/api/connections');
    const d = await r.json();
    document.getElementById('conn-live-badge').innerHTML = '<span class="dot ok live"></span> ' + d.count + ' connections';
    document.getElementById('ch-count').textContent = d.count;
    const conns = d.connections || [];
    if (!conns.length){
      document.getElementById('conn-grid').innerHTML = '';
      document.getElementById('conn-empty').style.display = 'block';
      document.getElementById('ch-traffic').textContent = '—';
      document.getElementById('ch-avgdur').textContent = '—';
      document.getElementById('ch-uniq').textContent = '—';
      return;
    }
    document.getElementById('conn-empty').style.display = 'none';
    const totalBytes = conns.reduce((s,c) => s + (c.bytes || 0), 0);
    document.getElementById('ch-traffic').textContent = fmtB(totalBytes);
    document.getElementById('ch-uniq').textContent = new Set(conns.map(c => c.ip)).size;
    const durs = conns.map(c => c.connected_at ? Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000) : 0);
    const avg = durs.length ? Math.floor(durs.reduce((a,b)=>a+b,0) / durs.length) : 0;
    document.getElementById('ch-avgdur').textContent = formatDuration(avg);

    document.getElementById('conn-grid').innerHTML = conns.map(c => {
      const secs = c.connected_at ? Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000) : 0;
      return `
        <div class="conn-card">
          <div class="conn-head">
            <div class="conn-avatar"><i class="ti ti-device-mobile"></i></div>
            <div style="flex:1;min-width:0">
              <div class="conn-ip">${esc(c.ip)}</div>
              <div class="conn-label">${esc(c.label || '—')}</div>
            </div>
            <span class="status-pill online"><span class="dot ok live"></span> Live</span>
          </div>
          <div class="conn-body">
            <div class="conn-stat"><div class="l">Traffic</div><div class="v">${esc(c.bytes_fmt || fmtB(c.bytes || 0))}</div></div>
            <div class="conn-stat"><div class="l">Duration</div><div class="v">${formatDuration(secs)}</div></div>
          </div>
        </div>
      `;
    }).join('');
  } catch (e) { /* silent */ }
}
function formatDuration(s){
  if (s < 60) return s + 's';
  if (s < 3600) return Math.floor(s / 60) + 'm';
  return Math.floor(s / 3600) + 'h ' + (Math.floor((s % 3600) / 60)) + 'm';
}

async function loadActivity(){
  try {
    const r = await api('/api/activity');
    const d = await r.json();
    const logs = (d.logs || []).slice().reverse();
    const host = document.getElementById('logs-list');
    if (!logs.length){ host.innerHTML = '<div class="text-sm text-muted">No activity yet.</div>'; return; }
    const icons = { ok: 'ti-circle-check', err: 'ti-circle-x', warn: 'ti-alert-triangle', info: 'ti-info-circle' };
    host.innerHTML = logs.map(l => `
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icons[l.level] || icons.info}"></i></div>
        <div class="log-body">
          <div class="log-msg">${esc(l.message)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString()} <span class="log-kind">${esc(l.kind)}</span></div>
        </div>
      </div>
    `).join('');
  } catch (e) {}
}

async function loadErrors(){
  try {
    const r = await api('/stats');
    const d = await r.json();
    renderErrors(d.recent_errors || []);
  } catch (e) {}
}

function updatePwStrength(val){
  const el = document.getElementById('pw-strength');
  el.className = 'pw-strength';
  const hasLen = val.length >= 4;
  const hasNum = /\d/.test(val);
  const hasCase = /[a-z]/.test(val) && /[A-Z]/.test(val);
  const hasLong = val.length >= 8;
  let score = 0;
  if (hasLen) score++;
  if (hasNum) score++;
  if (hasCase) score++;
  if (hasLong) score++;
  if (val.length) el.classList.add('l' + score);
  document.getElementById('req-len').classList.toggle('met', hasLen);
  document.getElementById('req-num').classList.toggle('met', hasNum);
  document.getElementById('req-case').classList.toggle('met', hasCase);
  document.getElementById('req-long').classList.toggle('met', hasLong);
}

async function changePassword(){
  const cur = document.getElementById('cp-current').value;
  const nw = document.getElementById('cp-new').value;
  const cf = document.getElementById('cp-confirm').value;
  if (!cur || !nw || !cf){ toast('All fields required', '', 'err'); return; }
  if (nw.length < 4){ toast('Minimum 4 characters', '', 'err'); return; }
  if (nw !== cf){ toast('Passwords do not match', '', 'err'); return; }
  try {
    const r = await api('/api/change-password', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({current_password: cur, new_password: nw}),
    });
    const d = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(d.detail || 'Failed');
    toast('Password updated', '', 'ok');
    ['cp-current', 'cp-new', 'cp-confirm'].forEach(id => document.getElementById(id).value = '');
  } catch (e) { toast(e.message || 'Failed', '', 'err'); }
}

function openModal(id){ document.getElementById(id).classList.add('open'); }
function closeModal(id){ document.getElementById(id).classList.remove('open'); }
document.querySelectorAll('.modal-backdrop').forEach(el => {
  el.addEventListener('click', e => { if (e.target === el) el.classList.remove('open'); });
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') document.querySelectorAll('.modal-backdrop.open').forEach(m => m.classList.remove('open'));
});

let qrText = '';
function showQR(label, text){
  qrText = text;
  document.getElementById('qr-title').textContent = label;
  document.getElementById('qr-img').src = 'https://api.qrserver.com/v1/create-qr-code/?size=440x440&data=' + encodeURIComponent(text);
  openModal('modal-qr');
}
function copyQRText(){
  if (qrText) copyRaw(qrText);
}

let ws;
function wsLog(color, txt){
  const host = document.getElementById('ws-log');
  const p = document.createElement('div');
  p.style.color = color;
  p.textContent = '[' + new Date().toLocaleTimeString() + '] ' + txt;
  host.appendChild(p);
  host.scrollTop = host.scrollHeight;
}
function wsConnect(){
  const uuid = document.getElementById('ws-uuid').value.trim();
  if (!uuid){ toast('UUID required', '', 'err'); return; }
  const proto = location.protocol === 'https:' ? 'wss' : 'ws';
  ws = new WebSocket(proto + '://' + location.host + '/ws/' + uuid);
  ws.onopen = () => wsLog('var(--ok-fg)', 'Connected');
  ws.onerror = () => wsLog('var(--err-fg)', 'Error — invalid or inactive UUID');
  ws.onmessage = m => wsLog('var(--fg-1)', 'Received ' + (m.data.size || m.data.length) + ' bytes');
  ws.onclose = e => wsLog('var(--err-fg)', 'Closed (' + e.code + ')' + (e.code === 1008 ? ' — access denied' : ''));
}
function wsSend(){
  const msg = document.getElementById('ws-msg').value;
  if (!msg || !ws || ws.readyState !== 1) return;
  ws.send(msg);
  wsLog('var(--warn-fg)', 'Sent: ' + msg);
  document.getElementById('ws-msg').value = '';
}
function wsClose(){ if (ws) ws.close(); }

let chartHourly, chartDist, chartTraffic;
function chartTheme(){
  const cs = getComputedStyle(document.documentElement);
  return {
    fg2: cs.getPropertyValue('--fg-2').trim(),
    fg3: cs.getPropertyValue('--fg-3').trim(),
    line1: cs.getPropertyValue('--line-1').trim(),
    brand: cs.getPropertyValue('--brand').trim(),
    brandLo: cs.getPropertyValue('--brand-lo').trim(),
    okFg: cs.getPropertyValue('--ok-fg').trim(),
    infoFg: cs.getPropertyValue('--info-fg').trim(),
    warnFg: cs.getPropertyValue('--warn-fg').trim(),
    bg1: cs.getPropertyValue('--bg-1').trim(),
  };
}
function initCharts(){
  const t = chartTheme();
  const ctxH = document.getElementById('chart-hourly').getContext('2d');
  const gH = ctxH.createLinearGradient(0, 0, 0, 240);
  gH.addColorStop(0, 'rgba(112,112,245,0.30)');
  gH.addColorStop(1, 'rgba(112,112,245,0)');
  chartHourly = new Chart(ctxH, {
    type: 'line',
    data: { labels: [], datasets: [{
      label: 'MB', data: [], borderColor: t.brand, backgroundColor: gH,
      fill: true, tension: 0.35, pointRadius: 0, borderWidth: 2,
    }]},
    options: {
      responsive: true, maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: { legend: { display: false }, tooltip: { padding: 10, cornerRadius: 8 } },
      scales: {
        x: { grid: { display: false }, ticks: { color: t.fg3, font: { size: 10 } } },
        y: { grid: { color: t.line1 }, ticks: { color: t.fg3, font: { size: 10 }, callback: v => v + ' MB' } },
      },
    },
  });
  chartDist = new Chart(document.getElementById('chart-dist').getContext('2d'), {
    type: 'doughnut',
    data: {
      labels: ['VLESS/WS', 'XHTTP', 'HTTP Proxy'],
      datasets: [{
        data: [55, 35, 10],
        backgroundColor: [t.brand, t.okFg, t.infoFg],
        borderColor: t.bg1, borderWidth: 3, hoverOffset: 6,
      }],
    },
    options: {
      responsive: true, maintainAspectRatio: false, cutout: '72%',
      plugins: {
        legend: { position: 'bottom', labels: { color: t.fg2, font: { size: 10 }, padding: 10, usePointStyle: true, pointStyle: 'circle', boxWidth: 8 } },
      },
    },
  });
  const ctxT = document.getElementById('chart-traffic').getContext('2d');
  const gT = ctxT.createLinearGradient(0, 0, 0, 300);
  gT.addColorStop(0, 'rgba(112,112,245,0.28)');
  gT.addColorStop(1, 'rgba(112,112,245,0)');
  chartTraffic = new Chart(ctxT, {
    type: 'line',
    data: { labels: [], datasets: [
      { label: 'Usage', data: [], borderColor: t.brand, backgroundColor: gT, fill: true, tension: 0.35, pointRadius: 0, borderWidth: 2 },
      { label: 'Average', data: [], borderColor: t.warnFg, borderDash: [5, 4], borderWidth: 1.4, pointRadius: 0, fill: false, tension: 0 },
    ]},
    options: {
      responsive: true, maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: { legend: { display: false }, tooltip: { padding: 10, cornerRadius: 8 } },
      scales: {
        x: { grid: { display: false }, ticks: { color: t.fg3, font: { size: 10 } } },
        y: { grid: { color: t.line1 }, ticks: { color: t.fg3, font: { size: 10 }, callback: v => v + ' MB' } },
      },
    },
  });
}
function rebuildCharts(){
  if (chartHourly) chartHourly.destroy();
  if (chartDist) chartDist.destroy();
  if (chartTraffic) chartTraffic.destroy();
  initCharts();
}
function updateHourlyChart(hourly){
  if (!chartHourly) return;
  const labels = Object.keys(hourly).sort();
  const vals = labels.map(k => +(hourly[k] / 1024**2).toFixed(2));
  chartHourly.data.labels = labels;
  chartHourly.data.datasets[0].data = vals;
  chartHourly.update();
}
function updateTrafficChart(hourly){
  if (!chartTraffic) return;
  const labels = Object.keys(hourly).sort();
  const vals = labels.map(k => +(hourly[k] / 1024**2).toFixed(2));
  const avg = vals.length ? vals.reduce((a,b)=>a+b,0) / vals.length : 0;
  chartTraffic.data.labels = labels;
  chartTraffic.data.datasets[0].data = vals;
  chartTraffic.data.datasets[1].data = labels.map(() => +avg.toFixed(2));
  chartTraffic.update();
}

async function checkAuth(){
  try {
    const r = await fetch('/api/me');
    const d = await r.json();
    if (!d.authenticated) location.href = '/login';
  } catch (e) { location.href = '/login'; }
}
function logout(){
  fetch('/api/logout', {method: 'POST'}).finally(() => location.href = '/login');
}

async function refreshAll(){
  await refreshDefaultLink();
  await refreshOverview();
  const activePage = document.querySelector('.page.on');
  if (!activePage) return;
  const id = activePage.id.replace('page-', '');
  if (PAGE_LOADERS[id]) await PAGE_LOADERS[id]();
  toast('Refreshed', '', 'ok');
}

document.addEventListener('DOMContentLoaded', async () => {
  await checkAuth();
  initCharts();
  document.getElementById('set-host').textContent = location.host;
  await refreshDefaultLink();
  await refreshOverview();

  setInterval(async () => {
    if (document.visibilityState !== 'visible') return;
    const id = document.querySelector('.page.on')?.id;
    if (id === 'page-connections') loadConnections();
    else if (id === 'page-overview') refreshOverview();
  }, 5000);
});
</script>
</body>
</html>""".replace("__COMMON_CSS__", _COMMON_CSS)


_PUBLIC_PAGE_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>__NAME__ · Gateway</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
__COMMON_CSS__
body{
  background:
    radial-gradient(ellipse 600px 300px at 50% -8%, var(--brand-lo), transparent 62%),
    var(--bg-0);
  min-height: 100vh;
}
</style>
</head>
<body>

<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-mark">G</div>
      <div>
        <div class="brand-txt">Gateway</div>
        <div class="brand-ver">v12</div>
      </div>
    </div>
    <div class="top-actions">
      <button class="btn btn-secondary btn-icon btn-sm" onclick="toggleTheme()" aria-label="Toggle theme"><i class="ti ti-sun" id="theme-icon"></i></button>
    </div>
  </div>

  <div id="root">
    <div class="empty-hero"><div class="ic"><i class="ti ti-loader-2" style="animation:spin .8s linear infinite"></i></div><div class="text-sm text-muted">Loading…</div></div>
  </div>

  <div class="foot">Powered by Gateway v12</div>
</div>

<div class="modal-backdrop" id="modal-qr">
  <div class="modal" style="max-width:340px">
    <div class="modal-head">
      <div>
        <div class="modal-title" id="qr-title">Scan QR</div>
        <div class="modal-sub">Point your client at it.</div>
      </div>
      <button class="modal-close" onclick="closeModal('modal-qr')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body" style="align-items:center">
      <div class="qr-canvas"><img id="qr-img" src="" alt="QR"></div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-primary" onclick="copyQRLink()"><i class="ti ti-copy"></i> Copy link</button>
    </div>
  </div>
</div>

<div class="toast-host" id="toast-host"></div>

<script>
const UUID_KEY = '__UUID_KEY__';
let savedPw = '';
let currentData = null;

(function(){
  const saved = localStorage.getItem('gateway-pub-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  renderThemeIcon(saved);
})();
function renderThemeIcon(theme){
  const icon = document.getElementById('theme-icon');
  if (!icon) return;
  icon.className = 'ti ' + (theme === 'dark' ? 'ti-sun' : 'ti-moon');
}
function toggleTheme(){
  const cur = document.documentElement.getAttribute('data-theme');
  const next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('gateway-pub-theme', next);
  renderThemeIcon(next);
}

function esc(s){return String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function fmtB(b){
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if (b < 1024**3) return (b/1024**2).toFixed(2) + ' MB';
  return (b/1024**3).toFixed(2) + ' GB';
}
function daysLeft(exp){ if (!exp) return null; return Math.ceil((new Date(exp) - Date.now()) / 864e5); }
function toast(title, msg = '', level = 'info'){
  const host = document.getElementById('toast-host');
  const icons = { ok: 'ti-check', err: 'ti-x', warn: 'ti-alert-triangle', info: 'ti-info-circle' };
  const el = document.createElement('div');
  el.className = 'toast ' + level;
  el.innerHTML = `<div class="ic"><i class="ti ${icons[level] || icons.info}"></i></div><div class="body"><div class="ttl">${esc(title)}</div>${msg ? `<div class="msg">${esc(msg)}</div>` : ''}</div>`;
  host.appendChild(el);
  setTimeout(() => { el.classList.add('out'); setTimeout(() => el.remove(), 250); }, 2600);
}
function copyRaw(txt){ navigator.clipboard.writeText(txt).then(() => toast('Copied', '', 'ok')); }
function openModal(id){ document.getElementById(id).classList.add('open'); }
function closeModal(id){ document.getElementById(id).classList.remove('open'); }
document.querySelectorAll('.modal-backdrop').forEach(el => {
  el.addEventListener('click', e => { if (e.target === el) el.classList.remove('open'); });
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') document.querySelectorAll('.modal-backdrop.open').forEach(m => m.classList.remove('open'));
});

let qrText = '';
function showQR(label, text){
  qrText = text;
  document.getElementById('qr-title').textContent = label;
  document.getElementById('qr-img').src = 'https://api.qrserver.com/v1/create-qr-code/?size=440x440&data=' + encodeURIComponent(text);
  openModal('modal-qr');
}
function copyQRLink(){ if (qrText) copyRaw(qrText); }

async function fetchData(pw = ''){
  const url = '/api/public/sub/' + UUID_KEY + (pw ? '?pw=' + encodeURIComponent(pw) : '');
  const r = await fetch(url);
  return r.json();
}

function renderLock(name, errorMsg = ''){
  document.getElementById('root').innerHTML = `
    <div class="lock-wrap">
      <div class="lock-card">
        <div class="lock-icon-wrap"><i class="ti ti-lock"></i></div>
        <div class="lock-title">${esc(name)}</div>
        <div class="lock-sub">This sub-group is password-protected. Enter the password shared with you to continue.</div>
        <div class="lock-form">
          ${errorMsg ? `<div class="field-error" style="justify-content:center;margin-bottom:8px"><i class="ti ti-alert-circle"></i> ${esc(errorMsg)}</div>` : ''}
          <div class="input-wrap">
            <input class="input" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="trail" type="button" onclick="togglePw('lock-pw', this)" aria-label="Show"><i class="ti ti-eye"></i></button>
          </div>
          <button class="btn btn-primary" onclick="submitLock()"><i class="ti ti-lock-open"></i> Unlock</button>
        </div>
        <div class="lock-foot"><i class="ti ti-shield-check"></i> Secured by Gateway v12</div>
      </div>
    </div>
  `;
  const input = document.getElementById('lock-pw');
  input.addEventListener('keydown', e => { if (e.key === 'Enter') submitLock(); });
}

function togglePw(id, btn){
  const el = document.getElementById(id);
  const show = el.type === 'password';
  el.type = show ? 'text' : 'password';
  btn.querySelector('i').className = show ? 'ti ti-eye-off' : 'ti ti-eye';
}

async function submitLock(){
  const pw = document.getElementById('lock-pw').value;
  const data = await fetchData(pw);
  if (data.locked){ renderLock(data.name, 'Incorrect password'); return; }
  savedPw = pw;
  currentData = data;
  renderContent(data);
}

function renderContent(d){
  currentData = d;
  const activeCount = d.links.filter(l => l.active).length;
  const baseUrl = d.sub_url || (location.origin + '/sub-group/' + UUID_KEY);
  const subUrl = baseUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');

  window._links = d.links.map(l => ({
    vless: l.vless_link,
    sub: l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),
    label: l.label,
  }));

  document.getElementById('root').innerHTML = `
    <div class="hero">
      <div class="hero-eyebrow"><i class="ti ti-folders"></i> Shared access group</div>
      <div class="hero-title">${esc(d.name)}</div>
      ${d.desc ? `<div class="hero-desc">${esc(d.desc)}</div>` : ''}
      <div class="hero-meta"><i class="ti ti-clock"></i> Updated ${new Date().toLocaleTimeString()}</div>
      <div class="sub-pill">
        <span class="url">${esc(subUrl)}</span>
        <button class="btn btn-secondary btn-sm" onclick="copyRaw('${esc(subUrl)}')"><i class="ti ti-copy"></i> Copy</button>
        <button class="btn btn-secondary btn-sm" onclick="showQR('Group subscription', '${esc(subUrl)}')"><i class="ti ti-qrcode"></i> QR</button>
      </div>
    </div>

    <div class="stat-strip">
      <div class="metric-card">
        <div class="label"><i class="ti ti-key"></i> Active configs</div>
        <div class="value">${activeCount}</div>
        <div class="meta">of ${d.links.length}</div>
      </div>
      <div class="metric-card rail-ok">
        <div class="label"><i class="ti ti-plug-connected"></i> Connections</div>
        <div class="value">${d.active_connections}</div>
        <div class="meta"><span class="dot ok live"></span> live</div>
      </div>
      <div class="metric-card">
        <div class="label"><i class="ti ti-arrows-exchange"></i> Total used</div>
        <div class="value">${esc(d.total_used_fmt)}</div>
      </div>
    </div>

    <div class="cfg-title"><i class="ti ti-link"></i> Configs (${d.links.length})</div>
    <div class="cfg-grid">
      ${d.links.map((l, i) => renderPublicConfig(l, i)).join('')}
    </div>
  `;
  scheduleRefresh();
}

function renderPublicConfig(l, i){
  const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
  const fillClass = pct > 90 ? 'err' : pct > 70 ? 'warn' : '';
  const statusPill = l.active
    ? '<span class="status-pill online"><span class="dot ok live"></span> Active</span>'
    : '<span class="status-pill offline"><span class="dot err"></span> Inactive</span>';
  const protoBadge = l.protocol === 'vless-ws' ? '<span class="badge brand">VLESS · WS</span>'
    : l.protocol === 'xhttp-packet-up' ? '<span class="badge info">XHTTP · packet-up</span>'
    : '<span class="badge info">XHTTP · stream-up</span>';
  const dl = daysLeft(l.expires_at);
  const expLabel = !l.expires_at ? '<span class="meta"><i class="ti ti-infinity"></i> never</span>'
    : dl > 0 ? `<span class="meta"><i class="ti ti-calendar"></i> ${dl}d</span>`
    : '<span class="meta"><i class="ti ti-calendar-x"></i> expired</span>';
  const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
  return `
    <div class="config-card ${l.active ? '' : 'is-inactive'}">
      <div class="config-body">
        <div class="config-head">
          <div>
            <div class="config-name">${esc(l.label)}</div>
            <div class="config-uuid">${esc(l.uuid.slice(0, 16))}…</div>
          </div>
          ${statusPill}
        </div>
        <div class="config-tags">
          ${protoBadge}
          ${l.connections > 0 ? `<span class="badge ok">${l.connections} live</span>` : ''}
        </div>
        <div class="progress" style="margin-top:12px"><div class="fill ${fillClass}" style="width:${pct}%"></div></div>
        <div class="progress-meta">
          <span>${fmtB(l.used_bytes)} / ${lim}</span>
          <span>${pct.toFixed(0)}%</span>
        </div>
      </div>
      <div class="config-tear"></div>
      <div class="config-foot" style="flex-direction:column;align-items:stretch;gap:8px">
        <div class="meta" style="justify-content:space-between">
          <span><i class="ti ti-route"></i> :${l.port || 443}</span>
          ${expLabel}
        </div>
        <button class="cfg-link-toggle" onclick="toggleLink(${i}, this)">
          <span><i class="ti ti-eye"></i> Show config link</span>
          <i class="ti ti-chevron-down"></i>
        </button>
        <div class="cfg-link-wrap" id="link-wrap-${i}">
          <div class="cfg-link-inner">
            <div class="cfg-link">${esc(l.vless_link)}</div>
          </div>
        </div>
        <div class="row" style="gap:6px">
          <button class="btn btn-primary btn-sm" style="flex:1" onclick="copyRaw(window._links[${i}].vless)"><i class="ti ti-copy"></i> Copy</button>
          <button class="btn btn-secondary btn-sm" onclick="showQR(window._links[${i}].label, window._links[${i}].vless)"><i class="ti ti-qrcode"></i> QR</button>
        </div>
      </div>
    </div>
  `;
}

function toggleLink(i, btn){
  const wrap = document.getElementById('link-wrap-' + i);
  const isOpen = wrap.classList.toggle('open');
  btn.querySelector('span').innerHTML = isOpen
    ? '<i class="ti ti-eye-off"></i> Hide config link'
    : '<i class="ti ti-eye"></i> Show config link';
  const chevron = btn.querySelector('.ti-chevron-down, .ti-chevron-up');
  if (chevron) chevron.className = isOpen ? 'ti ti-chevron-up' : 'ti ti-chevron-down';
}

let refreshTimer = null;
function scheduleRefresh(){
  if (refreshTimer) clearTimeout(refreshTimer);
  refreshTimer = setTimeout(async () => {
    try {
      const data = await fetchData(savedPw);
      if (!data.locked) renderContent(data);
    } catch (e) {}
  }, 30000);
}

async function init(){
  try {
    const data = await fetchData();
    if (data.locked){ renderLock(data.name); return; }
    currentData = data;
    renderContent(data);
  } catch (e){
    document.getElementById('root').innerHTML = '<div class="empty-hero"><div class="ic" style="color:var(--err-fg)"><i class="ti ti-alert-circle"></i></div><div class="text-sm" style="color:var(--err-fg)">Failed to load</div></div>';
  }
}
init();
</script>
</body>
</html>"""


def get_public_page_html(uuid_key: str, name: str = "Shared access group") -> str:
    """Render the public sub-group page for a given UUID key."""
    html = _PUBLIC_PAGE_TEMPLATE.replace("__UUID_KEY__", uuid_key)
    html = html.replace("__NAME__", name)
    return html
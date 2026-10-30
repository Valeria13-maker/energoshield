from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
import pydantic
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="АСУ «ЭнергоЩит» — ЮЗЭС ПАО «Россети Кубань» (г. Новороссийск)"
)


class EnergyObject(BaseModel):
  id: int
  code: str
  name: str
  type: str  # "ПС", "ТП", "ВЛ", "Опора"
  zone: str
  voltage: str
  lat: float
  lng: float
  load_mw: float
  oil_temp: int
  wind_ms: int
  status: str
  crew: str
  consumers_cut: int


# База данных объектов: ПС 110кВ + 10 ТП с отходящими ВЛ 0,4 кВ и опорами
grid_db = [
    EnergyObject(
        id=1,
        code="ПС-110-КРЛ",
        name="ПС 110/35/6 кВ «Кирилловская»",
        type="ПС",
        zone="Приморский округ",
        voltage="110 кВ",
        lat=44.7562,
        lng=37.7345,
        load_mw=42.5,
        oil_temp=48,
        wind_ms=14,
        status="В сети",
        crew="Дежурный персонал ПС",
        consumers_cut=0,
    ),
    EnergyObject(
        id=2,
        code="ПС-110-ЮЖН",
        name="ПС 110/10 кВ «Южная»",
        type="ПС",
        zone="Южный район",
        voltage="110 кВ",
        lat=44.6785,
        lng=37.7810,
        load_mw=58.4,
        oil_temp=94,
        wind_ms=28,
        status="Аварийное откл.",
        crew="ОВБ-1 Новороссийский РЭС",
        consumers_cut=4200,
    ),
    EnergyObject(
        id=101,
        code="ТП-101",
        name="ТП-101 «Ул. Советов»",
        type="ТП",
        zone="Центральный район",
        voltage="10/0,4 кВ",
        lat=44.7150,
        lng=37.7720,
        load_mw=1.2,
        oil_temp=52,
        wind_ms=15,
        status="В сети",
        crew="Бригада ТП №1",
        consumers_cut=0,
    ),
    EnergyObject(
        id=102,
        code="ТП-104",
        name="ТП-104 «Пр. Ленина»",
        type="ТП",
        zone="Южный район",
        voltage="10/0,4 кВ",
        lat=44.6820,
        lng=37.7750,
        load_mw=2.1,
        oil_temp=88,
        wind_ms=25,
        status="Аварийное откл.",
        crew="ОВБ-2 Цемдолина",
        consumers_cut=310,
    ),
    EnergyObject(
        id=103,
        code="ТП-208",
        name="ТП-208 «Портовая»",
        type="ТП",
        zone="Восточный район",
        voltage="6/0,4 кВ",
        lat=44.7290,
        lng=37.8100,
        load_mw=3.4,
        oil_temp=91,
        wind_ms=25,
        status="Аварийное откл.",
        crew="ОВБ-3 Портовый РЭС",
        consumers_cut=450,
    ),
    EnergyObject(
        id=104,
        code="ТП-315",
        name="ТП-315 «Борисовка»",
        type="ТП",
        zone="Пригородный округ",
        voltage="10/0,4 кВ",
        lat=44.7600,
        lng=37.6950,
        load_mw=1.8,
        oil_temp=60,
        wind_ms=15,
        status="В сети",
        crew="Бригада Пригородная",
        consumers_cut=0,
    ),
    EnergyObject(
        id=105,
        code="ТП-410",
        name="ТП-410 «Мысхако»",
        type="ТП",
        zone="с. Мысхако",
        voltage="10/0,4 кВ",
        lat=44.6490,
        lng=37.7600,
        load_mw=2.5,
        oil_temp=55,
        wind_ms=15,
        status="В сети",
        crew="Штатная ТП",
        consumers_cut=0,
    ),
    EnergyObject(
        id=106,
        code="ТП-512",
        name="ТП-512 «Кирилловка-Север»",
        type="ТП",
        zone="Приморский округ",
        voltage="10/0,4 кВ",
        lat=44.7680,
        lng=37.7200,
        load_mw=1.6,
        oil_temp=50,
        wind_ms=15,
        status="В сети",
        crew="Бригада №4",
        consumers_cut=0,
    ),
    EnergyObject(
        id=107,
        code="ТП-620",
        name="ТП-620 «Цемдолина Промзона»",
        type="ТП",
        zone="с. Цемдолина",
        voltage="10/0,4 кВ",
        lat=44.7450,
        lng=37.7050,
        load_mw=3.1,
        oil_temp=58,
        wind_ms=15,
        status="В сети",
        crew="Бригада ЮЗЭС",
        consumers_cut=0,
    ),
    EnergyObject(
        id=108,
        code="ТП-714",
        name="ТП-714 «Шесхарис»",
        type="ТП",
        zone="Восточный район",
        voltage="10/0,4 кВ",
        lat=44.7190,
        lng=37.8350,
        load_mw=2.9,
        oil_temp=82,
        wind_ms=25,
        status="АВР / Ремонт",
        crew="ОВБ-3",
        consumers_cut=190,
    ),
    EnergyObject(
        id=109,
        code="ТП-822",
        name="ТП-822 «Мефодиевка»",
        type="ТП",
        zone="Восточный район",
        voltage="10/0,4 кВ",
        lat=44.7400,
        lng=37.7900,
        load_mw=2.2,
        oil_temp=53,
        wind_ms=15,
        status="В сети",
        crew="Бригада №2",
        consumers_cut=0,
    ),
    EnergyObject(
        id=110,
        code="ТП-905",
        name="ТП-905 «Гайдук Центр»",
        type="ТП",
        zone="с. Гайдук",
        voltage="10/0,4 кВ",
        lat=44.7800,
        lng=37.6900,
        load_mw=1.9,
        oil_temp=49,
        wind_ms=15,
        status="В сети",
        crew="Бригада Пригородная",
        consumers_cut=0,
    ),
    EnergyObject(
        id=201,
        code="ВЛ-04-101-1",
        name="ВЛ 0,4 кВ «Ф-1 от ТП-101»",
        type="ВЛ",
        zone="Центральный",
        voltage="0,4 кВ",
        lat=44.7162,
        lng=37.7735,
        load_mw=0.6,
        oil_temp=45,
        wind_ms=20,
        status="В сети",
        crew="ОВБ-1",
        consumers_cut=0,
    ),
    EnergyObject(
        id=202,
        code="ВЛ-04-101-2",
        name="ВЛ 0,4 кВ «Ф-2 от ТП-101»",
        type="ВЛ",
        zone="Центральный",
        voltage="0,4 кВ",
        lat=44.7138,
        lng=37.705,
        load_mw=0.6,
        oil_temp=45,
        wind_ms=20,
        status="В сети",
        crew="ОВБ-1",
        consumers_cut=0,
    ),
]

event_log = [
    {
        "time": "20:10:15",
        "msg": "АСУ «ЭнергоЩит» успешно инициализирована для ЮЗЭС (г. Новороссийск).",
    },
    {
        "time": "20:12:00",
        "msg": "Загружено 10+ ТП и отходящие фидеры ВЛ 0,4 кВ.",
    },
    {
        "time": "20:15:30",
        "msg": "Диспетчерский пункт: Контроль распределительной сети 0,4 кВ.",
    },
]


@app.get("/api/objects", response_model=list[EnergyObject])
def get_objects():
  return grid_db


@app.get("/api/logs")
def get_logs():
  return event_log


@app.post("/api/objects", response_model=EnergyObject)
def add_object(obj: EnergyObject):
  grid_db.append(obj)
  now = datetime.now().strftime("%H:%M:%S")
  event_log.insert(
      0, {"time": now, "msg": f"Новый объект [{obj.type}]: {obj.name}"}
  )
  return obj


@app.put("/api/objects/{obj_id}/operate")
def operate_object(obj_id: int, action: str):
  now = datetime.now().strftime("%H:%M:%S")
  for o in grid_db:
    if o.id == obj_id:
      if action == "dispatch":
        o.status = "АВР / Ремонт"
        event_log.insert(
            0,
            {
                "time": now,
                "msg": f"Наряд-допуск: {o.code} переведен в ремонт.",
            },
        )
      elif action == "restore":
        o.status = "В сети"
        o.oil_temp = 48
        o.consumers_cut = 0
        event_log.insert(
            0, {"time": now, "msg": f"АПВ выполнено: Объект {o.name} в работе."}
        )
      elif action == "alarm":
        o.status = "Аварийное откл."
        o.oil_temp = 96
        o.consumers_cut = 200
        event_log.insert(
            0,
            {"time": now, "msg": f"ТРЕВОГА РЗА: Отключение на {o.name}!"},
        )
      return {"ok": True}
  return {"ok": False}


@app.post("/api/weather_sim")
def simulate_weather(wind: int):
  now = datetime.now().strftime("%H:%M:%S")
  affected = 0
  for o in grid_db:
    o.wind_ms = wind
    if wind >= 30 and (o.type == "ВЛ" or o.id in (102, 103)):
      o.status = "Аварийное откл."
      o.consumers_cut = 350
      affected += 1
  event_log.insert(
      0,
      {
          "time": now,
          "msg": f"Шторм Норд-Ост ({wind} м/с): аварий ВЛ 0,4 кВ: {affected}.",
      },
  )
  return {"ok": True}


@app.get("/api/export_csv")
def export_csv():
  lines = [
      "Код;Наименование;Тип;Район;Напряжение;Статус;Нагрузка"
      " (МВт);Отключено абонентов;Бригада"
  ]
  for o in grid_db:
    lines.append(
        f"{o.code};{o.name};{o.type};{o.zone};{o.voltage};{o.status};{o.load_mw};{o.consumers_cut};{o.crew}"
    )
  content = "\ufeff" + "\n".join(lines)
  return PlainTextResponse(
      content=content,
      headers={
          "Content-Disposition": (
              "attachment; filename=yuzes_novorossiysk_grid.csv"
          )
      },
  )


HTML_PAGE = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>АСУ «ЭнергоЩит: ЮЗЭС» | ПАО «Россети Кубань»</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #090D16; --bg-panel: #111827; --bg-card: #1F2937;
            --border: #374151; --text: #F9FAFB; --muted: #9CA3AF;
            --brand-amber: #F59E0B; --brand-cyan: #06B6D4;
            --ok: #10B981; --warn: #F59E0B; --crit: #EF4444;
        }
        body.light {
            --bg-dark: #E2E8F0; --bg-panel: #FFFFFF; --bg-card: #F8FAFC;
            --border: #CBD5E1; --text: #0F172A; --muted: #475569;
        }
        body.large-font { font-size: 118% !important; }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
        body { background: var(--bg-dark); color: var(--text); padding: 10px; height: 100vh; display: flex; flex-direction: column; gap: 10px; overflow: hidden; }

        .topbar {
            background: var(--bg-panel); border: 1px solid var(--border); border-radius: 10px;
            padding: 8px 16px; display: flex; justify-content: space-between; align-items: center;
            border-bottom: 3px solid var(--brand-amber);
        }
        .brand { display: flex; align-items: center; gap: 12px; }
        .logo-box {
            background: linear-gradient(135deg, #F59E0B, #D97706); color: #000;
            font-weight: 800; padding: 6px 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 13px;
        }
        .brand h1 { font-size: 14px; }
        .brand p { font-size: 11px; color: var(--muted); }

        .kpi-row { display: flex; gap: 8px; }
        .kpi-box {
            background: var(--bg-card); border: 1px solid var(--border); padding: 4px 10px;
            border-radius: 6px; text-align: center; min-width: 100px;
        }
        .kpi-box span { display: block; font-size: 9px; color: var(--muted); text-transform: uppercase; }
        .kpi-box strong { font-size: 13px; font-family: 'JetBrains Mono', monospace; color: var(--brand-cyan); }
        .kpi-box.danger strong { color: var(--crit); }

        .top-actions button, .top-actions a {
            background: var(--bg-card); color: var(--text); border: 1px solid var(--border);
            padding: 6px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; text-decoration: none; cursor: pointer; margin-left: 4px;
        }
        .top-actions button:hover, .top-actions a:hover { border-color: var(--brand-amber); color: var(--brand-amber); }

        .workspace { display: grid; grid-template-columns: 280px 1fr 360px; gap: 10px; flex: 1; min-height: 0; }
        .panel { background: var(--bg-panel); border: 1px solid var(--border); border-radius: 10px; padding: 10px; display: flex; flex-direction: column; gap: 8px; min-height: 0; }
        .panel-title { font-size: 11px; font-weight: 700; color: var(--brand-amber); text-transform: uppercase; border-bottom: 1px solid var(--border); padding-bottom: 4px; display: flex; justify-content: space-between; }

        .sim-box { background: var(--bg-card); padding: 8px; border-radius: 6px; border-left: 3px solid var(--brand-cyan); }
        .sim-box label { font-size: 11px; font-weight: 600; display: flex; justify-content: space-between; margin-bottom: 4px; }
        .sim-box input[type=range] { width: 100%; accent-color: var(--brand-amber); cursor: pointer; }
        .btn-full { width: 100%; padding: 6px; border-radius: 5px; border: none; font-weight: 700; font-size: 11px; cursor: pointer; margin-top: 6px; background: var(--brand-amber); color: #000; }

        .filter-buttons { display: flex; gap: 4px; flex-wrap: wrap; }
        .filter-btn { background: var(--bg-card); border: 1px solid var(--border); color: var(--text); padding: 3px 6px; border-radius: 4px; font-size: 10px; cursor: pointer; }
        .filter-btn.active { background: var(--brand-cyan); color: #000; font-weight: 700; border-color: var(--brand-cyan); }

        .log-box { flex: 1; background: #05080F; border: 1px solid var(--border); border-radius: 5px; padding: 6px; overflow-y: auto; font-family: 'JetBrains Mono', monospace; font-size: 10px; }
        .log-entry { margin-bottom: 4px; border-bottom: 1px dashed #1E293B; padding-bottom: 3px; line-height: 1.3; }
        .log-time { color: var(--brand-amber); margin-right: 4px; }

        #map { width: 100%; height: 100%; min-height: 420px; border-radius: 6px; border: 1px solid var(--border); z-index: 1; }

        .safety-bar { background: var(--bg-card); padding: 8px; border-radius: 6px; display: flex; justify-content: space-between; align-items: center; border-left: 3px solid var(--ok); font-size: 11px; }
        .safety-checks { display: flex; gap: 8px; font-size: 10px; align-items: center; }

        .sub-list { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 6px; padding-right: 4px; }
        .sub-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 6px; padding: 8px; border-left: 3px solid var(--ok); }
        .sub-card.st-crit { border-left-color: var(--crit); background: rgba(239, 68, 68, 0.08); }
        .sub-card.st-warn { border-left-color: var(--warn); }
        .sub-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px; }
        .sub-header h3 { font-size: 11px; }
        .type-badge { font-family: 'JetBrains Mono', monospace; font-size: 9px; background: rgba(6, 182, 212, 0.2); color: var(--brand-cyan); padding: 2px 5px; border-radius: 3px; }
        .sub-meta { font-size: 10px; color: var(--muted); margin-bottom: 4px; }
        .sub-actions { display: flex; gap: 4px; }
        .sub-actions button { flex: 1; padding: 4px; border: none; border-radius: 3px; font-size: 10px; font-weight: 700; cursor: pointer; color: #fff; }
        .b-work { background: var(--warn); color: #000 !important; }
        .b-ok { background: var(--ok); }
        .b-err { background: var(--crit); }

        .mini-form { display: grid; grid-template-columns: 1fr 1fr; gap: 4px; padding-top: 4px; border-top: 1px solid var(--border); }
        .mini-form input, .mini-form select { background: var(--bg-card); color: var(--text); border: 1px solid var(--border); padding: 5px; border-radius: 4px; font-size: 10px; }
        .mini-form button { grid-column: span 2; background: var(--brand-cyan); color: #000; font-weight: 700; border: none; padding: 6px; border-radius: 4px; cursor: pointer; font-size: 11px; }
    </style>
</head>
<body>

<div class="topbar">
    <div class="brand">
        <div class="logo-box">ЮЗЭС • РФ</div>
        <div>
            <h1>АСУ «ЭНЕРГОЩИТ» — НОВОРОССИЙСК</h1>
            <p>Ситуационный центр ПАО «Россети Кубань» (Юго-Западные электрические сети)</p>
        </div>
    </div>
    <div class="kpi-row">
        <div class="kpi-box"><span>Объектов</span><strong id="kpi-total">0</strong></div>
        <div class="kpi-box danger"><span>Без света</span><strong id="kpi-cut">0 чел.</strong></div>
        <div class="kpi-box"><span>Аварий</span><strong id="kpi-alarms">0</strong></div>
    </div>
    <div class="top-actions">
        <a href="/api/export_csv" download>📥 Скачать CSV</a>
        <button onclick="document.body.classList.toggle('light')">🌗 Тема</button>
        <button onclick="document.body.classList.toggle('large-font')">🔍 Шрифт</button>
    </div>
</div>

<div class="workspace">
    <div class="panel">
        <div class="panel-title"><span>🌪️ Тренажер «Норд-Ост»</span><span>Бора</span></div>
        <div class="sim-box">
            <label><span>Скорость ветра:</span><strong id="wind-val">24 м/с</strong></label>
            <input type="range" id="wind-slider" min="5" max="42" value="24" oninput="document.getElementById('wind-val').innerText = this.value + ' м/с'">
            <button class="btn-full" onclick="applyWeather()">Моделировать штормовой удар</button>
        </div>

        <div class="panel-title"><span>🔍 Фильтр объектов (Слои)</span><span>Сети</span></div>
        <div class="filter-buttons">
            <button class="filter-btn active" onclick="setFilter('ALL', this)">Все</button>
            <button class="filter-btn" onclick="setFilter('ПС', this)">ПС 110кВ</button>
            <button class="filter-btn" onclick="setFilter('ТП', this)">ТП 10/6кВ</button>
            <button class="filter-btn" onclick="setFilter('ВЛ', this)">ВЛ 0,4кВ</button>
        </div>

        <div class="panel-title"><span>📟 Журнал диспетчера РЗА</span><span>Live</span></div>
        <div class="log-box" id="log-container"></div>
    </div>

    <div class="panel">
        <div class="panel-title">
            <span>🗺️ Схема распределительных сетей (ТП и линии 0,4 кВ)</span>
            <span style="font-size:10px; color:var(--brand-cyan);">ЮЗЭС</span>
        </div>
        <div id="map"></div>
        <div class="safety-bar">
            <div>
                <b style="color:var(--ok); display:block;">🛡️ Контроль ТБ при выдаче наряда-допуска</b>
                <span style="font-size:10px; color:var(--muted);">Требования перед допуском ОВБ к ТП/ВЛ:</span>
            </div>
            <div class="safety-checks">
                <label><input type="checkbox" id="chk1" checked> 1. Откл.</label>
                <label><input type="checkbox" id="chk2" checked> 2. Плакаты</label>
                <label><input type="checkbox" id="chk3" checked> 3. ПЗ (Заземление)</label>
            </div>
        </div>
    </div>

    <div class="panel">
        <div class="panel-title"><span>⚡ Реестр узлов и фидеров (ЮЗЭС)</span><span id="obj-count">0</span></div>
        <div class="sub-list" id="objs-container"></div>

        <form class="mini-form" onsubmit="createObject(event)">
            <input type="text" id="n_name" placeholder="Название (напр. ТП-115)" required>
            <input type="text" id="n_zone" placeholder="Район / Улица" required>
            <select id="n_type">
                <option value="ТП">ТП 10/6 кВ</option>
                <option value="ВЛ">ВЛ 0,4 кВ (Фидер)</option>
            </select>
            <select id="n_crew">
                <option value="ОВБ-1 Новороссийский РЭС">ОВБ-1 (Новороссийский РЭС)</option>
                <option value="ОВБ-2 Цемдолина">ОВБ-2 (Цемдолина)</option>
                <option value="ОВБ-3 Служба ВЛ">ОВБ-3 (Служба ВЛ)</option>
            </select>
            <button type="submit">➕ Добавить узел в сеть</button>
        </form>
    </div>
</div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
    const map = L.map('map').setView([44.7239, 37.7685], 12);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors | ПАО «Россети Кубань» ЮЗЭС'
    }).addTo(map);

    let mapLayers = [];
    let currentFilter = 'ALL';

    function setFilter(type, btn) {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = type;
        loadData();
    }

    function statusColor(st) {
        if (st === 'Аварийное откл.') return '#EF4444';
        if (st === 'АВР / Ремонт') return '#F59E0B';
        return '#10B981';
    }

    async function loadData() {
        const res = await fetch('/api/objects');
        const objects = await res.json();
        const logsRes = await fetch('/api/logs');
        const logs = await logsRes.json();

        mapLayers.forEach(l => map.removeLayer(l));
        mapLayers = [];

        const container = document.getElementById('objs-container');
        container.innerHTML = '';

        let totalCut = 0;
        let alarms = 0;
        let displayedCount = 0;

        objects.forEach(o => {
            if (o.status !== 'В сети') alarms++;
            totalCut += o.consumers_cut;

            if (currentFilter !== 'ALL' && o.type !== currentFilter) return;
            displayedCount++;

            let markerRadius = o.type === 'ПС' ? 13 : (o.type === 'ТП' ? 9 : 6);
            const marker = L.circleMarker([o.lat, o.lng], {
                radius: markerRadius,
                fillColor: statusColor(o.status),
                color: '#090D16',
                weight: 2,
                fillOpacity: 0.95
            }).addTo(map);

            marker.bindPopup(
                '<b>[' + o.code + '] ' + o.name + '</b><br>' +
                'Тип: ' + o.type + ' | Класс: ' + o.voltage + '<br>' +
                'Район: ' + o.zone + '<br>' +
                'Нагрузка: <b>' + o.load_mw + ' МВт</b> | Ветер: ' + o.wind_ms + ' м/с<br>' +
                'Статус: <b>' + o.status + '</b><br>' +
                'Бригада: ' + o.crew
            );
            mapLayers.push(marker);

            let cardCls = 'sub-card';
            if (o.status === 'Аварийное откл.') cardCls += ' st-crit';
            else if (o.status === 'АВР / Ремонт') cardCls += ' st-warn';

            let actionsHtml = '';
            if (o.status === 'Аварийное откл.') {
                actionsHtml += '<button class="b-work" onclick="operate(' + o.id + ', \\'dispatch\\')">Ремонт</button>';
            }
            if (o.status !== 'В сети') {
                actionsHtml += '<button class="b-ok" onclick="operate(' + o.id + ', \\'restore\\')">Включить</button>';
            } else {
                actionsHtml += '<button class="b-err" onclick="operate(' + o.id + ', \\'alarm\\')">Откл</button>';
            }

            const card = document.createElement('div');
            card.className = cardCls;
            card.innerHTML =
                '<div class="sub-header"><h3>' + o.name + '</h3><span class="type-badge">' + o.type + '</span></div>' +
                '<div class="sub-meta">📍 ' + o.zone + ' • ⚡ ' + o.voltage + '</div>' +
                '<div class="sub-actions">' + actionsHtml + '</div>';
            container.appendChild(card);
        });

        document.getElementById('kpi-total').innerText = objects.length;
        document.getElementById('kpi-cut').innerText = totalCut + ' чел.';
        document.getElementById('kpi-alarms').innerText = alarms;
        document.getElementById('obj-count').innerText = displayedCount + ' из ' + objects.length;

        const logBox = document.getElementById('log-container');
        logBox.innerHTML = logs.map(l => '<div class="log-entry"><span class="log-time">[' + l.time + ']</span>' + l.msg + '</div>').join('');

        setTimeout(() => { map.invalidateSize(); }, 200);
    }

    async function operate(id, action) {
        if (action === 'dispatch') {
            const c1 = document.getElementById('chk1').checked;
            const c2 = document.getElementById('chk2').checked;
            const c3 = document.getElementById('chk3').checked;
            if (!c1 || !c2 || !c3) {
                alert('ОШИБКА ТБ: Выполните все требования безопасности перед допуском ОВБ!');
                return;
            }
        }
        await fetch('/api/objects/' + id + '/operate?action=' + action, { method: 'PUT' });
        loadData();
    }

    async function applyWeather() {
        const w = document.getElementById('wind-slider').value;
        await fetch('/api/weather_sim?wind=' + w, { method: 'POST' });
        loadData();
    }

    async function createObject(e) {
        e.preventDefault();
        const t = document.getElementById('n_type').value;
        const payload = {
            id: Math.floor(Math.random() * 9000) + 1000,
            code: t + '-' + Math.floor(Math.random() * 900 + 100),
            name: document.getElementById('n_name').value,
            type: t,
            zone: document.getElementById('n_zone').value,
            voltage: t === 'ПС' ? '110 кВ' : (t === 'ВЛ' ? '0,4 кВ' : '10/0,4 кВ'),
            lat: 44.70 + (Math.random() * 0.07),
            lng: 37.71 + (Math.random() * 0.08),
            load_mw: 0.5,
            oil_temp: 45,
            wind_ms: 25,
            status: 'Аварийное откл.',
            crew: document.getElementById('n_crew').value,
            consumers_cut: 120
        };
        await fetch('/api/objects', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        document.getElementById('n_name').value = '';
        document.getElementById('n_zone').value = '';
        loadData();
    }

    loadData();
</script>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
def index():
  return HTML_PAGE


if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000)
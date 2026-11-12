# -*- coding: utf-8 -*-
"""
Simulasi Hidrolika (Darcy-Weisbach), Neraca Energi Surya (PV + LiFePO4),
dan Pembangkitan 5 Gambar Teknik untuk CD-3 Jeruk Limau Ciberes.

Dijalankan secara deterministik agar seluruh angka pada Tabel Perbandingan
dan Dokumen CD-3 konsisten dengan luaran perhitungan numerik.
"""

import os
import json
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# ==============================================================================
# 1. PARAMETER FISIK & SIMULASI HIDROLIKA (DARCY-WEISBACH)
# ==============================================================================
RHO = 996.2          # kg/m3 pada suhu air Tropis ~28 C
G = 9.81             # m/s2
MU = 8.32e-4         # Pa.s
NU = MU / RHO        # m2/s (~8.35e-7)
EPS_PE = 1.5e-6      # m (kekasaran absolut pipa polietilena HDPE/LDPE halus)

ID_MAIN = 0.0250     # m (pipa PE 1 inci nominal, ID ~25.0 mm)
ID_LAT = 0.0136      # m (pipa lateral LDPE 16 mm, tebal 1.2 mm -> ID 13.6 mm)

L_RIVER_TO_FIELD = 20.54   # m (jarak Sungai Ciberes ke kebun sesuai CD-1)
L_HEADER_PORTION = 10.0    # m (header manifold melewati parit melintang)
L_MAIN_TOTAL = L_RIVER_TO_FIELD + L_HEADER_PORTION  # ~30.54 m
L_LAT = 20.0               # m (rencana awal petak uji 20 m x 3 baris, pra-survei)
DELTA_Z_SUCTION_MANIFOLD = 1.50  # m (beda elevasi muka air sungai - bedengan)

K_MAIN_MINOR = 6.2   # foot valve/strainer (2.2), 2x elbow 90 (1.8), tee (1.0), flow sensor + valve (1.2)
K_LAT_MINOR = 2.0    # take-off grommet + tee/elbow

Q_EMITTER_TOTAL_PER_TREE = 16.0  # L/jam (2x PC Dripper 8 L/jam per pohon)
DOSE_TARGET_L = 15.0             # L/pohon (acuan mitra CD-1/CD-2)
T_IRRIG_MIN = (DOSE_TARGET_L / Q_EMITTER_TOTAL_PER_TREE) * 60.0  # 56.25 menit


def swamee_jain_f(re, d_m, eps=EPS_PE):
    if re <= 0:
        return 0.0
    if re < 2300:
        return 64.0 / re
    term = (eps / (3.7 * d_m)) + (5.74 / (re ** 0.9))
    return 0.25 / (math.log10(term) ** 2)


def pipe_head_loss_m(q_m3s, length_m, d_m, k_minor=0.0):
    if q_m3s <= 0:
        return 0.0, 0.0, 0.0
    area = math.pi * (d_m ** 2) / 4.0
    vel = q_m3s / area
    re = vel * d_m / NU
    f = swamee_jain_f(re, d_m)
    hf_friction = f * (length_m / d_m) * (vel ** 2) / (2.0 * G)
    hf_minor = k_minor * (vel ** 2) / (2.0 * G)
    return hf_friction + hf_minor, vel, re


def compute_hydraulics():
    # Skenario uji aliran lateral (Christansen F-factor ~0.39 untuk N=8-10 outlet seragam sepanjang 20 m)
    F_CHRISTIANSEN_8 = 0.391
    # Kerugian filter cakram 120-150 mesh (124 um) terkalibrasi dari literatur Z-09 (clean ~0.18 bar -> bilas threshold 0.70 bar)
    p_filter_clean_bar = 0.20
    p_filter_trigger_bar = 0.70
    p_dripper_min_bar = 0.7845  # 78.45 kPa (ambang kestabilan Z-19 / 34_JEE_2023)
    p_dripper_nom_bar = 1.00    # 100 kPa target desain nominal untuk PC 8 L/h

    configs = [
        {"name": "1 Zona Aktif (8 pohon / 1 baris)", "trees": 8, "active_laterals": 1},
        {"name": "2 Zona Aktif (16 pohon / 2 baris)", "trees": 16, "active_laterals": 2},
        {"name": "3 Baris Serentak (24 pohon / petak 20x3m)", "trees": 24, "active_laterals": 3},
        {"name": "Uji C-03 Maks (20 pohon / 1 baris 25m)", "trees": 20, "active_laterals": 1},
        {"name": "Mode End-Flush 1 Lateral (v=0.80 m/s)", "trees": 0, "active_laterals": 1, "flush_v": 0.80},
    ]

    results = []
    for cfg in configs:
        if cfg.get("flush_v"):
            v_target = cfg["flush_v"]
            q_total_m3s = v_target * (math.pi * (ID_LAT ** 2) / 4.0)
            q_total_lh = q_total_m3s * 3600000.0
            f_christ = 1.0  # aliran penuh sampai ujung pipa saat keran flush dibuka
        else:
            q_total_lh = cfg["trees"] * Q_EMITTER_TOTAL_PER_TREE
            q_total_m3s = q_total_lh / 3600000.0
            f_christ = F_CHRISTIANSEN_8

        hf_main, v_main, re_main = pipe_head_loss_m(q_total_m3s, L_MAIN_TOTAL, ID_MAIN, K_MAIN_MINOR)
        q_lat_m3s = q_total_m3s / cfg["active_laterals"]
        hf_lat_full, v_lat, re_lat = pipe_head_loss_m(q_lat_m3s, L_LAT, ID_LAT, K_LAT_MINOR)
        hf_lat = hf_lat_full * f_christ

        # Total head statis + gesek + minor (belum termasuk tekanan kerja ujung & filter)
        h_pipe_total_m = DELTA_Z_SUCTION_MANIFOLD + hf_main + hf_lat
        p_pipe_total_bar = (RHO * G * h_pipe_total_m) / 1e5

        if cfg.get("flush_v"):
            p_req_clean_bar = p_pipe_total_bar + p_filter_clean_bar + 0.15  # residual flush head 0.15 bar
            p_req_dirty_bar = p_pipe_total_bar + p_filter_trigger_bar + 0.15
        else:
            p_req_clean_bar = p_pipe_total_bar + p_filter_clean_bar + p_dripper_nom_bar
            p_req_dirty_bar = p_pipe_total_bar + p_filter_trigger_bar + p_dripper_nom_bar

        results.append({
            "name": cfg["name"],
            "trees": cfg["trees"],
            "active_laterals": cfg["active_laterals"],
            "Q_L_h": round(q_total_lh, 1),
            "Q_L_min": round(q_total_lh / 60.0, 2),
            "v_main_ms": round(v_main, 3),
            "v_lat_inlet_ms": round(v_lat, 3),
            "hf_main_m": round(hf_main, 3),
            "hf_lat_m": round(hf_lat, 3),
            "P_pipe_plus_elev_bar": round(p_pipe_total_bar, 3),
            "P_pump_clean_bar": round(p_req_clean_bar, 3),
            "P_pump_dirty_filter_bar": round(p_req_dirty_bar, 3),
            "passes_scour_06ms": v_lat >= 0.60,
        })

    # Kurva tekanan akhir lateral vs debit pada lateral 20 m untuk plot
    q_sweep_lh = np.linspace(50, 500, 100)
    v_lat_sweep = []
    p_pump_curve_clean = []
    p_pump_curve_dirty = []
    for q_lh in q_sweep_lh:
        q_m3s = q_lh / 3600000.0
        # Asumsi 3 baris paralel saat debit > 256 L/h atau 1 lateral saat mode flush/zona tunggal
        hf_m, _, _ = pipe_head_loss_m(q_m3s, L_MAIN_TOTAL, ID_MAIN, K_MAIN_MINOR)
        hf_l, v_l, _ = pipe_head_loss_m(q_m3s, L_LAT, ID_LAT, K_LAT_MINOR)
        h_total_1lat = DELTA_Z_SUCTION_MANIFOLD + hf_m + hf_l * F_CHRISTIANSEN_8
        p_1lat_bar = (RHO * G * h_total_1lat) / 1e5
        v_lat_sweep.append(v_l)
        p_pump_curve_clean.append(p_1lat_bar + p_filter_clean_bar + p_dripper_nom_bar)
        p_pump_curve_dirty.append(p_1lat_bar + p_filter_trigger_bar + p_dripper_nom_bar)

    return {
        "configs": results,
        "sweep": {
            "q_lh": [round(float(x), 1) for x in q_sweep_lh],
            "v_lat_1lat_ms": [round(float(x), 3) for x in v_lat_sweep],
            "p_pump_clean_bar": [round(float(x), 3) for x in p_pump_curve_clean],
            "p_pump_dirty_bar": [round(float(x), 3) for x in p_pump_curve_dirty],
        },
        "thresholds": {
            "p_dripper_min_kpa": 78.45,
            "v_scour_min_ms": 0.60,
            "t_irrig_min": T_IRRIG_MIN,
            "p_filter_flush_trigger_kpa": 70.0,
        }
    }


# ==============================================================================
# 2. SIMULASI NERACA ENERGI SURYA (100 Wp PV + LiFePO4 12.8V 30Ah)
# ==============================================================================
def compute_energy():
    pv_wp = 100.0
    psh_sunny = 4.5          # jam ekivalen puncak Jawa Barat
    psh_cloudy = 1.5         # skenario mendung berat (~33% cerah)
    eta_temp = 1.0 - 0.1422  # penalti termal siang hari 14.22% (34_JEE_2023 / Z-19)
    eta_mppt_wire = 0.86     # MPPT 0.94 * kabel/debu 0.915
    eta_sys = eta_temp * eta_mppt_wire  # ~0.738

    e_gen_sunny_wh = pv_wp * psh_sunny * eta_sys
    e_gen_cloudy_wh = pv_wp * psh_cloudy * eta_sys

    bat_v = 12.8
    bat_ah = 30.0
    bat_nom_wh = bat_v * bat_ah        # 384 Wh
    bat_dod = 0.80
    bat_usable_wh = bat_nom_wh * bat_dod  # 307.2 Wh

    # Beban per siklus (24 pohon petak uji 20m x 3 baris, 15 L/pohon = 360 L)
    # Catatan perbandingan operasi:
    # A) 3 Zona Bergantian (masing-masing 56.25 menit = 2.8125 jam total), pompa ~65 W (head sedang)
    # B) 3 Baris Serentak (1x 56.25 menit = 0.9375 jam total), pompa ~88 W (debit 6.4 L/min @ ~1.4 bar)
    p_ctrl_sleep_w = 0.025  # ESP32 deep sleep + DS3231 + sensor MOSFET-gated OFF (25 mW)
    p_ctrl_active_w = 1.50  # ESP32 aktif + flow/pressure/soil ADC

    # Skenario A: 3 Zona Bergantian + Motorized Ball Valve (0 W statis, 5 dtk @ 4 W per buka/tutup)
    t_3zone_h = 3 * (T_IRRIG_MIN / 60.0)  # 2.8125 jam
    e_pump_3zone_wh = 65.0 * t_3zone_h
    e_valve_mbv_wh = 3 * 2 * (4.0 * 5.0 / 3600.0)  # ~0.033 Wh
    e_valve_nc_sol_wh = 12.0 * t_3zone_h           # 33.75 Wh (konstan ditahan 12W!)
    e_ctrl_72h_wh = p_ctrl_active_w * t_3zone_h + p_ctrl_sleep_w * (72.0 - t_3zone_h)

    e_cycle_3zone_mbv_wh = e_pump_3zone_wh + e_valve_mbv_wh + e_ctrl_72h_wh
    e_cycle_3zone_nc_wh = e_pump_3zone_wh + e_valve_nc_sol_wh + e_ctrl_72h_wh

    # Skenario B: Operasi Cepat 3 Baris Serentak (uji petak 24 pohon @ 384 L/h) + Motorized Ball Valve
    t_1step_h = T_IRRIG_MIN / 60.0        # 0.9375 jam
    e_pump_simul_wh = 88.0 * t_1step_h    # 82.50 Wh
    e_ctrl_simul_72h_wh = p_ctrl_active_w * t_1step_h + p_ctrl_sleep_w * (72.0 - t_1step_h)
    e_cycle_simul_mbv_wh = e_pump_simul_wh + e_valve_mbv_wh + e_ctrl_simul_72h_wh

    return {
        "pv_wp": pv_wp,
        "eta_sys_pct": round(eta_sys * 100.0, 1),
        "e_gen_sunny_wh_day": round(e_gen_sunny_wh, 1),
        "e_gen_cloudy_wh_day": round(e_gen_cloudy_wh, 1),
        "bat_nom_wh": round(bat_nom_wh, 1),
        "bat_usable_wh": round(bat_usable_wh, 1),
        "e_cycle_3zone_mbv_wh": round(e_cycle_3zone_mbv_wh, 2),
        "e_cycle_3zone_nc_wh": round(e_cycle_3zone_nc_wh, 2),
        "e_valve_mbv_wh": round(e_valve_mbv_wh, 4),
        "e_valve_nc_wh": round(e_valve_nc_sol_wh, 2),
        "valve_saving_pct": round((1.0 - e_valve_mbv_wh / e_valve_nc_sol_wh) * 100.0, 2),
        "e_cycle_simul_mbv_wh": round(e_cycle_simul_mbv_wh, 2),
        "cycles_autonomy_3zone_mbv": round(bat_usable_wh / e_cycle_3zone_mbv_wh, 2),
        "cycles_autonomy_simul_mbv": round(bat_usable_wh / e_cycle_simul_mbv_wh, 2),
        "days_autonomy_3d_interval_3zone": round((bat_usable_wh / e_cycle_3zone_mbv_wh) * 3.0, 1),
        "days_autonomy_3d_interval_simul": round((bat_usable_wh / e_cycle_simul_mbv_wh) * 3.0, 1),
    }


# ==============================================================================
# 3. PEMBANGKITAN 5 GAMBAR TEKNIK HIGH-RES
# ==============================================================================
plt.rcParams["font.family"] = "DejaVu Sans"


def draw_fig1_arsitektur():
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 62)
    ax.axis("off")

    ax.text(50, 59.5, "ARSITEKTUR SISTEM MIKRO-IRIGASI TETES TERZONASI MANDIRI SURYA",
            ha="center", va="center", fontsize=12.5, fontweight="bold", color="#0F172A")
    ax.text(50, 56.8, "Integrasi Tiga Domain: Energi Off-Grid SELV 12 V, Hidrolika Terfiltrasi, dan Kendali Tertanam ESP32",
            ha="center", va="center", fontsize=9.2, color="#475569")

    # Domain 1: Energi Surya (Kiri Atas)
    d1 = FancyBboxPatch((2, 34), 30, 20, boxstyle="round,pad=0.6", facecolor="#FFFBEB", edgecolor="#D97706", linewidth=1.6)
    ax.add_patch(d1)
    ax.text(17, 52.2, "DOMAIN 1: CATU DAYA SELV 12 V", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#B45309")

    boxes_d1 = [
        (4, 44.5, 12, 5.5, "Panel Surya\n100 Wp Mono"),
        (18, 44.5, 12, 5.5, "MPPT Controller\n12 V / 10 A"),
        (4, 35.8, 12, 5.5, "Baterai LiFePO4\n12,8 V 30 Ah (384 Wh)"),
        (18, 35.8, 12, 5.5, "Buck/LDO 3,3 V + 5 V\n& Interlock < 11,5 V"),
    ]
    for x, y, w, h, txt in boxes_d1:
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", facecolor="white", edgecolor="#F59E0B", linewidth=1.1)
        ax.add_patch(b)
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.8, color="#1E293B")

    ax.annotate("", xy=(18, 47.2), xytext=(16, 47.2), arrowprops=dict(arrowstyle="->", color="#B45309", lw=1.4))
    ax.annotate("", xy=(10, 41.3), xytext=(22, 44.5), arrowprops=dict(arrowstyle="<->", color="#B45309", lw=1.3))
    ax.annotate("", xy=(24, 41.3), xytext=(24, 44.5), arrowprops=dict(arrowstyle="->", color="#B45309", lw=1.4))

    # Domain 2: Kendali & Sensor (Tengah)
    d2 = FancyBboxPatch((35, 21), 30, 33, boxstyle="round,pad=0.6", facecolor="#EFF6FF", edgecolor="#2563EB", linewidth=1.6)
    ax.add_patch(d2)
    ax.text(50, 52.2, "DOMAIN 2: KENDALI & INSTRUMENTASI IP65", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#1D4ED8")

    b_esp = FancyBboxPatch((40, 39), 20, 9.5, boxstyle="round,pad=0.4", facecolor="#DBEAFE", edgecolor="#1D4ED8", linewidth=1.4)
    ax.add_patch(b_esp)
    ax.text(50, 43.8, "Mikrokontroler ESP32\n(FSM Dosis Volume & Jadwal)\nRTC DS3231 + Tombol 1-Sentuhan",
            ha="center", va="center", fontsize=8.0, fontweight="bold", color="#1E3A8A")

    b_sens = FancyBboxPatch((37, 29.5), 26, 7.2, boxstyle="round,pad=0.3", facecolor="white", edgecolor="#3B82F6", linewidth=1.1)
    ax.add_patch(b_sens)
    ax.text(50, 33.1, "Sensor Umpan Balik Tertutup:\n- Flow Meter YF-S201 (Dosis L/pohon)\n- Transduser Tekanan 0-5 bar (Filter & Pipa)\n- Kelembapan Tanah Capacitive v1.2 (Mod RC+MOSFET)",
            ha="center", va="center", fontsize=7.3, color="#1E293B")

    b_drv = FancyBboxPatch((37, 22.3), 26, 5.5, boxstyle="round,pad=0.3", facecolor="white", edgecolor="#3B82F6", linewidth=1.1)
    ax.add_patch(b_drv)
    ax.text(50, 25.0, "Driver Aktuator Isolasi:\nMOSFET Pompa (>30 s jeda) & Modul H-Bridge\nMotorized Ball Valve (0 W Statis)",
            ha="center", va="center", fontsize=7.4, color="#1E293B")

    ax.annotate("", xy=(50, 39), xytext=(50, 36.7), arrowprops=dict(arrowstyle="<-", color="#1D4ED8", lw=1.3))
    ax.annotate("", xy=(50, 27.8), xytext=(50, 29.5), arrowprops=dict(arrowstyle="->", color="#1D4ED8", lw=1.3))

    # Domain 3: Hidrolika & Kebun (Bawah & Kanan)
    d3 = FancyBboxPatch((68, 21), 30, 33, boxstyle="round,pad=0.6", facecolor="#ECFDF5", edgecolor="#059669", linewidth=1.6)
    ax.add_patch(d3)
    ax.text(83, 52.2, "DOMAIN 3: HIDROLIKA & LAPANGAN", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#047857")

    boxes_d3 = [
        (70, 44.5, 26, 5.2, "1. Sungai Ciberes (20,54 m) + Saringan Hisap\nNon-Korosif Pra-Pompa + Foot Valve"),
        (70, 37.5, 26, 5.2, "2. Pompa DC 12 V (Non-Besi Cor) + Disc Filter\n120-150 Mesh + Flush Manual (dP >= 70 kPa)"),
        (70, 30.2, 26, 5.5, "3. Header PE 1\" & Motorized Ball Valve\nZona 1, Zona 2, Zona 3 (Lintas Parit Melintang)"),
        (70, 22.5, 26, 5.8, "4. Lateral PE 16 mm + 2x PC Dripper 8 L/jam\nRadius 0,5-0,8 m + Keran End-Flush (v >= 0,6 m/s)"),
    ]
    for x, y, w, h, txt in boxes_d3:
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", facecolor="white", edgecolor="#10B981", linewidth=1.1)
        ax.add_patch(b)
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.4, color="#064E3B")

    for y1, y2 in [(44.5, 42.7), (37.5, 35.7), (30.2, 28.3)]:
        ax.annotate("", xy=(83, y2), xytext=(83, y1), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.4))

    # Antarmuka Operator & Pengaman (Bawah penuh)
    d4 = FancyBboxPatch((2, 3), 96, 14.5, boxstyle="round,pad=0.6", facecolor="#F8FAFC", edgecolor="#64748B", linewidth=1.4)
    ax.add_patch(d4)
    ax.text(50, 15.3, "ANTARMUKA OPERATOR & MEKANISME FAIL-SAFE LAPANGAN", ha="center", va="center", fontsize=9.2, fontweight="bold", color="#334155")
    b_op = FancyBboxPatch((4, 4.8), 29, 8.2, boxstyle="round,pad=0.3", facecolor="white", edgecolor="#94A3B8", lw=1)
    ax.add_patch(b_op)
    ax.text(18.5, 8.9, "Operasi Sederhana untuk Buruh (C-05):\nTombol 1-Sentuhan Mulai/Stop + Indikator LED\nStatus (Aktif / Selesai / Perlu Bilas Filter)",
            ha="center", va="center", fontsize=7.5, color="#1E293B")
    b_fs = FancyBboxPatch((35.5, 4.8), 30, 8.2, boxstyle="round,pad=0.3", facecolor="white", edgecolor="#94A3B8", lw=1)
    ax.add_patch(b_fs)
    ax.text(50.5, 8.9, "Keselamatan & Perlindungan Aset:\nSELV 12 V DC Aman Sentuh (IEC 60364-4-41)\nKotak Kontroler IP65 + Cut-off Pipa Bocor/Kering",
            ha="center", va="center", fontsize=7.5, color="#1E293B")
    b_sc = FancyBboxPatch((68, 4.8), 28, 8.2, boxstyle="round,pad=0.3", facecolor="white", edgecolor="#94A3B8", lw=1)
    ax.add_patch(b_sc)
    ax.text(82, 8.9, "Skalabilitas ke Kebun Penuh (S-08/S-09):\nPetak Uji 20x3 m (3 Baris) -> Ekspansi\n10 Zona 500-600 Pohon (<= Rp18 Juta)",
            ha="center", va="center", fontsize=7.5, color="#1E293B")

    # Cross-domain arrows (posisi label bersih tidak menabrak panah)
    ax.annotate("", xy=(40, 43.8), xytext=(30, 38.5), arrowprops=dict(arrowstyle="->", color="#D97706", lw=1.6, ls="--"))
    ax.text(32.5, 44.3, "3,3 V &\nADC Vbat", fontsize=7.0, fontweight="bold", color="#B45309", ha="center",
            bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none", alpha=0.85))
    ax.annotate("", xy=(70, 40.1), xytext=(63, 25.0), arrowprops=dict(arrowstyle="->", color="#1D4ED8", lw=1.5))
    ax.text(66.5, 36.2, "12 V\nSwitch", fontsize=7.0, fontweight="bold", color="#1D4ED8", ha="center",
            bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none", alpha=0.85))
    ax.annotate("", xy=(63, 33.1), xytext=(70, 33.1), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.5))
    ax.annotate("", xy=(45, 17.5), xytext=(50, 22.3), arrowprops=dict(arrowstyle="<->", color="#475569", lw=1.3))

    out = os.path.join(ASSETS_DIR, "fig1_arsitektur_sistem.png")
    plt.tight_layout(pad=0.4)
    plt.savefig(out, dpi=300)
    plt.close(fig)


def draw_fig2_denah():
    fig, ax = plt.subplots(figsize=(11, 6.8), dpi=300)
    ax.set_xlim(-6.2, 31.2)
    ax.set_ylim(-4.0, 18.2)
    ax.axis("off")

    ax.text(12.5, 17.4, "RANCANGAN AWAL PETAK UJI MIKRO-IRIGASI 20 m x 3 BARIS (PRA-SURVEI CIBERES)",
            ha="center", va="center", fontsize=12, fontweight="bold", color="#0F172A")
    ax.text(12.5, 16.3, "Tata Letak Estimasi Awal: Baris 1 - Parit 1 - Baris 2 - Parit 2 - Baris 3 - Parit 3 + Penghubung Melintang (+)",
            ha="center", va="center", fontsize=8.8, color="#475569")

    # Sungai & Rumah Pompa (Kiri)
    river = patches.Rectangle((-5.6, 1.0), 3.4, 13.5, facecolor="#BAE6FD", edgecolor="#0284C7", lw=1.5)
    ax.add_patch(river)
    ax.text(-3.9, 7.75, "SUNGAI / SALURAN\nCIBERES\n(Jarak ~20,54 m\nke tepi kebun)",
            ha="center", va="center", fontsize=8, fontweight="bold", color="#0369A1", rotation=90)

    pump_box = FancyBboxPatch((-0.9, 5.9), 4.0, 4.4, boxstyle="round,pad=0.2", facecolor="#FEF3C7", edgecolor="#D97706", lw=1.4)
    ax.add_patch(pump_box)
    ax.text(1.1, 8.1, "Unit Daya &\nPompa DC 12 V\n+ Disc Filter\n+ PV 100 Wp\n(Box IP65)",
            ha="center", va="center", fontsize=7.0, fontweight="bold", color="#92400E")

    # Mainline PE 1"
    ax.plot([-2.2, -0.9], [8.1, 8.1], color="#1E40AF", lw=3.0)
    ax.text(-1.55, 9.35, "Hisap +\nSaringan", fontsize=6.6, ha="center", va="bottom", color="#1E40AF",
            bbox=dict(boxstyle="round,pad=0.1", facecolor="white", edgecolor="none", alpha=0.85))

    ax.plot([3.1, 6.2], [8.1, 8.1], color="#1D4ED8", lw=3.2)
    ax.text(4.65, 10.1, "Mainline PE 1\"\n(Flow YF-S201 +\nTransduser P)", fontsize=6.7, ha="center", color="#1D4ED8", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="#BFDBFE", lw=0.7))

    # Header manifold lintasi baris & parit melintang
    ax.plot([6.2, 6.2], [2.8, 13.2], color="#1D4ED8", lw=3.2)

    # Tiga Parit Eksisting + Parit Melintang (+)
    ditch_y = [10.4, 5.7, 1.2]
    for idx, dy in enumerate(ditch_y, start=1):
        ditch = patches.Rectangle((6.6, dy), 20.4, 1.0, facecolor="#E0F2FE", edgecolor="#38BDF8", lw=1.0, hatch="//")
        ax.add_patch(ditch)
        ax.text(28.5, dy + 0.5, f"Parit {idx}\n(Eksisting)", va="center", ha="center", fontsize=7.2, color="#0369A1")

    # Parit melintang (+)
    cross_ditch = patches.Rectangle((15.5, 1.2), 1.2, 13.0, facecolor="#E0F2FE", edgecolor="#38BDF8", lw=1.0, ls="--")
    ax.add_patch(cross_ditch)
    ax.text(16.1, 0.35, "Parit Melintang (+)", ha="center", va="center", fontsize=6.8, color="#0369A1",
            bbox=dict(boxstyle="round,pad=0.1", facecolor="white", edgecolor="none"))

    # Jembatan/gantungan pipa atas parit melintang
    bridge = patches.Rectangle((15.2, 1.0), 1.8, 13.5, fill=False, edgecolor="#B45309", lw=1.0, ls=":")
    ax.add_patch(bridge)
    ax.text(16.1, 14.8, "Lintasan Pipa PE Berpenopang (Anti-Terendam/Terinjak)",
            ha="center", va="bottom", fontsize=7.0, color="#B45309", fontweight="bold")

    # Tiga Baris Pohon & Lateral PE 16 mm
    row_y = [13.2, 8.1, 3.3]
    for r_idx, ry in enumerate(row_y, start=1):
        # Motorized Ball Valve Zona
        mv = FancyBboxPatch((6.8, ry - 0.55), 2.1, 1.1, boxstyle="round,pad=0.1", facecolor="#DBEAFE", edgecolor="#1D4ED8", lw=1.2)
        ax.add_patch(mv)
        ax.text(7.85, ry, f"MBV Z{r_idx}", ha="center", va="center", fontsize=6.8, fontweight="bold", color="#1E3A8A")

        # Lateral PE 16 mm
        ax.plot([6.2, 6.8], [ry, ry], color="#1D4ED8", lw=2.4)
        ax.plot([8.9, 26.8], [ry, ry], color="#059669", lw=2.4)
        ax.text(17.8, ry + 0.92, f"Baris Pohon {r_idx} - Lateral PE 16 mm (~20 m, 8 Pohon Estimasi)",
                fontsize=7.1, fontweight="bold", color="#065F46", va="bottom", ha="center",
                bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor="none", alpha=0.88))

        # 8 Pohon + 2 PC Dripper tiap pohon
        xs = np.linspace(10.0, 25.4, 8)
        for px in xs:
            canopy = patches.Circle((px, ry), 0.70, facecolor="#BBF7D0", edgecolor="#15803D", lw=1.0, alpha=0.85)
            ax.add_patch(canopy)
            ax.plot(px, ry, "o", color="#14532D", markersize=3.5)
            ax.plot([px - 0.34, px + 0.34], [ry - 0.34, ry + 0.34], "o", color="#0284C7", markersize=3.0)

        # Keran End-Flush
        fv = FancyBboxPatch((26.8, ry - 0.45), 1.9, 0.9, boxstyle="round,pad=0.1", facecolor="#FEE2E2", edgecolor="#DC2626", lw=1.1)
        ax.add_patch(fv)
        ax.text(27.75, ry, "Flush", ha="center", va="center", fontsize=6.6, fontweight="bold", color="#991B1B")

    # Sensor tanah ditempatkan jelas di celah antara baris 2 dan parit 2
    soil = FancyBboxPatch((18.2, 6.85), 4.6, 0.75, boxstyle="round,pad=0.1", facecolor="#FEF9C3", edgecolor="#CA8A04", lw=1.0)
    ax.add_patch(soil)
    ax.text(20.5, 7.22, "Sensor Tanah + Box IP65", ha="center", va="center", fontsize=6.3, color="#854D0E", fontweight="bold")
    ax.annotate("", xy=(20.5, 8.05), xytext=(20.5, 7.62), arrowprops=dict(arrowstyle="->", color="#CA8A04", lw=1.0))

    # Dimensi 20 m bar cleanly below
    ax.annotate("", xy=(9.0, -0.55), xytext=(26.8, -0.55), arrowprops=dict(arrowstyle="<->", color="#334155", lw=1.2))
    ax.text(17.9, -1.25, "Panjang Petak Uji Awal ~20 m (Dimensi pasti & jumlah pohon divalidasi saat survei lapangan)",
            ha="center", va="center", fontsize=7.6, fontweight="bold", color="#334155")

    # Legend box cleanly separated below
    leg_txt = ("Legenda Komponen Utama:\n"
               "  Garis Biru = Mainline PE 1\" (25 mm)   |   Garis Hijau = Lateral PE 16 mm (ID 13,6 mm)\n"
               "  Titik Biru Muda = 2x PC Dripper 8 L/jam per Pohon (r = 0,5-0,8 m)   |   MBV = Motorized Ball Valve 12V\n"
               "  Flush = Keran Bilas Ujung Lateral (v >= 0,6 m/s)   |   Catatan: Skema mudah diperpanjang untuk C-03 (>= 25 m)")
    ax.text(-5.2, -2.9, leg_txt, fontsize=7.0, color="#334155", va="center",
            bbox=dict(boxstyle="round,pad=0.38", facecolor="#F8FAFC", edgecolor="#CBD5E1"))

    out = os.path.join(ASSETS_DIR, "fig2_denah_petak_uji_20m.png")
    plt.tight_layout(pad=0.4)
    plt.savefig(out, dpi=300)
    plt.close(fig)


def draw_fig3_skematik():
    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 64)
    ax.axis("off")

    ax.text(50, 61.5, "SKEMATIK RANGKAIAN KELISTRIKAN & PENGKONDISIAN SINYAL (SELV 12 V DC)",
            ha="center", va="center", fontsize=12, fontweight="bold", color="#0F172A")
    ax.text(50, 58.8, "Kestabilan Catu 3,3 V Terpisah, Proteksi Interlock Baterai, Penguat RC Sensor Tanah, & Driver 0 W Statis",
            ha="center", va="center", fontsize=8.8, color="#475569")

    # Rel Daya Atas
    ax.plot([4, 96], [53.5, 53.5], color="#DC2626", lw=2.0)
    ax.text(50, 55.0, "+12,8 V DC BUS UTAMA (SELV Terproteksi Sekring 15 A & TVS)", ha="center", va="center", fontsize=8.0, fontweight="bold", color="#B91C1C")
    ax.plot([25, 96], [49.0, 49.0], color="#2563EB", lw=1.6, ls="--")
    ax.text(68, 50.4, "+3,3 V REG LDO EKSTERNAL (Khusus Analog & Logika ESP32)", ha="center", va="center", fontsize=7.6, fontweight="bold", color="#1D4ED8")
    ax.plot([4, 96], [6.5, 6.5], color="#1E293B", lw=2.2)
    ax.text(50, 4.6, "GND REFERENSI BINTANG (Star Grounding - Memisahkan Arus Besar Pompa dari Jalur ADC Sensor)", ha="center", va="center", fontsize=7.8, fontweight="bold", color="#1E293B")

    # Blok Kiri & Tengah
    blocks = [
        (4, 34, 17, 11, "#FFFBEB", "#D97706", "PV 100 Wp -> MPPT\n+ Baterai LiFePO4\n12,8 V 30 Ah\n(BMS + Sekring 15A)"),
        (4, 15, 17, 11.5, "#FEF2F2", "#DC2626", "Pembagi Tegangan\nR1=100k, R2=27k + Zener\n-> GPIO34 ESP32\nInterlock < 11,5 V"),
        (25, 34, 16, 11, "#EFF6FF", "#2563EB", "Buck 12V->5V + LDO\n3,3 V Low-Noise\nKapasitor 10 uF+100 nF\n(Stabilitas ADC)"),
        (25, 12, 22, 17.5, "#DBEAFE", "#1D4ED8", "KONTROLER ESP32\n- I2C (21/22): RTC DS3231\n- GPIO35: ADC Tanah\n- GPIO32: ADC Tekanan\n- GPIO27: Pulse Flow\n- GPIO14: Push Button\n- GPIO25/26/18/19: Aktuator"),
    ]
    for x, y, w, h, fc, ec, txt in blocks:
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4", facecolor=fc, edgecolor=ec, lw=1.4)
        ax.add_patch(b)
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.4, color="#0F172A", fontweight="bold" if "ESP32" in txt else "normal")

    # Blok Kanan Atas: Sensor
    s_blocks = [
        (51, 34, 21, 11, "#FEFCE8", "#CA8A04", "Sensor Tanah Capacitive v1.2\nModifikasi Z-01/Z-08:\n+ Resistor 1 MOhm (R_bleed)\n+ Filter RC 0,1 uF + Power Gate\nMOSFET (Anti-Karat/Drift)"),
        (75, 34, 21, 11, "#F0FDF4", "#16A34A", "Sensor Hidrolika:\n1. Flow YF-S201 (Hall-Effect\n+ Pull-Up + Divider 5V->3,3V)\n2. Transduser Tekanan 0-5 bar\n(0,5-4,5 V -> Divider ke 3,3 V)"),
    ]
    for x, y, w, h, fc, ec, txt in s_blocks:
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4", facecolor=fc, edgecolor=ec, lw=1.3)
        ax.add_patch(b)
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.2, color="#0F172A")

    # Blok Kanan Bawah: Driver Daya & Aktuator
    a_blocks = [
        (51, 12, 21, 16, "#F5F3FF", "#7C3AED", "Driver Katup Zona 1..3:\nH-Bridge (DRV8800 / L293D)\nMotorized Ball Valve 12 V\nPulsa Buka/Tutup 5 dtk\n-> Daya Statis = 0 W!\nAnti-Karat Galvanik PTFE"),
        (75, 12, 21, 16, "#ECFDF5", "#059669", "Driver Pompa DC 12 V:\nOptocoupler + Logic-Level\nMOSFET (IRLZ44N) 55 V 47 A\n+ Dioda Flyback Schottky\n+ Jeda Minimum 30 dtk\n(Anti-Short-Cycling)"),
    ]
    for x, y, w, h, fc, ec, txt in a_blocks:
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4", facecolor=fc, edgecolor=ec, lw=1.4)
        ax.add_patch(b)
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.2, color="#0F172A")

    # Jalur Daya Rapi (tidak memotong isi kotak)
    ax.plot([12.5, 12.5], [45.0, 53.5], color="#DC2626", lw=1.7)
    ax.plot([31.0, 31.0], [45.0, 53.5], color="#DC2626", lw=1.3, ls=":")
    ax.plot([35.0, 35.0], [45.0, 49.0], color="#2563EB", lw=1.6)
    ax.plot([35.0, 35.0], [29.5, 34.0], color="#2563EB", lw=1.4, ls="--")
    # Catu sensor 3.3V dari rel 3.3V ke atas kotak sensor
    ax.plot([61.5, 61.5], [45.0, 49.0], color="#2563EB", lw=1.3, ls="--")
    ax.plot([85.5, 85.5], [45.0, 49.0], color="#2563EB", lw=1.3, ls="--")
    # Catu aktuator 12.8V lewat koridor antar kolom (x=49 dan x=73.5), tidak menembus sensor
    ax.plot([49.2, 49.2], [53.5, 25.0], color="#DC2626", lw=1.3, ls=":")
    ax.plot([49.2, 51.0], [25.0, 25.0], color="#DC2626", lw=1.3, ls=":")
    ax.plot([73.5, 73.5], [53.5, 25.0], color="#DC2626", lw=1.3, ls=":")
    ax.plot([73.5, 75.0], [25.0, 25.0], color="#DC2626", lw=1.3, ls=":")

    # Star ground bawah bersih
    for gx in [12.5, 36.0, 61.5, 85.5]:
        top_y = 15.0 if gx == 12.5 else 12.0
        ax.plot([gx, gx], [6.5, top_y], color="#1E293B", lw=1.4)

    # Sinyal ESP32 <-> Sensor & Aktuator lewat celah tengah y=31.2 (tidak memotong kotak katup)
    ax.annotate("", xy=(47.0, 27.5), xytext=(51.0, 35.0), arrowprops=dict(arrowstyle="<-", color="#CA8A04", lw=1.4))
    ax.annotate("", xy=(47.0, 29.0), xytext=(75.0, 35.0), arrowprops=dict(arrowstyle="<-", color="#16A34A", lw=1.4))
    ax.annotate("", xy=(51.0, 21.0), xytext=(47.0, 21.0), arrowprops=dict(arrowstyle="->", color="#7C3AED", lw=1.4))
    # Sinyal pompa dirutekan lewat jalur bersih y=9.5 dibawah kotak Driver Katup
    ax.plot([47.0, 49.5, 49.5, 73.2, 73.2], [14.5, 14.5, 9.2, 9.2, 14.5], color="#059669", lw=1.4)
    ax.annotate("", xy=(75.0, 14.5), xytext=(73.2, 14.5), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.4))
    ax.annotate("", xy=(25.0, 20.5), xytext=(21.0, 20.5), arrowprops=dict(arrowstyle="<-", color="#DC2626", lw=1.4))

    out = os.path.join(ASSETS_DIR, "fig3_skematik_kelistrikan.png")
    plt.tight_layout(pad=0.4)
    plt.savefig(out, dpi=300)
    plt.close(fig)


def draw_fig4_flowchart():
    fig, ax = plt.subplots(figsize=(10.8, 7.0), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.axis("off")

    ax.text(50, 67.5, "DIAGRAM ALIR LOGIKA KENDALI TERTUTUP & KEAMANAN (FSM ESP32)",
            ha="center", va="center", fontsize=12, fontweight="bold", color="#0F172A")
    ax.text(50, 64.8, "Pemicu RTC/Tombol, Interlock Baterai, Gating Sensor Tanah, Dosis Flow Meter, dan Fail-Safe Tekanan",
            ha="center", va="center", fontsize=8.8, color="#475569")

    def box(x, y, w, h, txt, fc="#FFFFFF", ec="#2563EB", shape="rect"):
        if shape == "round":
            b = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.35,rounding_size=1.8", facecolor=fc, edgecolor=ec, lw=1.4)
            ax.add_patch(b)
        elif shape == "diamond":
            pts = [[x, y + h / 2], [x + w / 2, y], [x, y - h / 2], [x - w / 2, y]]
            poly = patches.Polygon(pts, facecolor=fc, edgecolor=ec, lw=1.4)
            ax.add_patch(poly)
        else:
            b = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.2", facecolor=fc, edgecolor=ec, lw=1.3)
            ax.add_patch(b)
        ax.text(x, y, txt, ha="center", va="center", fontsize=7.4, color="#0F172A", fontweight="bold" if shape != "rect" else "normal")

    # Diamond diperlebar agar teks pas sempurna di dalam
    box(28, 59.5, 30, 4.2, "IDLE / DEEP SLEEP\n(Tunggu RTC DS3231 atau Tombol 1-Sentuhan)", fc="#DBEAFE", ec="#1D4ED8", shape="round")
    box(28, 52.0, 29, 4.2, "Bangun Sistem + Aktifkan Power Gate Sensor\nBaca V_baterai & Sensor Tanah Terkalibrasi", fc="#F8FAFC", ec="#475569")
    box(28, 43.2, 31, 6.2, "V_bat >= 11,5 V ?\n(Interlock LiFePO4)", fc="#FEF3C7", ec="#D97706", shape="diamond")
    box(74, 43.2, 32, 4.8, "FAULT / LOW BATTERY\nKunci Katup Tertutup, LED Merah Berkedip,\nKembali ke Deep Sleep (Lindungi Sel)", fc="#FEE2E2", ec="#DC2626")

    box(28, 33.8, 34, 6.4, "Tombol Manual OR\n(Jadwal RTC & Kering)?", fc="#FEF3C7", ec="#D97706", shape="diamond")
    box(74, 33.8, 32, 4.4, "Tunda Siklus (Hujan/Tanah Lembab)\nMatikan Power Gate Sensor -> Deep Sleep", fc="#F1F5F9", ec="#64748B")

    box(28, 24.5, 35, 4.5, "ZONA i: Buka Motorized Ball Valve Zona i (5 dtk)\nVerifikasi Jeda Pompa >= 30 dtk -> Nyalakan Pompa DC", fc="#ECFDF5", ec="#059669")
    box(28, 17.0, 35, 4.5, "LOOP PEMANTAUAN:\nIntegrasi Volume V = Integral Q(t) dt (Flow Meter)\nPantau Tekanan P_pipa (Transduser 0-5 bar)", fc="#EFF6FF", ec="#2563EB")

    box(28, 8.2, 34, 6.4, "P di luar [0,5..3,5 bar]\natau dP >= 70 kPa?", fc="#FEF3C7", ec="#D97706", shape="diamond")
    box(74, 8.2, 32, 4.8, "SAFETY TRIP / PERINGATAN:\nMatikan Pompa (Dry-Run/Bocor) atau Nyalakan\nLED Kuning 'Bilas Disc Filter'!", fc="#FFEDD5", ec="#EA580C")

    box(74, 21.5, 32, 5.2, "V_zona >= Target (mis. 120-160 L)?\nYa -> Matikan Pompa, Tutup MBV i,\nLanjut Zona i+1 atau Selesai -> Deep Sleep", fc="#DCFCE7", ec="#15803D")

    def arr(x1, y1, x2, y2, lbl="", lx=None, ly=None, col="#334155"):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color=col, lw=1.4))
        if lbl:
            ax.text(lx if lx is not None else (x1 + x2) / 2, ly if ly is not None else (y1 + y2) / 2 + 0.8,
                    lbl, fontsize=7.2, fontweight="bold", color=col, ha="center")

    arr(28, 57.4, 28, 54.1)
    arr(28, 49.9, 28, 46.3)
    arr(43.5, 43.2, 58, 43.2, "TIDAK", 50.8, 44.3, "#DC2626")
    arr(28, 40.1, 28, 37.0, "YA", 30.2, 38.4, "#059669")
    arr(45.0, 33.8, 58, 33.8, "TIDAK", 51.5, 34.9, "#64748B")
    arr(28, 30.6, 28, 26.8, "YA", 30.2, 28.6, "#059669")
    arr(28, 22.2, 28, 19.3)
    arr(28, 14.7, 28, 11.4)
    arr(45.0, 8.2, 58, 8.2, "YA (ABNORMAL)", 51.5, 9.3, "#EA580C")
    ax.annotate("", xy=(58, 22.0), xytext=(45.5, 17.8), arrowprops=dict(arrowstyle="->", color="#15803D", lw=1.4))
    ax.text(51.5, 21.4, "Normal", fontsize=7.2, fontweight="bold", color="#15803D", ha="center",
            bbox=dict(boxstyle="round,pad=0.1", facecolor="white", edgecolor="none"))
    ax.annotate("", xy=(45.5, 16.0), xytext=(58, 19.8), arrowprops=dict(arrowstyle="->", color="#2563EB", lw=1.2, ls="--"))
    ax.text(52.2, 15.8, "Belum", fontsize=7.0, fontweight="bold", color="#2563EB", ha="center")

    out = os.path.join(ASSETS_DIR, "fig4_flowchart_fsm.png")
    plt.tight_layout(pad=0.4)
    plt.savefig(out, dpi=300)
    plt.close(fig)


def draw_fig5_simulasi(hyd, ene):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.6, 5.1), dpi=300)

    # Panel A: Hidrolika (Head Pompa dibutuhkan vs Kecepatan Scouring 1 Lateral)
    q = np.array(hyd["sweep"]["q_lh"])
    v_lat = np.array(hyd["sweep"]["v_lat_1lat_ms"])
    p_clean = np.array(hyd["sweep"]["p_pump_clean_bar"])
    p_dirty = np.array(hyd["sweep"]["p_pump_dirty_bar"])

    l1, = ax1.plot(q, p_clean, color="#059669", lw=2.2, label="Tekanan Pompa (Filter Bersih ~0,20 bar)")
    l2, = ax1.plot(q, p_dirty, color="#D97706", lw=2.0, ls="--", label="Tekanan Pompa (Ambang Bilas 0,70 bar)")
    l4 = ax1.axhline(0.7845, color="#DC2626", lw=1.2, ls=":", label="Ambang Minimal Emitter (78,45 kPa)")
    ax1.fill_between(q, p_clean, p_dirty, color="#FEF3C7", alpha=0.4)

    ax1_r = ax1.twinx()
    l3, = ax1_r.plot(q, v_lat, color="#2563EB", lw=2.0, label="Kecepatan 1 Lateral 16 mm (m/s)")
    ax1_r.axhline(0.60, color="#1D4ED8", lw=1.2, ls="-.")

    # Titik operasi eksak sesuai simulation_results.json!
    c_1z = next(c for c in hyd["configs"] if c["trees"] == 8)
    c_3b = next(c for c in hyd["configs"] if c["trees"] == 24)
    c_fl = next(c for c in hyd["configs"] if c["trees"] == 0)

    ax1.scatter([c_1z["Q_L_h"], c_3b["Q_L_h"]], [c_1z["P_pump_clean_bar"], c_3b["P_pump_clean_bar"]],
                color="#065F46", zorder=6, s=50)
    ax1.annotate(f"1 Zona (8 pohon, 128 L/jam)\nP = {c_1z['P_pump_clean_bar']:.2f} bar",
                 xy=(c_1z["Q_L_h"], c_1z["P_pump_clean_bar"]), xytext=(48, 0.90),
                 arrowprops=dict(arrowstyle="->", color="#065F46", lw=1.1), fontsize=7.0, fontweight="bold", color="#065F46")
    ax1.annotate(f"3 Baris Serentak (3 lat, 384 L/jam)\nP = {c_3b['P_pump_clean_bar']:.2f} bar",
                 xy=(c_3b["Q_L_h"], c_3b["P_pump_clean_bar"]), xytext=(242, 1.07),
                 arrowprops=dict(arrowstyle="->", color="#065F46", lw=1.1), fontsize=7.0, fontweight="bold", color="#065F46")

    ax1_r.scatter([c_fl["Q_L_h"]], [c_fl["v_lat_inlet_ms"]], color="#1D4ED8", zorder=6, s=55, marker="D")
    ax1_r.annotate(f"End-Flush 1 Lateral\n({c_fl['Q_L_h']:.1f} L/jam, v=0,80 m/s)",
                   xy=(c_fl["Q_L_h"], c_fl["v_lat_inlet_ms"]), xytext=(270, 0.96),
                   arrowprops=dict(arrowstyle="->", color="#1D4ED8", lw=1.1), fontsize=7.2, fontweight="bold", color="#1D4ED8")

    ax1.set_title("Simulasi Hidrolika: Kebutuhan Tekanan & Kecepatan Bilas", fontsize=10, fontweight="bold", color="#0F172A")
    ax1.set_xlabel("Laju Alir Sistem Total (L/jam)", fontsize=8.8)
    ax1.set_ylabel("Tekanan Minimal Keluar Pompa (bar)", fontsize=8.8, color="#065F46")
    ax1_r.set_ylabel("Kecepatan Aliran 1 Lateral 16 mm (m/s)", fontsize=8.8, color="#1D4ED8")
    ax1.set_ylim(0.5, 2.6)
    ax1_r.set_ylim(0, 1.2)
    ax1.grid(True, linestyle="--", alpha=0.35)

    lines = [l1, l2, l4, l3]
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="upper left", fontsize=6.9, framealpha=0.92)

    # Panel B: Perbandingan Konsumsi Energi & Otonomi (LiFePO4 12,8V 30Ah = 307,2 Wh usable)
    labels_b = [
        "3 Baris Serentak\n+ MBV (0 W Statis)",
        "3 Zona Bergantian\n+ MBV (0 W Statis)",
        "3 Zona Bergantian\n+ Selenoid NC (12 W)",
        "Energi Surya 100 Wp\n(Mendung 1 hari)",
        "Kapasitas Pakai\nLiFePO4 30Ah (DoD 80%)"
    ]
    vals_b = [
        ene["e_cycle_simul_mbv_wh"],
        ene["e_cycle_3zone_mbv_wh"],
        ene["e_cycle_3zone_nc_wh"],
        ene["e_gen_cloudy_wh_day"],
        ene["bat_usable_wh"],
    ]
    colors_b = ["#059669", "#10B981", "#EF4444", "#F59E0B", "#2563EB"]
    y_pos = np.arange(len(labels_b))
    bars = ax2.barh(y_pos, vals_b, color=colors_b, height=0.58, edgecolor="#1E293B", linewidth=0.6)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(labels_b, fontsize=7.8)
    ax2.invert_yaxis()
    ax2.set_xlabel("Energi per Siklus 24 Pohon (360 L) / Kapasitas (Wh)", fontsize=8.6)
    ax2.set_title("Simulasi Neraca Energi Surya & Efisiensi Katup (Wh)", fontsize=10, fontweight="bold", color="#0F172A")
    ax2.set_xlim(0, 370)
    ax2.grid(True, axis="x", linestyle="--", alpha=0.35)

    for bar, val in zip(bars, vals_b):
        ax2.text(val + 5, bar.get_y() + bar.get_height() / 2, f"{val:.1f} Wh",
                 va="center", ha="left", fontsize=8.0, fontweight="bold", color="#0F172A")

    out = os.path.join(ASSETS_DIR, "fig5_simulasi_hidrolika_energi.png")
    plt.tight_layout(pad=1.0)
    plt.savefig(out, dpi=300)
    plt.close(fig)


def main():
    hyd = compute_hydraulics()
    ene = compute_energy()

    draw_fig1_arsitektur()
    draw_fig2_denah()
    draw_fig3_skematik()
    draw_fig4_flowchart()
    draw_fig5_simulasi(hyd, ene)

    summary = {"hydraulics": hyd, "energy": ene}
    json_path = os.path.join(SCRIPT_DIR, "simulation_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("=== HYDRAULICS RESULTS ===")
    for r in hyd["configs"]:
        print(r)
    print("=== ENERGY RESULTS ===")
    print(ene)
    print("=== ASSETS GENERATED ===")
    for fn in sorted(os.listdir(ASSETS_DIR)):
        print(" ", fn)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Sumber data tunggal (Single Source of Truth) untuk BOM Purwarupa, Proyeksi Skala Penuh,
RAB Pelaksanaan, Matriks Pugh, dan Sitasi IEEE Terverifikasi CD-3 Jeruk Limau Ciberes.
"""

BOM_PROTOTYPE = [
    ("1", "Panel Surya Monokristalin 100 Wp (SELV 12 V)", "1 unit", 620000, "S-06, S-12: catu off-grid nol emisi"),
    ("2", "Solar Charge Controller MPPT 10 A + Bracket", "1 unit", 250000, "S-06: maksimalkan panen surya saat mendung"),
    ("3", "Baterai LiFePO4 12,8 V 30 Ah (384 Wh) + BMS Terintegrasi", "1 unit", 1150000, "S-06: otonomi > 8 jam / >= 3 siklus serentak"),
    ("4", "Pompa Diafragma DC 12 V 80-100 W (Non-Besi Cor / Polimer)", "1 unit", 340000, "Z-12, Z-14: bebas korosi besi di air berendapan"),
    ("5", "Saringan Hisap Pra-Pompa + Foot Valve Non-Korosif 1 inci", "1 set", 95000, "Z-12, S-13: cegah batu/pasir sungai masuk pompa"),
    ("6", "Disc Filter 120-150 Mesh (124 um) + Keran Bilas Lumpur", "1 unit", 165000, "Z-09, S-13: proteksi penyumbatan labirin emitter"),
    ("7", "Motorized Ball Valve 12 V DC PTFE 3/4 inci (0 W Statis)", "3 unit", 185000, "Z-04, Z-16, Z-17: hemat 99,9% energi katup vs NC"),
    ("8", "Driver H-Bridge DRV8800 + MOSFET IRLZ44N + Opto + Dioda", "1 set", 95000, "S-10: isolasi switching pompa & kendali polaritas MBV"),
    ("9", "Mikrokontroler ESP32 + RTC DS3231 + Buck 5 V + LDO 3,3 V Eksternal", "1 set", 175000, "Z-08, S-05: kestabilan tegangan ADC & jadwal RTC"),
    ("10", "Sensor Aliran Air Water Flow Meter YF-S201 (Hall-Effect)", "1 unit", 75000, "S-01: integrasi volume dosis aktual 15 L/pohon"),
    ("11", "Transduser Tekanan Analog 0-5 bar + Tee Kuningan/PE", "1 unit", 195000, "Z-09, Z-16: deteksi dry-run, bocor, & dP filter >=70 kPa"),
    ("12", "Sensor Tanah Capacitive v1.2 + R 1 MOhm + C 0,1 uF + MOSFET Gate", "2 set", 55000, "Z-01, Z-08, Z-21: mitigasi korosi & drift suhu"),
    ("13", "Kotak Panel IP65 Outdoor + Tombol 1-Sentuhan IP67 + 3 LED + Sekring 15 A", "1 set", 220000, "C-05, S-10: proteksi IP65 hujan & antarmuka buruh"),
    ("14", "Pipa Utama Mainline HDPE/PE 1 inci (Sungai 20,54 m + Header)", "31 m", 10000, "C-01: jalur utama berdiameter ID ~25 mm gesekan rendah"),
    ("15", "Pipa Lateral PE 16 mm (3 baris @ 20 m + cadangan sambungan)", "65 m", 3500, "Z-12: ID 13,6 mm menyalurkan 3x8 pohon petak uji"),
    ("16", "PC Dripper 8 L/jam (48 terpasang + 2 cadangan)", "50 unit", 2500, "S-02, Z-19: debit seragam radius akar 0,5-0,8 m"),
    ("17", "Keran End-Flush 16 mm (3x) + Tee/Grommet + Tiang Penopang Lintas Parit (+)", "1 set", 142500, "Z-12: bilas sedimen >=0,6 m/s & lintasi parit"),
]


def calc_bom_totals():
    rows = []
    grand = 0
    for no, nama, qty_str, unit_p, just in BOM_PROTOTYPE:
        qty_num = int("".join(ch for ch in qty_str.split()[0] if ch.isdigit()))
        sub = qty_num * unit_p
        grand += sub
        rows.append((no, nama, qty_str, unit_p, sub, just))
    return rows, grand


# Proyeksi Skala Penuh 500-600 Pohon (10 Zona @ 50-60 pohon/zona, kebun ~100 m) <= Rp18.000.000
FULL_SCALE_PROJECTION = [
    ("1", "Peningkatan PLTS Off-Grid (PV 2x150 Wp + MPPT 30 A + LiFePO4 100 Ah)", "1 paket", 5450000, "S-06: mendukung siklus beruntun 10 zona kebun 3.000 m2"),
    ("2", "Pompa DC/BLDC 24 V atau 2x Pompa DC 12 V Paralel (Non-Besi Cor) + Pra-Filter", "1 paket", 1950000, "C-01: menyuplai 60 pohon/zona (~960 L/jam @ 1,5-2,0 bar)"),
    ("3", "Motorized Ball Valve 12/24 V PTFE (10 zona) + Ekspansi Relay/Driver Isolasi", "10 unit", 185000, "Z-16, S-09: penjadwalan bergilir 10 zona 0 W statis"),
    ("4", "Mainline HDPE 1,5 inci (140 m) & Jembatan Pipa Lintas Parit Melintang (+)", "1 paket", 2150000, "C-01: menekan kehilangan tekan sepanjang kebun 100-118 m"),
    ("5", "Pipa Lateral PE 16 mm (~600 m untuk 3 jalur utama x 100 m + cadangan) + Keran Flush", "1 paket", 2250000, "Z-12: dilengkapi keran end-flush di setiap akhir zona"),
    ("6", "PC Dripper 8 L/jam (1.200 unit untuk 600 pohon @ 2 emitter) + Selang Mikro", "1.200 unit", 2300, "S-02: dosis 15 L/pohon terkompensasi tekanan di 600 pohon"),
    ("7", "Unit Kendali ESP32 Master + Disc Filter Ganda 120 Mesh + Sensor Tekanan & Flow + 4 Sensor Tanah", "1 paket", 1380000, "S-01, S-10, S-13: instrumentasi & proteksi IP65 terpusat"),
]


def calc_full_scale():
    rows = []
    total = 0
    for no, nama, qty_str, unit_p, just in FULL_SCALE_PROJECTION:
        if "unit" in qty_str and qty_str.split()[0].replace(".", "").isdigit():
            qty_num = int(qty_str.split()[0].replace(".", ""))
            sub = qty_num * unit_p
        else:
            sub = unit_p
        total += sub
        rows.append((no, nama, qty_str, unit_p, sub, just))
    return rows, total


# RAB Pelaksanaan Tugas Akhir Total (Purwarupa + Instrumen Uji & Survei Ciberes)
RAB_SUPPORT = [
    ("B.1", "Alat Ukur & Kalibrasi Uji (Gelas Ukur 2 L, TDS/EC Meter, Multimeter, Stopwatch)", "1 paket", 385000, "Verifikasi S-01, S-02 (CU), dan kalibrasi flow meter"),
    ("B.2", "Material Pemasangan Lapangan (Lem PVC/PE, Kabel NYYHY, Cable Gland IP68, Potting Epoxy)", "1 paket", 420000, "Proteksi kelembapan sambungan kebun Ciberes"),
    ("B.3", "Jasa Fabrikasi Mekanik (Rangka Tiang Penyangga Panel Surya 100 Wp & Dudukan Kotak Panel)", "1 paket", 350000, "Stabilisasi panel surya terhadap angin & hujan kebun"),
    ("B.4", "Operasional Survei Validasi Lapangan, Transportasi Pengujian Bandung-Subang (3x), & Logistik", "1 paket", 430000, "Pengukuran dimensi riil & uji coba kebun mitra"),
]


if __name__ == "__main__":
    _, p_tot = calc_bom_totals()
    _, f_tot = calc_full_scale()
    s_tot = sum(x[3] for x in RAB_SUPPORT)
    print(f"Prototype BOM: Rp{p_tot:,}")
    print(f"Full-Scale Projection: Rp{f_tot:,}")
    print(f"Support RAB: Rp{s_tot:,} -> Grand Total RAB: Rp{p_tot + s_tot:,}")


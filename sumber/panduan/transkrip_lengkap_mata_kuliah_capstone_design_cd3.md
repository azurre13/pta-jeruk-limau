# Transkrip Lengkap Perkuliahan: Penyusunan Dokumen Perancangan (CD3), Matriks Scoring, & Arsitektur Sistem

* **Topik Pembahasan:** Panduan Penyusunan Dokumen Capstone Design 3 (CD3), Matriks Seleksi Solusi, Arsitektur Sistem, & Persiapan Seminar Proposal (Sempro)
* **Durasi Rekaman:** 56:10
* **Pembicara:** Dosen Pengampu & Mahasiswa

---

## Sesi 1: Percakapan Mahasiswa Sebelum Kelas Dimulai (00:00 – 01:54)

**\[00:00\] \[Mahasiswa 1\]:**  
10 menit lagi.

**\[00:04\] \[Mahasiswa 2\]:**  
10 menit? Ya udah.

**\[00:08\] \[Mahasiswa 1\]:**  
Malas sih dia.

**\[00:12\] \[Mahasiswa 2\]:**  
Lah, nggak tahu dia kayak penyakit malas gitu.

**\[00:25\] \[Mahasiswa 1\]:**  
Kadang-kadang tuh orang *random* banget tiba-tiba *mood* naik *mood* turun. Tahu-tahu bolos karena *"kalian tadi ninggalin aku jadi aku bolos"* gitu. Tahu-tahu ngomongnya gitu kan.

**\[00:46\] \[Mahasiswa 2\]:**  
Cek. Kalau ikutan... kayak cowok banget.

---

## Sesi 2: Pengumuman Deadline CD3 & Kriteria Alternatif Solusi (01:55 – 04:19)

**\[01:55\] \[Dosen\]:**  
Oke, sebentar... mau lihat *schedule* ya, nanti 10 Desember ya. Pengumpulan CD3 paling lambat 10 Desember, jadi bagian... bagian besar, 3 minggu sampai 4 minggu ya.

**\[02:30\] \[Mahasiswa 2\]:**  
*(Berbisik)* CD3 10 Desember.

**\[02:55\] \[Dosen\]:**  
Rubriknya hanya satu ya, di sini hanya alternatif solusi. Detailnya masih 1 sampai 4. Di poin keempat itu minimal dua alternatif solusi dengan matriks *scoring* dan penjelasannya untuk seleksi.

**\[03:20\] \[Mahasiswa 1\]:**  
*(Berbisik)* Apa ini? Alternatif solusi.

**\[03:25\] \[Dosen\]:**  
Umumnya, kalau saya *review* itu kebanyakan dokumen sebelum-sebelumnya itu nggak nyambung dengan dokumen sebelumnya, spesifikasi ya. Harusnya solusi itu berasal dari spesifikasi alternatifnya.

**\[04:05\] \[Mahasiswa 2\]:**  
*(Berbisik)* Minimal dua ya? Minimal dua. Minimal dua. Baiknya tiga.

---

## Sesi 3: Evaluasi Parameter Pembanding & Kesesuaian dengan CD2 (04:20 – 08:30)

**\[04:20\] \[Dosen\]:**  
Biasanya justru yang nggak sesuai spesifikasi parameter yang mau dibandingkan antara solusi. Biasanya *miss* ya. Jadi, ini yang menjadi *note* khususnya di bagian parameter yang dibandingkan. Dan baiknya apa sih yang kita bandingkan gitu?

**\[05:05\] \[Dosen\]:**  
Nah, macam-macam memang bisa dibandingkan. Tapi yang dibandingkan lebih baik ke *core*-nya. Ini tidak perlu membandingkan teknologi atau *stack* teknologinya, itu nggak relevan. Nah, tapi yang bisa kalian bandingkan itu *core*. *Core* itu bisa kalian bandingkan algoritmanya, modelnya, kalau kalian pakai ya... Algoritma, metode, bagaimana dia bekerja. Kemudian kalau kalian sudah punya satuan metrik dari *non-functional requirement*, itu juga bisa dipakai.

**\[06:20\] \[Dosen\]:**  
Misalkan kalian di CD2 itu sudah mendefinisikan *response time*-nya, berarti harusnya muncul. Di CD2 kalian sudah mendefinisikan akurasi, nah itu harusnya muncul. Dari spesifikasi itu kalian bandingkan untuk masing-masing solusi. Parameter...

**\[07:05\] \[Dosen\]:**  
Kebanyakan di sini nih yang nggak sesuai dengan CD2-nya. Jadi yang dibandingkan justru hal yang baru. Ketika yang dibandingkan hal yang baru, jadi nggak kebayang lagi spesifikasi itu seolah-olah cuma nanti hal yang akan diukur saja. Padahal ketika kalian membuat produk, sudah ada spesifikasinya, ya harusnya mengacu ke situ. Nah, jadi kebanyakan beberapa yang sebelum-sebelumnya... ini jadinya nggak dapat.

---

## Sesi 4: Penyusunan Matriks Scoring & Skala Penilaian Objektif (08:31 – 18:45)

**\[08:31\] \[Dosen\]:**  
Nah, memang nanti mengukurnya itu bisa menggunakan matriks *scoring*. Matriks *scoring*. Skornya bisa 1 sampai 5.

**\[08:55\] \[Dosen\]:**  
Nah, biasanya mahasiswa juga waktu seminar bingung nih kalau ditanya, *"Gimana kalian dapat angka 5?"* Misalnya solusi 1, solusi 2, solusi 3. Contoh aja lah misalkan. Solusi 1 kalian kasih skor 3, solusi 2 empat, solusi 3 lima. Nah kalian ketika ditanya *"Kalian dapat 3, 4, 5 dari mana?"* Biasanya: *"Kami kira-kira, Pak."* atau *"Kami feeling-nya segitu, Pak."*

**\[10:05\] \[Dosen\]:**  
Nah, sebenarnya nggak bisa kira-kira juga. Tapi memang belum ada ini ya, belum ada panduan, panduan yang pasti. Panduan yang pasti ini harus berapa skornya 1 sampai 5. Dan untuk menentukan 1 sampai 5 sebetulnya bisa dibuat sendiri skalanya. Kalian bisa dapat hasilnya dari literatur atau dari *running* eksperimen awal.

**\[10:50\] \[Dosen\]:**  
Jadi skalanya nanti bisa dibuat dari... kita nggak akan ngomong nilainya tapi kita bisa ngomong *range*-nya, kesepakatannya. Misalkan *response time*-nya. *Response time*-nya kita dari hasil eksperimen awal misalkan untuk masing-masing solusi: solusi pertama itu dapat katakanlah *response time*-nya $3\text{ ms}$. Solusi kedua itu *response time*-nya $8\text{ ms}$. Solusi ketiga *response time*-nya $10\text{ ms}$.

**\[11:55\] \[Dosen\]:**  
Nah, sebenarnya dari sini kita bisa bikin skala saja. Katakanlah $0$ sampai $10$. Lalu ini masuk yang mana nih? Masuknya *grade* berapa? Misalnya paling kecil, paling besar berarti dia skornya paling kecil dia skornya besar. Ya kalau kita bikin 2-2 berarti ini akan masuk... Nah, hal yang kayak gini lebih enak nanti untuk menjelaskan ketika penguji bertanya, *"Kalian dapat angkanya dari mana?"*

**\[13:05\] \[Dosen\]:**  
Jadi nilainya memang tidak ada patokan baku satunya itu harus dari mana, duanya dari mana. Itu memang dibebaskan tapi bukan berarti bahwa akan kira-kira. Jadinya itu ya. Baiknya memang sudah ada studi literatur yang menunjukkan hasilnya. Minimal gitu. Atau kalian sudah *running* eksperimennya. Sudah muncul hasilnya. Jadi kalian bisa bikin skala sendiri. Itu yang lebih enak nanti disampaikan waktu seminar proposal, disampaikan ke penguji. Kalau matriks *scoring* nanti sih tinggal disusun saja sih biasanya ya.

**\[14:55\] \[Dosen\]:**  
Nah nanti paling ya yang jumlahnya paling besar, biasanya itu. Itu usulan solusinya.

**\[15:26\] \[Dosen\]:**  
Jadi memang nilainya nggak harus semua rata kanan. Nggak harus semua rata kanan. Maksudnya solusi yang dipilih itu sebetulnya tidak harus nilainya akan besar semua. Tapi kan kalau namanya juga *scoring* ya, penjumlahan, berarti kan yang penting hasil penjumlahannya yang paling besar, itu yang dipilih.

**\[16:05\] \[Dosen\]:**  
Kebanyakan juga biasanya semuanya dirata-kanankan. Jadi desain solusi yang terpilih semua nilainya tuh katakanlah paling gede. Padahal nggak harus seperti itu. Ya bisa jadi solusi 3 secara algoritma bagus, tapi mungkin secara respons dia cukup kecil misalnya, 3. Tapi yang penting hasil penjumlahannya. Hasil penjumlahannya yang paling besar, itulah solusi yang dipilih.

**\[17:15\] \[Dosen\]:**  
Jadi sekali lagi, terutama di sini, terutama di sini untuk matriks *scoring*. Evaluasi terbesarnya ada di sini. Yang pertama parameter yang dibandingkan itu selalu baru. Harusnya sesuai dengan spesifikasi yang sebelumnya. Minimal *non-functional requirement*-nya harus masuk di situ. Ya kalian boleh juga menambahkan parameter yang baru ya. Nah, kemudian nilai di sini juga selalu... selalu jawabannya kira-kira.

**\[18:10\] \[Dosen\]:**  
Jadi sekali lagi untuk mendapatkan baiknya kalian sudah membaca studi literatur, syukur-syukur sudah ada nilainya. Atau kalian jalankan eksperimen sederhana untuk tahu hasilnya. Jadi isi angka 3, 4, 5 untuk matriks *scoring* itu nggak kira-kira lagi. Kalau nanti sempro, lagi-lagi kalian ditanya bisa jawab dari mana angkanya. Ya. Intinya cuma itu sih sebenarnya.

---

## Sesi 5: Perancangan Arsitektur Sistem & Pembagian Subsistem (18:46 – 24:10)

**\[18:46\] \[Mahasiswa 1\]:**  
*(Berbisik)* Yang beda... beda yang kau tanya kemarin.

**\[19:00\] \[Dosen\]:**  
Umumnya itu... jadi di sini biar nanti ada titik kejelasannya. Berdasarkan dari judulnya ada solusi berupa sistem, arsitektur dan *framework*, lalu perangkat lunak, perangkat keras, proses, lalu model atau algoritma. Nah karena kalian punya satu topik besar kan, satu topik besar. Jadi *blueprint* pertama hasilnya akan berupa arsitektur. Itu pasti. Itu wajib. Arsitektur itu pasti harus ada. Karena kalian gabungan. Beda kalau kalian ngerjainnya sendiri-sendiri. Itu memang hasilnya akan mungkin yang *software* software, yang *hardware* hardware. Tapi karena kalian kerjanya bersama-sama dalam satu topik besar, pasti ada arsitektur utama dulu. Arsitektur sistem itu harus ada dulu. Ya, bagaimana sistem secara umum, secara besar itu bekerja. Nah itu perlu dijelaskan cara kerja arsitekturnya, cara kerjanya, atau *workflow*-nya dari arsitektur tersebut.

**\[21:20\] \[Dosen\]:**  
Nah, kalau sudah baru dijelaskan kalian ngerjain sub yang mana. Kalau kalian misalkan bikin sub untuk *software*, nah baru kalian jelaskan untuk *software* apa yang dirancang. Nanti ada bagian lagi misalnya blok *hardware*, nah itu juga. Setelah menjelaskan arsitektur yang global baru kalian ceritakan bagian kalian masing-masing. *Software* ya *software*, *hardware*, jaringan ya jaringan.

**\[22:25\] \[Dosen\]:**  
Nah jadi kelihatan nih nanti. *Software* berarti nanti kalian baru masukkan misalkan yang berisi solusi perangkat lunak, berarti nanti ada perancangan *flowchart*-nya, atau perancangan antarmukanya, lalu ada perancangan *database*-nya, *entity relationship diagram*-nya. Nah itu dia. Nah lalu baru di situ. Kalau yang *hardware* berarti ada *detail engineering design*-nya, lalu PCB-nya, modul-modul dan sebagainya. Ini bisa pakai diagram blok kalau yang *hardware*.

**\[23:35\] \[Dosen\]:**  
Tapi alurnya harus seperti itu. Kalian harus mulai dari yang besar dulu nih arsitekturnya utama. Lalu kalian masing-masing tuliskan bagian kalian sendiri. Rancangannya sesuaikan dengan apa yang kalian buat.

---

## Sesi 6: Aturan Pemodelan Software (UML vs DFD), Database, & UI Design (24:11 – 35:14)

**\[24:11\] \[Dosen\]:**  
Nah, kalau *software* tolong diperhatikan. Suka campur aduk nih kalau *software*. Jadi kalau nanti sekiranya kalian bikin *software*, *code*-nya itu basisnya bukan objek, kalian nggak boleh merancang UML. UML lalu diagramnya apa ada di situ? *Class diagram* ya, terus apalagi? *Sequence*, lalu apalagi? Cuma tiga? *Activity diagram*. Nah, kalian boleh bikin ini kalau pendekatannya *object-oriented* *code*-nya. Kalian nanti pakai *class*, pakai *abstraction*, nah itu boleh pakai bikin UML, bikin *class*, bikin *sequence* dan *activity diagram*.

**\[26:10\] \[Dosen\]:**  
Tapi kalau kalian nggak pakai OOP, ya kalian bikinnya DFD, *Data Flow Diagram*. Kalau kalian kebolak-balik dan nanti pengujinya Pak Nasrun, nah itu bahaya kalian.

**\[26:35\] \[Mahasiswa 2\]:**  
*(Berbisik)* Kata... beneran.

**\[27:35\] \[Dosen\]:**  
Jadi tolong ya... CD3 itu isinya perancangan. Jadi mulailah dari arsitekturnya. Arsitektur sistem lalu masuk ke bagian kaliannya. Buat *software*, sekali lagi kalau kalian nggak pakai pendekatan *object-oriented*, jangan bikin UML, *class diagram*, *sequence*, atau *activity diagram*. Itu nggak boleh. Kalau nggak pakai *object-oriented*, bikinlah DFD, *Data Flow Diagram*. Mulai dari diagram konteks lalu level 1, level 2, level 3 dan sebagainya. Gitu ya.

**\[28:40\] \[Dosen\]:**  
Nah, kemudian kalau pakai *database* sebetulnya yang umum dituliskan itu skemanya. Lalu yang menjadi catatan juga perancangan *database* ya. *Database* itu sudah muncul skemanya. Biasanya sudah muncul skemanya gitu relasi antar tabelnya. Kadang langsung di-*copy-paste* saja bentuk *database*-nya, kayak tabel-tabelnya: tabel A, B, C, D. Kalau kalian mau pakai skema boleh, tapi yang nggak boleh bentuk langsung tabelnya di-*copy-paste* itu nggak boleh.

**\[30:10\] \[Dosen\]:**  
Kalau kalian merancang tabel, ya memang harus namanya juga rancangan ya. Kalian bikin tabel-tabelnya. Misalkan tabel *user*, lalu ada namanya *field*-nya apa saja, tipe data dan panjang ya, lalu misalnya keterangan. *User* misalnya *field*-nya ada *username*, tipenya `varchar` katakanlah, panjangnya 20, keterangannya misalnya *primary key*. *Password* `varchar` misalnya 32, misalnya pakai MD5 biasa. Nama `varchar` 40. Nah ini desainnya kayak gini. Bukan cuma nampilin hasil dari ya katakanlah phpMyAdmin atau *software* yang lain yang udah jadi. Ini udah yang ditampilkan cuma tabel-tabelnya doang. Terus langsung skemanya. Nah ini nggak boleh ya.

**\[31:05\] \[Dosen\]:**  
*(Menegur mahasiswa yang baru masuk kelas)*  
Ini dari mana? Hah? Sebelumnya dari mana? Baru datang? Jadwalnya jam berapa? Oke.

**\[32:20\] \[Dosen\]:**  
Jadi gini, nah ini desain tabel. Kalau sudah desainnya, nah boleh kalian bikin skemanya untuk menunjukkan relasi antar tabelnya. Jadi desainnya baru kalian bikin relasi antar tabel. Nah yang nggak boleh langsung ini, langsung bikin nama tabelnya aja, desainnya nggak ada. Nah ini udah desain. Nah seperti itu.

**\[33:25\] \[Dosen\]:**  
Kalau *hardware*, ya biasa ya ada *detail engineering design*, kalian boleh tambahkan blok diagram. Diagram bloknya seperti apa atau desain PCB-nya seperti apa kayak gitu.

**\[34:05\] \[Dosen\]:**  
Kalau *software*, berarti ada desain dari sisi proses ya, ini dari sisi proses atau datanya atau *flow*-nya. Lalu ada desain dari sisi penyimpanan datanya. Biasanya lalu ada desain antarmukanya. Ini kalau *software*. Jadi ada desain proses, lalu ada desain penyimpanan datanya, lalu ada desain UI-nya, antarmuka. Kalau *hardware*, ya ada detail *engineering design*-nya, perangkatnya desainnya seperti apa, lalu blok diagramnya bagaimana prosesnya mulai dari akuisisi sampai mengeluarkan *output*. Kalau ada PCB yang kalian bikin sendiri, ya itu juga didesain. Ditampilkan saja. Nah itu ya.

---

## Sesi 7: Jadwal dan Anggaran, Diskusi CD3-1 vs CD3-2, & Job Desc (35:15 – 40:14)

**\[35:15\] \[Dosen\]:**  
Lalu yang terakhir jadwal dan anggaran. Jadwal dan anggaran isinya jadwal implementasi rancangan, pembuatan *prototype* sampai dengan pengujian. Lalu anggaran berapa. Proses pengerjaan sedapat mungkin tidak lebih dari 6 bulan.

**\[35:50\] \[Mahasiswa 1\]:**  
*(Berbisik)* 6 bulan. 6 bulan. 6 bulan.

**\[36:00\] \[Dosen\]:**  
Kalau jadwal saya rasa cukup buat... menurut saya banyak sekali yang perlu diperbaiki. Ada yang mau ditanyakan? Kalau didiskusikan.

**\[36:26\] \[Mahasiswa 3\]:**  
Pak, saya lihat di jadwal itu kan CD3 itu kebagi dua ya, Pak, ada 3-1 sama 3-2. Itu tuh memang beda atau gimana ya, Pak? Soalnya dari *template* CD3 sendiri itu cuma satu doang.

**\[37:15\] \[Dosen\]:**  
Nanti saya konfirmasi dulu ya. Kalau nggak salah dulu tuh strip 1 itu memang dokumen ini-nya, lalu strip 2 itu mulai pengembangan *prototyping*-nya. *Prototyping*. Tapi saya pastikan dulu.

**\[38:05\] \[Dosen\]:**  
Sebenarnya CLO-nya ada dua ya, CLO 3 dan CLO 4. Jadi nanti kalian dalam menyusun dokumennya melihat di CLO 3 dan CLO 4. Jadi ada arsitektur, detail desain, jadwal kegiatan, pembagian tugas kelompok. Jadi jangan lupa itu nanti harus disebutkan juga. Waktu kalian bikin jadwal kegiatan, anggaran, pembagiannya juga harus di-*state* di situ ya. Ya ada pembagian kelompok dan *job desc* itu dituliskan dengan detail.

**\[38:55\] \[Mahasiswa 4\]:**  
Pak, sebelumnya aku izin bertanya. Kalau semisal ada perubahan *job desc* kelompok di pertengahan pengerjaan TA apakah boleh diubah?

**\[39:15\] \[Dosen\]:**  
Jangan berubah dari awalnya. Jadi harus tetap dari awal PTA-nya.

**\[39:30\] \[Mahasiswa 4\]:**  
Perubahan *job desc*-nya?

**\[39:35\] \[Dosen\]:**  
Ya harusnya nggak ya. Itu *job desc* utamanya. Ya misalkan nanti dinamikanya pada saat semester depan ternyata kelompoknya ada yang mengundurkan diri atau apa, ya otomatis kan berubah. Tapi di PTA ya kalian harus sudah bikin pembagiannya apa. Nanti kalau di semester depan yaitu ada yang mengundurkan diri dan ternyata kalian harus merangkap, ya nggak apa-apa juga. Tapi *job desc* awal kalian harus di-*state* jelas di dokumen.

---

## Sesi 8: Rangkuman Rubrik CD3 & Evaluasi UI Wireframe (40:15 – 43:35)

**\[40:15\] \[Dosen\]:**  
Jadi saya tegaskan untuk dokumen 3, CD3 itu rubriknya CLO 3 dan CLO 4. Jadi silakan nanti disesuaikan arsitekturnya. Jadi ada alternatif solusi, arsitektur sistem, detail desain, jadwal kegiatan, pembagian tugas kelompok dan anggaran. CLO-nya ini. Jadi rubriknya ini jadi silakan nanti disesuaikan.

**\[40:55\] \[Dosen\]:**  
Dan ini sekali lagi evaluasi saya terhadap dokumen-dokumen sebelum-sebelumnya. Kebanyakan kurangnya di situ. Saya harap ya kalian bisa lebih baik lagi dalam bikin dokumennya. Hal-hal fatal tuh kayak gini sebenarnya fatal. Kalian nggak boleh desain UML kalau ternyata nggak pakai *object-oriented programming* pendekatannya. Cuman kadang ada juga yang nggak ngawur gitu. Tapi saya nggak ngerti kenapa itu bisa...

**\[41:45\] \[Dosen\]:**  
Misalnya berupa model algoritma baru. Kalau algoritma baru dan kalian nggak pakai OOP, Python-nya *pure* biasa, kan nggak perlu pakai bikin UML dan kawan-kawan.

**\[42:10\] \[Dosen\]:**  
Lalu kebanyakan juga di sini ya, desain apa namanya tabel atau *database* juga biasanya langsung seperti ini. Ini nggak boleh. Lalu UI desain juga sebetulnya sama ya. Kalau kita ngomong nama desain, namanya desain itu sebenarnya masih berupa sketsa-sketsa biasa nih. *Layout*. Jadi posisinya ada di mana, *button*-nya apa. Tapi belum ada tuh namanya warnanya itu belum ada sebenarnya. Tampilan akhir warnanya itu yang ada warnanya, *form*-nya itu belum ada. Ini baru muncul nanti di pengembangan. Namanya juga *design* ya. Baru rancangan aja, sketsa-sketsa gitu. Kalau itu aja rancangan kasarnya gitu.

---

## Sesi 9: Tanya Jawab Revisi CD1/CD2 untuk Sempro & Tanda Tangan Basah (43:36 – 49:10)

**\[43:36\] \[Mahasiswa 2\]:**  
Pak, izin bertanya, Pak. Kalau sekarang file CD1 sama CD2 masih bisa diubah, Pak?

**\[43:45\] \[Dosen\]:**  
Nanti di akhir ada *link* pengumpulan gabungan. Tapi sekali lagi saya sampaikan, yang dinilai itu nanti dokumen yang sudah kalian kumpulkan sebelumnya. Itu yang jadi bahan penilaian. Bukan perubahan yang terakhir. Jadi supaya *"Pak, CD-nya udah saya benerin nih, udah bagus kenapa nilainya jelek?"* Ya karena bukan yang terakhir yang dipakai untuk nilai. Revisi itu memang perlu, maka yang dinilai itu pada saat *deadline-deadline*, *file-file* yang kalian kumpulkan saat *deadline*.

**\[44:45\] \[Mahasiswa 2\]:**  
Pak, berarti pas sempro-an nanti pakainya yang udah revisi?

**\[44:55\] \[Dosen\]:**  
Jadi ada dua dokumen. Dokumen gabungan itu yang akan digunakan oleh penguji sempro. Nah, dokumen *deadline* itu yang akan dinilai oleh saya dosen kelas. Jadi waktu seminar proposal kalian pakai dokumen terbaru yang sudah direvisi. Tapi yang saya nilai itu dokumen sesuai *deadline*.

**\[45:30\] \[Mahasiswa 2\]:**  
Kalau nanti... kan ini CD1 sama CD2 niatnya mau diubah, Pak. Berarti si CD3 yang dikerjakan sekarang otomatis bakal nggak nyambung dengan yang dikumpulin sebelumnya itu gimana nanti, Pak? Nilainya kecil atau...

**\[45:45\] \[Dosen\]:**  
Bisa jalan.

**\[45:50\] \[Mahasiswa 2\]:**  
Secara data kan nanti ada yang kurang sesuai, Pak, kayak lebar lokasi atau semacamnya.

**\[46:00\] \[Dosen\]:**  
Oh, nggak apa-apa.

**\[46:05\] \[Mahasiswa 2\]:**  
Nilai tetap aman?

**\[46:10\] \[Dosen\]:**  
Nilainya tetap aman.

**\[46:15\] \[Dosen\]:**  
Dan satu lagi ya, karena ini sudah jadi kesepakatan bersama, ketika ada kendala atau apa... jadi tolong dipastikan kalian kalau bisa dapat tanda tangan tuh di awal-awal. Ya selesaikan secepatnya. Jangan di akhir. Karena nggak tahu kondisi dosennya, dosen pembimbingnya lagi ada atau nggak, lagi berhalangan atau nggak. Karena sudah jadi kesepakatan dan kesepakatan juga bersama dengan dosen, jadi ya dengan terpaksa kalau kalian nggak dapat tanda tangan sampai hari-H, ya nggak bisa disidang.

**\[47:15\] \[Dosen\]:**  
Kemarin ada yang saya izinkan awalnya tapi ternyata setelah diskusi dengan para pengajar yang lain disepakati nggak boleh. Karena memang sudah disampaikan di awal bahwa harus basah. Jadi silakan ya diselesaikan sebelumnya. Makanya jangan dekat-dekat hari-H. Ada *spare* seminggu kalau bisa seminggu sebelumnya udah beres. Jadi masih ada waktu buat cari dosen.

**\[47:51\] \[Mahasiswa 1\]:**  
*(Berbisik)* Ya nggak apa-apa disesuaikan sama kebun kecil aja. Nggak ada masalah datanya jadi kurang relevan gitu.

---

## Sesi 10: Jadwal Presentasi, Syarat Bimbingan, Aturan Kelas, & Presensi (49:11 – 56:10)

**\[49:15\] \[Dosen\]:**  
Minggu depan ya mulai dipresentasikan. Jadi kalau minggu depan dua minggu berturut-turut itu ada presentasi ya tanggal 9 bisa kita liburkan untuk cari tanda tangan. Tapi kalau kalian misalnya... pokoknya jatahnya dua kali nih. Kalau minggu depan ternyata belum ada yang siap, ya berarti nanti tanggal 9-nya... Ya minggu depan mulai presentasi. Dokumen CD ya seperti biasa.

**\[51:05\] \[Mahasiswa 2\]:**  
Pak, izin bertanya lagi, Pak. Buat syarat bimbingan minimal lima kali itu, Pak, berarti pembimbing satu lima kali, pembimbing dua lima kali atau bagaimana ya, Pak?

**\[51:20\] \[Dosen\]:**  
Ada aturannya. Kalau pembimbing satu empat kali, pembimbing dua satu kali kan nggak adil ya.

**\[51:35\] \[Mahasiswa 2\]:**  
Harus disertakan bukti bimbingannya juga di dokumen, Pak, atau gimana, Pak?

**\[51:42\] \[Dosen\]:**  
Bikin aja *logbook* biasa ya. Dilampirkan di dokumennya.

**\[52:15\] \[Mahasiswa 2\]:**  
*(Berdiskusi pelan)* Bimbingan lima kali... pembimbing satu lima kali, pembimbing dua lima kali...

**\[53:10\] \[Mahasiswa 2\]:**  
*(Berdiskusi pelan)* 10 Desember... Edit, itu yang minimal bimbingan lima kali itu kumulatif dari yang awal atau baru sih?

**\[53:35\] \[Dosen\]:**  
Kalau mau izin nggak bisa waktu saat datang baru bilang *"Pak saya harus pulang"*. Kalau kalian mau keluar silakan sampaikan maksimal 20 menit sebelum kelasnya dimulai. Oke. Jadi saya ke depan kalau tiba-tiba datang sudah lewat jamnya saya nggak terima lagi. Ya.

**\[54:15\] \[Dosen\]:**  
*(Melakukan presensi akhir kelas)*  
Oke, siapa yang belum dipanggil ya? ... Maheswara? ... Azhar, Muhammad Azhar Ismail ... Zalfa, Zalfa Putri Anastasya...  
**\[Mahasiswa\]:** Izin, Pak.  
**\[Dosen\]:** Ayoga ... Aditya ... Najwan, Najwan Muhammad Fadlan ... Fahri ... Rafael ... Fauzan ... Silpa ... Adinda ... Raka ... Hafidz, Muhammad Hafidz Anwar ... Fathin ... Habizar ... Dimas ... Fani ... Zaki ... Naufal, Muhammad Naufal Cahya Ramadhan ... Farhan ... Nabila ... Asmi ... Intan ... Muhammad Bara Ali ... Zul ... Rahmat ... Muhammad Fikri Al-Karim ... Hilman ... Ahmad Gozali ... Farel ... Oke, presensi saya tutup ya. Terima kasih. Selamat siang, jangan lupa disiapkan.
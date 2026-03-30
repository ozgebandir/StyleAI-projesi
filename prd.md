# 👗 StyleAI - Akıllı Kıyafet Asistanı (PRD)

Bu belge, **StyleAI** projesinin kapsamını, teknik gereksinimlerini ve çalışma mantığını tanımlayan Ürün Gereksinim Belgesi'dir (PRD).

---

## 🚀 1. Ürün Özeti (Overview)
**StyleAI**, kullanıcının bulunduğu konumdaki anlık hava durumu verilerini analiz ederek, o hava şartlarına en uygun kıyafet kombinlerini öneren bir Python uygulamasıdır. Kullanıcıların "Bugün ne giysem?" kararsızlığını veriye dayalı bir çözümle gidermeyi hedefler.

## 🎯 2. Hedef Kitle
- Günlük giyim kararlarında pratiklik arayan kullanıcılar.
- Hava durumuna göre (yağmur, aşırı soğuk vb.) hazırlıksız yakalanmak istemeyen bireyler.

## 🛠 3. Teknik Gereksinimler & Teknoloji Yığını
- **Dil:** Python 3.10+
- **API:** [OpenWeatherMap API](https://openweathermap.org/api) (Hava durumu verileri için).
- **Arayüz:** Streamlit (Hızlı ve etkileşimli web arayüzü).
- **Kütüphaneler:** `requests`, `json`, `python-dotenv`.

## ⚙️ 4. Kullanıcı Senaryosu (User Flow)
1. Kullanıcı uygulamayı açar ve bulunduğu şehri girer.
2. Uygulama, arka planda Python ile hava durumu API'sine istek atar.
3. Gelen sıcaklık, rüzgar ve yağış verileri analiz edilir.
4. **StyleAI**, mantıksal katmanda (Logic Layer) belirlenen eşik değerlere göre öneri sunar:
   - *Örnek:* Sıcaklık < 10°C ise → "Kalın bir palto ve atkı almalısın."

## 📍 5. Gelecek Planları (Roadmap)
- [ ] Kullanıcının kendi gardırobundaki kıyafetleri yükleyebilmesi.
- [ ] Etkinlik tipine göre (Düğün, İş Görüşmesi, Spor) özelleştirilmiş öneriler.
- [ ] Görüntü işleme ile kıyafetlerin stil analizi.

---
*Bu proje Özge Bandır tarafından geliştirilmektedir.*
